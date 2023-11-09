"""Generated client library for osconfig version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.osconfig.v1 import osconfig_v1_messages as messages


class OsconfigV1(base_api.BaseApiClient):
  """Generated client library for service osconfig version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://osconfig.googleapis.com/'
  MTLS_BASE_URL = 'https://osconfig.mtls.googleapis.com/'

  _PACKAGE = 'osconfig'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'OsconfigV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new osconfig handle."""
    url = url or self.BASE_URL
    super(OsconfigV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_instances_inventories = self.ProjectsLocationsInstancesInventoriesService(self)
    self.projects_locations_instances_vulnerabilityReports = self.ProjectsLocationsInstancesVulnerabilityReportsService(self)
    self.projects_locations_instances = self.ProjectsLocationsInstancesService(self)
    self.projects_locations_osPolicyAssignments_operations = self.ProjectsLocationsOsPolicyAssignmentsOperationsService(self)
    self.projects_locations_osPolicyAssignments = self.ProjectsLocationsOsPolicyAssignmentsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects_patchDeployments = self.ProjectsPatchDeploymentsService(self)
    self.projects_patchJobs_instanceDetails = self.ProjectsPatchJobsInstanceDetailsService(self)
    self.projects_patchJobs = self.ProjectsPatchJobsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsInstancesInventoriesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances_inventories resource."""

    _NAME = 'projects_locations_instances_inventories'

    def __init__(self, client):
      super(OsconfigV1.ProjectsLocationsInstancesInventoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Get inventory data for the specified VM instance. If the VM has no associated inventory, the message `NOT_FOUND` is returned.

      Args:
        request: (OsconfigProjectsLocationsInstancesInventoriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Inventory) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/inventory',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.inventories.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['view'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesInventoriesGetRequest',
        response_type_name='Inventory',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List inventory data for all VM instances in the specified zone.

      Args:
        request: (OsconfigProjectsLocationsInstancesInventoriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInventoriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/inventories',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.inventories.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken', 'view'],
        relative_path='v1/{+parent}/inventories',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesInventoriesListRequest',
        response_type_name='ListInventoriesResponse',
        supports_download=False,
    )

  class ProjectsLocationsInstancesVulnerabilityReportsService(base_api.BaseApiService):
    """Service class for the projects_locations_instances_vulnerabilityReports resource."""

    _NAME = 'projects_locations_instances_vulnerabilityReports'

    def __init__(self, client):
      super(OsconfigV1.ProjectsLocationsInstancesVulnerabilityReportsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the vulnerability report for the specified VM instance. Only VMs with inventory data have vulnerability reports associated with them.

      Args:
        request: (OsconfigProjectsLocationsInstancesVulnerabilityReportsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (VulnerabilityReport) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/vulnerabilityReport',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.vulnerabilityReports.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesVulnerabilityReportsGetRequest',
        response_type_name='VulnerabilityReport',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List vulnerability reports for all VM instances in the specified zone.

      Args:
        request: (OsconfigProjectsLocationsInstancesVulnerabilityReportsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVulnerabilityReportsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}/vulnerabilityReports',
        http_method='GET',
        method_id='osconfig.projects.locations.instances.vulnerabilityReports.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/vulnerabilityReports',
        request_field='',
        request_type_name='OsconfigProjectsLocationsInstancesVulnerabilityReportsListRequest',
        response_type_name='ListVulnerabilityReportsResponse',
        supports_download=False,
    )

  class ProjectsLocationsInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances resource."""

    _NAME = 'projects_locations_instances'

    def __init__(self, client):
      super(OsconfigV1.ProjectsLocationsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsOsPolicyAssignmentsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_osPolicyAssignments_operations resource."""

    _NAME = 'projects_locations_osPolicyAssignments_operations'

    def __init__(self, client):
      super(OsconfigV1.ProjectsLocationsOsPolicyAssignmentsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='osconfig.projects.locations.osPolicyAssignments.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}/operations/{operationsId}',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOsPolicyAssignmentsService(base_api.BaseApiService):
    """Service class for the projects_locations_osPolicyAssignments resource."""

    _NAME = 'projects_locations_osPolicyAssignments'

    def __init__(self, client):
      super(OsconfigV1.ProjectsLocationsOsPolicyAssignmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS policy assignment. This method also creates the first revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments',
        http_method='POST',
        method_id='osconfig.projects.locations.osPolicyAssignments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['osPolicyAssignmentId'],
        relative_path='v1/{+parent}/osPolicyAssignments',
        request_field='oSPolicyAssignment',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete the OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. If the LRO completes and is not cancelled, all revisions associated with the OS policy assignment are deleted. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}',
        http_method='DELETE',
        method_id='osconfig.projects.locations.osPolicyAssignments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieve an existing OS policy assignment. This method always returns the latest revision. In order to retrieve a previous revision of the assignment, also provide the revision ID in the `name` parameter.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (OSPolicyAssignment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsGetRequest',
        response_type_name='OSPolicyAssignment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List the OS policy assignments under the parent resource. For each OS policy assignment, the latest revision is returned.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOSPolicyAssignmentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/osPolicyAssignments',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsListRequest',
        response_type_name='ListOSPolicyAssignmentsResponse',
        supports_download=False,
    )

    def ListRevisions(self, request, global_params=None):
      r"""List the OS policy assignment revisions for a given OS policy assignment.

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsListRevisionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOSPolicyAssignmentRevisionsResponse) The response message.
      """
      config = self.GetMethodConfig('ListRevisions')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListRevisions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}:listRevisions',
        http_method='GET',
        method_id='osconfig.projects.locations.osPolicyAssignments.listRevisions',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+name}:listRevisions',
        request_field='',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsListRevisionsRequest',
        response_type_name='ListOSPolicyAssignmentRevisionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an existing OS policy assignment. This method creates a new revision of the OS policy assignment. This method returns a long running operation (LRO) that contains the rollout details. The rollout can be cancelled by cancelling the LRO. For more information, see [Method: projects.locations.osPolicyAssignments.operations.cancel](https://cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel).

      Args:
        request: (OsconfigProjectsLocationsOsPolicyAssignmentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/osPolicyAssignments/{osPolicyAssignmentsId}',
        http_method='PATCH',
        method_id='osconfig.projects.locations.osPolicyAssignments.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='oSPolicyAssignment',
        request_type_name='OsconfigProjectsLocationsOsPolicyAssignmentsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(OsconfigV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsPatchDeploymentsService(base_api.BaseApiService):
    """Service class for the projects_patchDeployments resource."""

    _NAME = 'projects_patchDeployments'

    def __init__(self, client):
      super(OsconfigV1.ProjectsPatchDeploymentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an OS Config patch deployment.

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
        flat_path='v1/projects/{projectsId}/patchDeployments',
        http_method='POST',
        method_id='osconfig.projects.patchDeployments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['patchDeploymentId'],
        relative_path='v1/{+parent}/patchDeployments',
        request_field='patchDeployment',
        request_type_name='OsconfigProjectsPatchDeploymentsCreateRequest',
        response_type_name='PatchDeployment',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an OS Config patch deployment.

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
        flat_path='v1/projects/{projectsId}/patchDeployments/{patchDeploymentsId}',
        http_method='DELETE',
        method_id='osconfig.projects.patchDeployments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsPatchDeploymentsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an OS Config patch deployment.

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
        flat_path='v1/projects/{projectsId}/patchDeployments/{patchDeploymentsId}',
        http_method='GET',
        method_id='osconfig.projects.patchDeployments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsPatchDeploymentsGetRequest',
        response_type_name='PatchDeployment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a page of OS Config patch deployments.

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
        flat_path='v1/projects/{projectsId}/patchDeployments',
        http_method='GET',
        method_id='osconfig.projects.patchDeployments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/patchDeployments',
        request_field='',
        request_type_name='OsconfigProjectsPatchDeploymentsListRequest',
        response_type_name='ListPatchDeploymentsResponse',
        supports_download=False,
    )

  class ProjectsPatchJobsInstanceDetailsService(base_api.BaseApiService):
    """Service class for the projects_patchJobs_instanceDetails resource."""

    _NAME = 'projects_patchJobs_instanceDetails'

    def __init__(self, client):
      super(OsconfigV1.ProjectsPatchJobsInstanceDetailsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      r"""Get a list of instance details for a given patch job.

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
        flat_path='v1/projects/{projectsId}/patchJobs/{patchJobsId}/instanceDetails',
        http_method='GET',
        method_id='osconfig.projects.patchJobs.instanceDetails.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/instanceDetails',
        request_field='',
        request_type_name='OsconfigProjectsPatchJobsInstanceDetailsListRequest',
        response_type_name='ListPatchJobInstanceDetailsResponse',
        supports_download=False,
    )

  class ProjectsPatchJobsService(base_api.BaseApiService):
    """Service class for the projects_patchJobs resource."""

    _NAME = 'projects_patchJobs'

    def __init__(self, client):
      super(OsconfigV1.ProjectsPatchJobsService, self).__init__(client)
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
        flat_path='v1/projects/{projectsId}/patchJobs/{patchJobsId}:cancel',
        http_method='POST',
        method_id='osconfig.projects.patchJobs.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelPatchJobRequest',
        request_type_name='OsconfigProjectsPatchJobsCancelRequest',
        response_type_name='PatchJob',
        supports_download=False,
    )

    def Execute(self, request, global_params=None):
      r"""Patch VM instances by creating and running a patch job.

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
        flat_path='v1/projects/{projectsId}/patchJobs:execute',
        http_method='POST',
        method_id='osconfig.projects.patchJobs.execute',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/patchJobs:execute',
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
        flat_path='v1/projects/{projectsId}/patchJobs/{patchJobsId}',
        http_method='GET',
        method_id='osconfig.projects.patchJobs.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='OsconfigProjectsPatchJobsGetRequest',
        response_type_name='PatchJob',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Get a list of patch jobs.

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
        flat_path='v1/projects/{projectsId}/patchJobs',
        http_method='GET',
        method_id='osconfig.projects.patchJobs.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/patchJobs',
        request_field='',
        request_type_name='OsconfigProjectsPatchJobsListRequest',
        response_type_name='ListPatchJobsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(OsconfigV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
