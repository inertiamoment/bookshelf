# coding: utf-8
"""
    Kubernetes

    No description provided (generated by Swagger Codegen
    https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.14.4

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat
from six import iteritems
import re


class V1CSIPersistentVolumeSource(object):
  """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
  """
    Attributes:
      swagger_types (dict): The key is attribute name and the value is attribute
        type.
      attribute_map (dict): The key is attribute name and the value is json key
        in definition.
  """
  swagger_types = {
      'controller_publish_secret_ref': 'V1SecretReference',
      'driver': 'str',
      'fs_type': 'str',
      'node_publish_secret_ref': 'V1SecretReference',
      'node_stage_secret_ref': 'V1SecretReference',
      'read_only': 'bool',
      'volume_attributes': 'dict(str, str)',
      'volume_handle': 'str'
  }

  attribute_map = {
      'controller_publish_secret_ref': 'controllerPublishSecretRef',
      'driver': 'driver',
      'fs_type': 'fsType',
      'node_publish_secret_ref': 'nodePublishSecretRef',
      'node_stage_secret_ref': 'nodeStageSecretRef',
      'read_only': 'readOnly',
      'volume_attributes': 'volumeAttributes',
      'volume_handle': 'volumeHandle'
  }

  def __init__(self,
               controller_publish_secret_ref=None,
               driver=None,
               fs_type=None,
               node_publish_secret_ref=None,
               node_stage_secret_ref=None,
               read_only=None,
               volume_attributes=None,
               volume_handle=None):
    """
        V1CSIPersistentVolumeSource - a model defined in Swagger
        """

    self._controller_publish_secret_ref = None
    self._driver = None
    self._fs_type = None
    self._node_publish_secret_ref = None
    self._node_stage_secret_ref = None
    self._read_only = None
    self._volume_attributes = None
    self._volume_handle = None
    self.discriminator = None

    if controller_publish_secret_ref is not None:
      self.controller_publish_secret_ref = controller_publish_secret_ref
    self.driver = driver
    if fs_type is not None:
      self.fs_type = fs_type
    if node_publish_secret_ref is not None:
      self.node_publish_secret_ref = node_publish_secret_ref
    if node_stage_secret_ref is not None:
      self.node_stage_secret_ref = node_stage_secret_ref
    if read_only is not None:
      self.read_only = read_only
    if volume_attributes is not None:
      self.volume_attributes = volume_attributes
    self.volume_handle = volume_handle

  @property
  def controller_publish_secret_ref(self):
    """
        Gets the controller_publish_secret_ref of this
        V1CSIPersistentVolumeSource.
        ControllerPublishSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver to complete
        the CSI ControllerPublishVolume and ControllerUnpublishVolume calls.
        This field is optional, and may be empty if no secret is required. If
        the secret object contains more than one secret, all secrets are passed.

        :return: The controller_publish_secret_ref of this
        V1CSIPersistentVolumeSource.
        :rtype: V1SecretReference
        """
    return self._controller_publish_secret_ref

  @controller_publish_secret_ref.setter
  def controller_publish_secret_ref(self, controller_publish_secret_ref):
    """
        Sets the controller_publish_secret_ref of this
        V1CSIPersistentVolumeSource.
        ControllerPublishSecretRef is a reference to the secret object
        containing sensitive information to pass to the CSI driver to complete
        the CSI ControllerPublishVolume and ControllerUnpublishVolume calls.
        This field is optional, and may be empty if no secret is required. If
        the secret object contains more than one secret, all secrets are passed.

        :param controller_publish_secret_ref: The controller_publish_secret_ref
        of this V1CSIPersistentVolumeSource.
        :type: V1SecretReference
        """

    self._controller_publish_secret_ref = controller_publish_secret_ref

  @property
  def driver(self):
    """
        Gets the driver of this V1CSIPersistentVolumeSource.
        Driver is the name of the driver to use for this volume. Required.

        :return: The driver of this V1CSIPersistentVolumeSource.
        :rtype: str
        """
    return self._driver

  @driver.setter
  def driver(self, driver):
    """
        Sets the driver of this V1CSIPersistentVolumeSource.
        Driver is the name of the driver to use for this volume. Required.

        :param driver: The driver of this V1CSIPersistentVolumeSource.
        :type: str
        """
    if driver is None:
      raise ValueError('Invalid value for `driver`, must not be `None`')

    self._driver = driver

  @property
  def fs_type(self):
    """
        Gets the fs_type of this V1CSIPersistentVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the
        host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\".

        :return: The fs_type of this V1CSIPersistentVolumeSource.
        :rtype: str
        """
    return self._fs_type

  @fs_type.setter
  def fs_type(self, fs_type):
    """
        Sets the fs_type of this V1CSIPersistentVolumeSource.
        Filesystem type to mount. Must be a filesystem type supported by the
        host operating system. Ex. \"ext4\", \"xfs\", \"ntfs\".

        :param fs_type: The fs_type of this V1CSIPersistentVolumeSource.
        :type: str
        """

    self._fs_type = fs_type

  @property
  def node_publish_secret_ref(self):
    """
        Gets the node_publish_secret_ref of this V1CSIPersistentVolumeSource.
        NodePublishSecretRef is a reference to the secret object containing
        sensitive information to pass to the CSI driver to complete the CSI
        NodePublishVolume and NodeUnpublishVolume calls. This field is optional,
        and may be empty if no secret is required. If the secret object contains
        more than one secret, all secrets are passed.

        :return: The node_publish_secret_ref of this
        V1CSIPersistentVolumeSource.
        :rtype: V1SecretReference
        """
    return self._node_publish_secret_ref

  @node_publish_secret_ref.setter
  def node_publish_secret_ref(self, node_publish_secret_ref):
    """
        Sets the node_publish_secret_ref of this V1CSIPersistentVolumeSource.
        NodePublishSecretRef is a reference to the secret object containing
        sensitive information to pass to the CSI driver to complete the CSI
        NodePublishVolume and NodeUnpublishVolume calls. This field is optional,
        and may be empty if no secret is required. If the secret object contains
        more than one secret, all secrets are passed.

        :param node_publish_secret_ref: The node_publish_secret_ref of this
        V1CSIPersistentVolumeSource.
        :type: V1SecretReference
        """

    self._node_publish_secret_ref = node_publish_secret_ref

  @property
  def node_stage_secret_ref(self):
    """
        Gets the node_stage_secret_ref of this V1CSIPersistentVolumeSource.
        NodeStageSecretRef is a reference to the secret object containing
        sensitive information to pass to the CSI driver to complete the CSI
        NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This
        field is optional, and may be empty if no secret is required. If the
        secret object contains more than one secret, all secrets are passed.

        :return: The node_stage_secret_ref of this V1CSIPersistentVolumeSource.
        :rtype: V1SecretReference
        """
    return self._node_stage_secret_ref

  @node_stage_secret_ref.setter
  def node_stage_secret_ref(self, node_stage_secret_ref):
    """
        Sets the node_stage_secret_ref of this V1CSIPersistentVolumeSource.
        NodeStageSecretRef is a reference to the secret object containing
        sensitive information to pass to the CSI driver to complete the CSI
        NodeStageVolume and NodeStageVolume and NodeUnstageVolume calls. This
        field is optional, and may be empty if no secret is required. If the
        secret object contains more than one secret, all secrets are passed.

        :param node_stage_secret_ref: The node_stage_secret_ref of this
        V1CSIPersistentVolumeSource.
        :type: V1SecretReference
        """

    self._node_stage_secret_ref = node_stage_secret_ref

  @property
  def read_only(self):
    """
        Gets the read_only of this V1CSIPersistentVolumeSource.
        Optional: The value to pass to ControllerPublishVolumeRequest. Defaults
        to false (read/write).

        :return: The read_only of this V1CSIPersistentVolumeSource.
        :rtype: bool
        """
    return self._read_only

  @read_only.setter
  def read_only(self, read_only):
    """
        Sets the read_only of this V1CSIPersistentVolumeSource.
        Optional: The value to pass to ControllerPublishVolumeRequest. Defaults
        to false (read/write).

        :param read_only: The read_only of this V1CSIPersistentVolumeSource.
        :type: bool
        """

    self._read_only = read_only

  @property
  def volume_attributes(self):
    """
        Gets the volume_attributes of this V1CSIPersistentVolumeSource.
        Attributes of the volume to publish.

        :return: The volume_attributes of this V1CSIPersistentVolumeSource.
        :rtype: dict(str, str)
        """
    return self._volume_attributes

  @volume_attributes.setter
  def volume_attributes(self, volume_attributes):
    """
        Sets the volume_attributes of this V1CSIPersistentVolumeSource.
        Attributes of the volume to publish.

        :param volume_attributes: The volume_attributes of this
        V1CSIPersistentVolumeSource.
        :type: dict(str, str)
        """

    self._volume_attributes = volume_attributes

  @property
  def volume_handle(self):
    """
        Gets the volume_handle of this V1CSIPersistentVolumeSource.
        VolumeHandle is the unique volume name returned by the CSI volume
        plugin’s CreateVolume to refer to the volume on all subsequent calls.
        Required.

        :return: The volume_handle of this V1CSIPersistentVolumeSource.
        :rtype: str
        """
    return self._volume_handle

  @volume_handle.setter
  def volume_handle(self, volume_handle):
    """
        Sets the volume_handle of this V1CSIPersistentVolumeSource.
        VolumeHandle is the unique volume name returned by the CSI volume
        plugin’s CreateVolume to refer to the volume on all subsequent calls.
        Required.

        :param volume_handle: The volume_handle of this
        V1CSIPersistentVolumeSource.
        :type: str
        """
    if volume_handle is None:
      raise ValueError('Invalid value for `volume_handle`, must not be `None`')

    self._volume_handle = volume_handle

  def to_dict(self):
    """
        Returns the model properties as a dict
        """
    result = {}

    for attr, _ in iteritems(self.swagger_types):
      value = getattr(self, attr)
      if isinstance(value, list):
        result[attr] = list(
            map(lambda x: x.to_dict() if hasattr(x, 'to_dict') else x, value))
      elif hasattr(value, 'to_dict'):
        result[attr] = value.to_dict()
      elif isinstance(value, dict):
        result[attr] = dict(
            map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], 'to_dict') else item, value.items()))
      else:
        result[attr] = value

    return result

  def to_str(self):
    """
        Returns the string representation of the model
        """
    return pformat(self.to_dict())

  def __repr__(self):
    """
        For `print` and `pprint`
        """
    return self.to_str()

  def __eq__(self, other):
    """
        Returns true if both objects are equal
        """
    if not isinstance(other, V1CSIPersistentVolumeSource):
      return False

    return self.__dict__ == other.__dict__

  def __ne__(self, other):
    """
        Returns true if both objects are not equal
        """
    return not self == other
