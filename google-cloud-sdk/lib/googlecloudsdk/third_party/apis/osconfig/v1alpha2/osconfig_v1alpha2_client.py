"""Generated client library for osconfig version v1alpha2."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.osconfig.v1alpha2 import osconfig_v1alpha2_messages as messages


class OsconfigV1alpha2(base_api.BaseApiClient):
  """Generated client library for service osconfig version v1alpha2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://osconfig.googleapis.com/'
  MTLS_BASE_URL = 'https://osconfig.mtls.googleapis.com/'

  _PACKAGE = 'osconfig'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'OsconfigV1alpha2'
  _URL_VERSION = 'v1alpha2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new osconfig handle."""
    url = url or self.BASE_URL
    super(OsconfigV1alpha2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.folders_guestPolicies = self.FoldersGuestPoliciesService(self)
    self.folders = self.FoldersService(self)
    self.organizations_guestPolicies = self.OrganizationsGuestPoliciesService(self)
    self.organizations = self.OrganizationsService(self)
    self.projects_guestPolicies = self.ProjectsGuestPoliciesService(self)
    self.projects_patchDeployments = self.ProjectsPatchDeploymentsService(self)
    self.projects_patchJobs_instanceDetails = self.ProjectsPatchJobsInstanceDetailsService(self)
    self.projects_patchJobs = self.ProjectsPatchJobsService(self)
    self.projects_zones_instances = self.ProjectsZonesInstancesService(self)
    self.projects_zones = self.ProjectsZonesService(self)
    self.projects = self.ProjectsService(self)

  class FoldersGuestPoliciesService(base_api.BaseApiService):
    """Service class for the folders_guestPolicies resource."""

    _NAME = 'folders_guestPolicies'

    def __init__(self, client):
      super(OsconfigV1alpha2.FoldersGuestPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS Config Guest Policy.

      Args:
        request: (OsconfigFoldersGuestPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/folders/{foldersId}/guestPolicies',
        http_method='POST',
        method_id='osconfig.folders.guestPolicies.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['guestPolicyId'],
        relative_path='v1alpha2/{+parent}/guestPolicies',
        request_field='guestPolicy',
        request_type_name='OsconfigFoldersGuestPoliciesCreateRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an OS Config GuestPolicy.

      Args:
        request: (OsconfigFoldersGuestPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/folders/{foldersId}/guestPolicies/{guestPoliciesId}',
        http_method='DELETE',
        method_id='osconfig.folders.guestPolicies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigFoldersGuestPoliciesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an OS Config GuestPolicy.

      Args:
        request: (OsconfigFoldersGuestPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/folders/{foldersId}/guestPolicies/{guestPoliciesId}',
        http_method='GET',
        method_id='osconfig.folders.guestPolicies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigFoldersGuestPoliciesGetRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of OS Config GuestPolicies.

      Args:
        request: (OsconfigFoldersGuestPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGuestPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/folders/{foldersId}/guestPolicies',
        http_method='GET',
        method_id='osconfig.folders.guestPolicies.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha2/{+parent}/guestPolicies',
        request_field='',
        request_type_name='OsconfigFoldersGuestPoliciesListRequest',
        response_type_name='ListGuestPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an OS Config GuestPolicy.

      Args:
        request: (OsconfigFoldersGuestPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/folders/{foldersId}/guestPolicies/{guestPoliciesId}',
        http_method='PATCH',
        method_id='osconfig.folders.guestPolicies.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha2/{+name}',
        request_field='guestPolicy',
        request_type_name='OsconfigFoldersGuestPoliciesPatchRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

  class FoldersService(base_api.BaseApiService):
    """Service class for the folders resource."""

    _NAME = 'folders'

    def __init__(self, client):
      super(OsconfigV1alpha2.FoldersService, self).__init__(client)
      self._upload_configs = {
          }

  class OrganizationsGuestPoliciesService(base_api.BaseApiService):
    """Service class for the organizations_guestPolicies resource."""

    _NAME = 'organizations_guestPolicies'

    def __init__(self, client):
      super(OsconfigV1alpha2.OrganizationsGuestPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS Config Guest Policy.

      Args:
        request: (OsconfigOrganizationsGuestPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/organizations/{organizationsId}/guestPolicies',
        http_method='POST',
        method_id='osconfig.organizations.guestPolicies.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['guestPolicyId'],
        relative_path='v1alpha2/{+parent}/guestPolicies',
        request_field='guestPolicy',
        request_type_name='OsconfigOrganizationsGuestPoliciesCreateRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an OS Config GuestPolicy.

      Args:
        request: (OsconfigOrganizationsGuestPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/organizations/{organizationsId}/guestPolicies/{guestPoliciesId}',
        http_method='DELETE',
        method_id='osconfig.organizations.guestPolicies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigOrganizationsGuestPoliciesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an OS Config GuestPolicy.

      Args:
        request: (OsconfigOrganizationsGuestPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/organizations/{organizationsId}/guestPolicies/{guestPoliciesId}',
        http_method='GET',
        method_id='osconfig.organizations.guestPolicies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigOrganizationsGuestPoliciesGetRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of OS Config GuestPolicies.

      Args:
        request: (OsconfigOrganizationsGuestPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGuestPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/organizations/{organizationsId}/guestPolicies',
        http_method='GET',
        method_id='osconfig.organizations.guestPolicies.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha2/{+parent}/guestPolicies',
        request_field='',
        request_type_name='OsconfigOrganizationsGuestPoliciesListRequest',
        response_type_name='ListGuestPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an OS Config GuestPolicy.

      Args:
        request: (OsconfigOrganizationsGuestPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/organizations/{organizationsId}/guestPolicies/{guestPoliciesId}',
        http_method='PATCH',
        method_id='osconfig.organizations.guestPolicies.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha2/{+name}',
        request_field='guestPolicy',
        request_type_name='OsconfigOrganizationsGuestPoliciesPatchRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

  class OrganizationsService(base_api.BaseApiService):
    """Service class for the organizations resource."""

    _NAME = 'organizations'

    def __init__(self, client):
      super(OsconfigV1alpha2.OrganizationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsGuestPoliciesService(base_api.BaseApiService):
    """Service class for the projects_guestPolicies resource."""

    _NAME = 'projects_guestPolicies'

    def __init__(self, client):
      super(OsconfigV1alpha2.ProjectsGuestPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS Config Guest Policy.

      Args:
        request: (OsconfigProjectsGuestPoliciesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/guestPolicies',
        http_method='POST',
        method_id='osconfig.projects.guestPolicies.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['guestPolicyId'],
        relative_path='v1alpha2/{+parent}/guestPolicies',
        request_field='guestPolicy',
        request_type_name='OsconfigProjectsGuestPoliciesCreateRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an OS Config GuestPolicy.

      Args:
        request: (OsconfigProjectsGuestPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/guestPolicies/{guestPoliciesId}',
        http_method='DELETE',
        method_id='osconfig.projects.guestPolicies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsGuestPoliciesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an OS Config GuestPolicy.

      Args:
        request: (OsconfigProjectsGuestPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/guestPolicies/{guestPoliciesId}',
        http_method='GET',
        method_id='osconfig.projects.guestPolicies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsGuestPoliciesGetRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of OS Config GuestPolicies.

      Args:
        request: (OsconfigProjectsGuestPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGuestPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/guestPolicies',
        http_method='GET',
        method_id='osconfig.projects.guestPolicies.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha2/{+parent}/guestPolicies',
        request_field='',
        request_type_name='OsconfigProjectsGuestPoliciesListRequest',
        response_type_name='ListGuestPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an OS Config GuestPolicy.

      Args:
        request: (OsconfigProjectsGuestPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GuestPolicy) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/guestPolicies/{guestPoliciesId}',
        http_method='PATCH',
        method_id='osconfig.projects.guestPolicies.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha2/{+name}',
        request_field='guestPolicy',
        request_type_name='OsconfigProjectsGuestPoliciesPatchRequest',
        response_type_name='GuestPolicy',
        supports_download=False,
    )

  class ProjectsPatchDeploymentsService(base_api.BaseApiService):
    """Service class for the projects_patchDeployments resource."""

    _NAME = 'projects_patchDeployments'

    def __init__(self, client):
      super(OsconfigV1alpha2.ProjectsPatchDeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS Config Patch Deployment.

      Args:
        request: (OsconfigProjectsPatchDeploymentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchDeployment) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchDeployments',
        http_method='POST',
        method_id='osconfig.projects.patchDeployments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['patchDeploymentId'],
        relative_path='v1alpha2/{+parent}/patchDeployments',
        request_field='patchDeployment',
        request_type_name='OsconfigProjectsPatchDeploymentsCreateRequest',
        response_type_name='PatchDeployment',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an OS Config Patch Deployment.

      Args:
        request: (OsconfigProjectsPatchDeploymentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchDeployments/{patchDeploymentsId}',
        http_method='DELETE',
        method_id='osconfig.projects.patchDeployments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsPatchDeploymentsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an OS Config Patch Deployment.

      Args:
        request: (OsconfigProjectsPatchDeploymentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchDeployment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchDeployments/{patchDeploymentsId}',
        http_method='GET',
        method_id='osconfig.projects.patchDeployments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsPatchDeploymentsGetRequest',
        response_type_name='PatchDeployment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of OS Config Patch Deployments.

      Args:
        request: (OsconfigProjectsPatchDeploymentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPatchDeploymentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchDeployments',
        http_method='GET',
        method_id='osconfig.projects.patchDeployments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1alpha2/{+parent}/patchDeployments',
        request_field='',
        request_type_name='OsconfigProjectsPatchDeploymentsListRequest',
        response_type_name='ListPatchDeploymentsResponse',
        supports_download=False,
    )

  class ProjectsPatchJobsInstanceDetailsService(base_api.BaseApiService):
    """Service class for the projects_patchJobs_instanceDetails resource."""

    _NAME = 'projects_patchJobs_instanceDetails'

    def __init__(self, client):
      super(OsconfigV1alpha2.ProjectsPatchJobsInstanceDetailsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Get a page of instances' details for a given patch job.

      Args:
        request: (OsconfigProjectsPatchJobsInstanceDetailsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPatchJobInstanceDetailsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchJobs/{patchJobsId}/instanceDetails',
        http_method='GET',
        method_id='osconfig.projects.patchJobs.instanceDetails.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha2/{+parent}/instanceDetails',
        request_field='',
        request_type_name='OsconfigProjectsPatchJobsInstanceDetailsListRequest',
        response_type_name='ListPatchJobInstanceDetailsResponse',
        supports_download=False,
    )

  class ProjectsPatchJobsService(base_api.BaseApiService):
    """Service class for the projects_patchJobs resource."""

    _NAME = 'projects_patchJobs'

    def __init__(self, client):
      super(OsconfigV1alpha2.ProjectsPatchJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted.

      Args:
        request: (OsconfigProjectsPatchJobsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchJob) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchJobs/{patchJobsId}:cancel',
        http_method='POST',
        method_id='osconfig.projects.patchJobs.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}:cancel',
        request_field='cancelPatchJobRequest',
        request_type_name='OsconfigProjectsPatchJobsCancelRequest',
        response_type_name='PatchJob',
        supports_download=False,
    )

    def Execute(self, request, global_params=None):
      r"""Patch VM instances by creating and running a PatchJob.

      Args:
        request: (OsconfigProjectsPatchJobsExecuteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchJob) The response message.
      """
      config = self.GetMethodConfig('Execute')
      return self._RunMethod(
          config, request, global_params=global_params)

    Execute.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchJobs:execute',
        http_method='POST',
        method_id='osconfig.projects.patchJobs.execute',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha2/{+parent}/patchJobs:execute',
        request_field='executePatchJobRequest',
        request_type_name='OsconfigProjectsPatchJobsExecuteRequest',
        response_type_name='PatchJob',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs.

      Args:
        request: (OsconfigProjectsPatchJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PatchJob) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchJobs/{patchJobsId}',
        http_method='GET',
        method_id='osconfig.projects.patchJobs.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha2/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsPatchJobsGetRequest',
        response_type_name='PatchJob',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of patch jobs.

      Args:
        request: (OsconfigProjectsPatchJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPatchJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/patchJobs',
        http_method='GET',
        method_id='osconfig.projects.patchJobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha2/{+parent}/patchJobs',
        request_field='',
        request_type_name='OsconfigProjectsPatchJobsListRequest',
        response_type_name='ListPatchJobsResponse',
        supports_download=False,
    )

  class ProjectsZonesInstancesService(base_api.BaseApiService):
    """Service class for the projects_zones_instances resource."""

    _NAME = 'projects_zones_instances'

    def __init__(self, client):
      super(OsconfigV1alpha2.ProjectsZonesInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def LookupGuestPolicies(self, request, global_params=None):
      r"""Lookup the guest policies that are assigned to a VM instance. This lookup will merge all policies that are assigned to the instance. This is usually called by the agent running on the instance, but it can also be called by users to see what configs are assigned to this instance.

      Args:
        request: (OsconfigProjectsZonesInstancesLookupGuestPoliciesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LookupEffectiveGuestPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('LookupGuestPolicies')
      return self._RunMethod(
          config, request, global_params=global_params)

    LookupGuestPolicies.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha2/projects/{projectsId}/zones/{zonesId}/instances/{instancesId}:lookupGuestPolicies',
        http_method='POST',
        method_id='osconfig.projects.zones.instances.lookupGuestPolicies',
        ordered_params=['instance'],
        path_params=['instance'],
        query_params=[],
        relative_path='v1alpha2/{+instance}:lookupGuestPolicies',
        request_field='lookupEffectiveGuestPoliciesRequest',
        request_type_name='OsconfigProjectsZonesInstancesLookupGuestPoliciesRequest',
        response_type_name='LookupEffectiveGuestPoliciesResponse',
        supports_download=False,
    )

  class ProjectsZonesService(base_api.BaseApiService):
    """Service class for the projects_zones resource."""

    _NAME = 'projects_zones'

    def __init__(self, client):
      super(OsconfigV1alpha2.ProjectsZonesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(OsconfigV1alpha2.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
