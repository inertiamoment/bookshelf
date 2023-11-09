"""Generated client library for servicedirectory version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.servicedirectory.v1beta1 import servicedirectory_v1beta1_messages as messages


class ServicedirectoryV1beta1(base_api.BaseApiClient):
  """Generated client library for service servicedirectory version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://servicedirectory.googleapis.com/'
  MTLS_BASE_URL = 'https://servicedirectory.mtls.googleapis.com/'

  _PACKAGE = 'servicedirectory'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ServicedirectoryV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new servicedirectory handle."""
    url = url or self.BASE_URL
    super(ServicedirectoryV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_namespaces_services_endpoints = self.ProjectsLocationsNamespacesServicesEndpointsService(self)
    self.projects_locations_namespaces_services = self.ProjectsLocationsNamespacesServicesService(self)
    self.projects_locations_namespaces = self.ProjectsLocationsNamespacesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsNamespacesServicesEndpointsService(base_api.BaseApiService):
    """Service class for the projects_locations_namespaces_services_endpoints resource."""

    _NAME = 'projects_locations_namespaces_services_endpoints'

    def __init__(self, client):
      super(ServicedirectoryV1beta1.ProjectsLocationsNamespacesServicesEndpointsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates an endpoint, and returns the new endpoint.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesEndpointsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Endpoint) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}/endpoints',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.services.endpoints.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['endpointId'],
        relative_path='v1beta1/{+parent}/endpoints',
        request_field='endpoint',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesEndpointsCreateRequest',
        response_type_name='Endpoint',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an endpoint.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesEndpointsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}/endpoints/{endpointsId}',
        http_method='DELETE',
        method_id='servicedirectory.projects.locations.namespaces.services.endpoints.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesEndpointsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an endpoint.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesEndpointsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Endpoint) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}/endpoints/{endpointsId}',
        http_method='GET',
        method_id='servicedirectory.projects.locations.namespaces.services.endpoints.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesEndpointsGetRequest',
        response_type_name='Endpoint',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all endpoints.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesEndpointsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListEndpointsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}/endpoints',
        http_method='GET',
        method_id='servicedirectory.projects.locations.namespaces.services.endpoints.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/endpoints',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesEndpointsListRequest',
        response_type_name='ListEndpointsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an endpoint.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesEndpointsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Endpoint) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}/endpoints/{endpointsId}',
        http_method='PATCH',
        method_id='servicedirectory.projects.locations.namespaces.services.endpoints.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta1/{+name}',
        request_field='endpoint',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesEndpointsPatchRequest',
        response_type_name='Endpoint',
        supports_download=False,
    )

  class ProjectsLocationsNamespacesServicesService(base_api.BaseApiService):
    """Service class for the projects_locations_namespaces_services resource."""

    _NAME = 'projects_locations_namespaces_services'

    def __init__(self, client):
      super(ServicedirectoryV1beta1.ProjectsLocationsNamespacesServicesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a service, and returns the new service.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.services.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['serviceId'],
        relative_path='v1beta1/{+parent}/services',
        request_field='service',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesCreateRequest',
        response_type_name='Service',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a service. This also deletes all endpoints associated with the service.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}',
        http_method='DELETE',
        method_id='servicedirectory.projects.locations.namespaces.services.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a service.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}',
        http_method='GET',
        method_id='servicedirectory.projects.locations.namespaces.services.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesGetRequest',
        response_type_name='Service',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the IAM Policy for a resource (namespace or service only).

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}:getIamPolicy',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.services.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:getIamPolicy',
        request_field='getIamPolicyRequest',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all services belonging to a namespace.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServicesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services',
        http_method='GET',
        method_id='servicedirectory.projects.locations.namespaces.services.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/services',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesListRequest',
        response_type_name='ListServicesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a service.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Service) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}',
        http_method='PATCH',
        method_id='servicedirectory.projects.locations.namespaces.services.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta1/{+name}',
        request_field='service',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesPatchRequest',
        response_type_name='Service',
        supports_download=False,
    )

    def Resolve(self, request, global_params=None):
      r"""Returns a service and its associated endpoints. Resolving a service is not considered an active developer method.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesResolveRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ResolveServiceResponse) The response message.
      """
      config = self.GetMethodConfig('Resolve')
      return self._RunMethod(
          config, request, global_params=global_params)

    Resolve.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}:resolve',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.services.resolve',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:resolve',
        request_field='resolveServiceRequest',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesResolveRequest',
        response_type_name='ResolveServiceResponse',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the IAM Policy for a resource (namespace or service only).

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}:setIamPolicy',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.services.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Tests IAM permissions for a resource (namespace or service only).

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesServicesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}/services/{servicesId}:testIamPermissions',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.services.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesServicesTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsNamespacesService(base_api.BaseApiService):
    """Service class for the projects_locations_namespaces resource."""

    _NAME = 'projects_locations_namespaces'

    def __init__(self, client):
      super(ServicedirectoryV1beta1.ProjectsLocationsNamespacesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a namespace, and returns the new namespace.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Namespace) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['namespaceId'],
        relative_path='v1beta1/{+parent}/namespaces',
        request_field='namespace',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesCreateRequest',
        response_type_name='Namespace',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a namespace. This also deletes all services and endpoints in the namespace.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}',
        http_method='DELETE',
        method_id='servicedirectory.projects.locations.namespaces.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a namespace.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Namespace) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}',
        http_method='GET',
        method_id='servicedirectory.projects.locations.namespaces.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesGetRequest',
        response_type_name='Namespace',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the IAM Policy for a resource (namespace or service only).

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}:getIamPolicy',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:getIamPolicy',
        request_field='getIamPolicyRequest',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all namespaces.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListNamespacesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces',
        http_method='GET',
        method_id='servicedirectory.projects.locations.namespaces.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/namespaces',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesListRequest',
        response_type_name='ListNamespacesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a namespace.

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Namespace) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}',
        http_method='PATCH',
        method_id='servicedirectory.projects.locations.namespaces.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta1/{+name}',
        request_field='namespace',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesPatchRequest',
        response_type_name='Namespace',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the IAM Policy for a resource (namespace or service only).

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}:setIamPolicy',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Tests IAM permissions for a resource (namespace or service only).

      Args:
        request: (ServicedirectoryProjectsLocationsNamespacesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/namespaces/{namespacesId}:testIamPermissions',
        http_method='POST',
        method_id='servicedirectory.projects.locations.namespaces.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='ServicedirectoryProjectsLocationsNamespacesTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(ServicedirectoryV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (ServicedirectoryProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='servicedirectory.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (ServicedirectoryProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='servicedirectory.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'includeUnrevealedLocations', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+name}/locations',
        request_field='',
        request_type_name='ServicedirectoryProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(ServicedirectoryV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }