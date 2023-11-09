# -*- coding: utf-8 -*- #
# Copyright 2017 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The cli_tree command help document markdown generator.

This module generates command help markdown from the tree generated by:

  gcloud --quiet alpha  # make sure the alpha component is installed
  gcloud --quiet beta   # make sure the beta component is installed
  gcloud meta list-gcloud --format=json |
  python -c "
    import json
    import sys
    data = json.load(sys.stdin)
    print 'gcloud_tree =', data" > gcloud_tree.py

Usage:

  from googlecloudsdk.calliope import cli_tree_markdown
  from googlecloudsdk.command_lib.shell import gcloud_tree

  command = <command node in gcloud tree>
  flag = <flag node in gcloud tree>
  generator = cli_tree_markdown.CliTreeMarkdownGenerator(command, gcloud_tree)
  generator.PrintSynopsisSection()
  generator.PrintFlagDefinition(flag)
    ...
  markdown = generator.Edit()
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import cli_tree
from googlecloudsdk.calliope import markdown
from googlecloudsdk.calliope import usage_text
from googlecloudsdk.core import properties

import six


if six.PY2:
  FLAG_TYPE_NAME = b'flag'
  POSITIONAL_TYPE_NAME = b'positional'
  GROUP_TYPE_NAME = b'group'
else:
  FLAG_TYPE_NAME = 'flag'
  POSITIONAL_TYPE_NAME = 'positional'
  GROUP_TYPE_NAME = 'group'


def _GetReleaseTrackFromId(release_id):
  """Returns the base.ReleaseTrack for release_id."""
  if release_id == 'INTERNAL':
    release_id = 'GA'
  return base.ReleaseTrack.FromId(release_id)


def Flag(d):
  """Returns a flag object suitable for the calliope.markdown module."""
  flag = type(FLAG_TYPE_NAME, (object,), d)
  flag.is_group = False
  flag.is_hidden = d.get(cli_tree.LOOKUP_IS_HIDDEN, d.get('hidden', False))
  flag.hidden = flag.is_hidden
  flag.is_positional = False
  flag.is_required = d.get(cli_tree.LOOKUP_IS_REQUIRED,
                           d.get(cli_tree.LOOKUP_REQUIRED, False))
  flag.required = flag.is_required
  flag.help = flag.description
  flag.dest = flag.name.lower().replace('-', '_')
  flag.metavar = flag.value
  flag.option_strings = [flag.name]
  if not hasattr(flag, 'default'):
    flag.default = None

  if flag.type == 'bool':
    flag.nargs = 0
  elif flag.nargs not in ('?', '*', '+'):
    flag.nargs = 1
  if flag.type == 'dict':
    flag.type = arg_parsers.ArgDict()
  elif flag.type == 'list':
    flag.type = arg_parsers.ArgList()
  elif flag.type == 'string':
    flag.type = None

  if flag.attr.get(cli_tree.LOOKUP_INVERTED_SYNOPSIS):
    flag.inverted_synopsis = True
  prop = flag.attr.get('property')
  if prop:
    if cli_tree.LOOKUP_VALUE in prop:
      kind = 'value'
      value = prop[cli_tree.LOOKUP_VALUE]
    else:
      value = None
      kind = 'bool' if flag.type == 'bool' else None
    flag.store_property = (properties.FromString(
        prop[cli_tree.LOOKUP_NAME]), kind, value)

  return flag


def Positional(d):
  """Returns a positional object suitable for the calliope.markdown module."""
  positional = type(POSITIONAL_TYPE_NAME, (object,), d)
  positional.help = positional.description
  positional.is_group = False
  positional.is_hidden = False
  positional.is_positional = True
  positional.is_required = positional.nargs != '*'
  positional.dest = positional.value.lower().replace('-', '_')
  positional.metavar = positional.value
  positional.option_strings = []
  try:
    positional.nargs = int(positional.nargs)
  except ValueError:
    pass
  return positional


def Argument(d):
  """Returns an argument object suitable for the calliope.markdown module."""
  if d.get(cli_tree.LOOKUP_IS_POSITIONAL, False):
    return Positional(d)
  if not d.get(cli_tree.LOOKUP_IS_GROUP, False):
    return Flag(d)
  group = type(GROUP_TYPE_NAME, (object,), d)
  group.arguments = [Argument(a) for a in d.get(cli_tree.LOOKUP_ARGUMENTS, [])]
  group.category = None
  group.help = group.description
  group.is_global = False
  group.is_hidden = False
  group.sort_args = True
  return group


class CliTreeMarkdownGenerator(markdown.MarkdownGenerator):
  """cli_tree command help markdown document generator.

  Attributes:
    _capsule: The help text capsule.
    _command: The tree node for command.
    _command_path: The command path list.
    _tree: The (sub)tree root.
    _sections: The help text sections indexed by SECTION name.
    _subcommands: The dict of subcommand help indexed by subcommand name.
    _subgroups: The dict of subgroup help indexed by subcommand name.
  """

  def __init__(self, command, tree):
    """Constructor.

    Args:
      command: The command node in the root tree.
      tree: The (sub)tree root.
    """
    self._tree = tree
    self._command = command
    self._command_path = command[cli_tree.LOOKUP_PATH]
    super(CliTreeMarkdownGenerator, self).__init__(
        self._command_path,
        _GetReleaseTrackFromId(self._command[cli_tree.LOOKUP_RELEASE]),
        self._command.get(cli_tree.LOOKUP_IS_HIDDEN,
                          self._command.get('hidden', False)))
    self._capsule = self._command[cli_tree.LOOKUP_CAPSULE]
    self._sections = self._command[cli_tree.LOOKUP_SECTIONS]
    self._subcommands = self.GetSubCommandHelp()
    self._subgroups = self.GetSubGroupHelp()

  def _GetCommandFromPath(self, command_path):
    """Returns the command node for command_path."""
    path = self._tree[cli_tree.LOOKUP_PATH]
    if path:
      # self._tree is not a super root. The first path name must match.
      if command_path[:1] != path:
        return None
      # Already checked the first name.
      command_path = command_path[1:]
    command = self._tree
    for name in command_path:
      commands = command[cli_tree.LOOKUP_COMMANDS]
      if name not in commands:
        return None
      command = commands[name]
    return command

  def IsValidSubPath(self, command_path):
    """Returns True if the given command path after the top is valid."""
    return self._GetCommandFromPath([cli_tree.DEFAULT_CLI_NAME] +
                                    command_path) is not None

  def GetArguments(self):
    """Returns the command arguments."""
    command = self._GetCommandFromPath(self._command_path)
    try:
      return [Argument(a) for a in
              command[cli_tree.LOOKUP_CONSTRAINTS][cli_tree.LOOKUP_ARGUMENTS]]
    except (KeyError, TypeError):
      return []

  def GetArgDetails(self, arg, depth=None):
    """Returns the help text with auto-generated details for arg.

    The help text was already generated on the cli_tree generation side.

    Args:
      arg: The arg to auto-generate help text for.
      depth: The indentation depth at which the details should be printed.
        Added here only to maintain consistency with superclass during testing.

    Returns:
      The help text with auto-generated details for arg.
    """
    return arg.help

  def _GetSubHelp(self, is_group=False):
    """Returns the help dict indexed by command for sub commands or groups."""
    return {name: usage_text.HelpInfo(
        help_text=subcommand[cli_tree.LOOKUP_CAPSULE],
        is_hidden=subcommand.get(cli_tree.LOOKUP_IS_HIDDEN,
                                 subcommand.get('hidden', False)),
        release_track=_GetReleaseTrackFromId(
            subcommand[cli_tree.LOOKUP_RELEASE]))
            for name, subcommand in six.iteritems(self._command[
                cli_tree.LOOKUP_COMMANDS])
            if subcommand[cli_tree.LOOKUP_IS_GROUP] == is_group}

  def GetSubCommandHelp(self):
    """Returns the subcommand help dict indexed by subcommand."""
    return self._GetSubHelp(is_group=False)

  def GetSubGroupHelp(self):
    """Returns the subgroup help dict indexed by subgroup."""
    return self._GetSubHelp(is_group=True)

  def PrintFlagDefinition(self, flag, disable_header=False):
    """Prints a flags definition list item."""
    if isinstance(flag, dict):
      flag = Flag(flag)
    super(CliTreeMarkdownGenerator, self).PrintFlagDefinition(
        flag, disable_header=disable_header)

  def _ExpandHelpText(self, doc):
    """{...} references were done when the tree was generated."""
    return doc


def Markdown(command, tree):
  """Returns the help markdown document string for the command node in tree.

  Args:
    command: The command node in the root tree.
    tree: The (sub)tree root.

  Returns:
    The markdown document string.
  """
  return CliTreeMarkdownGenerator(command, tree).Generate()
