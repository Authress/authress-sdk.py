# authress.ResourcePermissionsApi
Method | HTTP request | Description
------------- | ------------- | -------------
[**get_permissioned_resource**](ResourcePermissionsApi.md#get_permissioned_resource) | **GET** /v1/resources/{resourceUri} | Retrieve resource configuration
[**get_permissioned_resources**](ResourcePermissionsApi.md#get_permissioned_resources) | **GET** /v1/resources | List all resource configurations
[**get_resource_users**](ResourcePermissionsApi.md#get_resource_users) | **GET** /v1/resources/{resourceUri}/users | List users with resource access
[**update_permissioned_resource**](ResourcePermissionsApi.md#update_permissioned_resource) | **PUT** /v1/resources/{resourceUri} | Update resource configuration


# **get_permissioned_resource**
> PermissionedResource get_permissioned_resource(resource_uri)

Retrieve resource configuration

Permissions can be set globally at a resource level. This will apply to all users in an account.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.permissioned_resource import PermissionedResource
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.company.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

resource_uri = '/organizations/org_a/documents/doc_1' # str | The uri path of a resource to validate, must be URL encoded, uri segments are allowed.

try:
    # Retrieve resource configuration
    api_response = authress_client.resource_permissions.get_permissioned_resource(resource_uri)
    print("The response of ResourcePermissionsApi->get_permissioned_resource:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ResourcePermissionsApi->get_permissioned_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uri** | **str**| The uri path of a resource to validate, must be URL encoded, uri segments are allowed. |

### Return type

[**PermissionedResource**](PermissionedResource.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**404** | Not found. The user doesn&#39;t have permission to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissioned_resources**
> PermissionedResourceCollection get_permissioned_resources()

List all resource configurations

Permissions can be set globally at a resource level. Lists any resources with a globally set resource policy.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.permissioned_resource_collection import PermissionedResourceCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.company.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)


try:
    # List all resource configurations
    api_response = authress_client.resource_permissions.get_permissioned_resources()
    print("The response of ResourcePermissionsApi->get_permissioned_resources:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ResourcePermissionsApi->get_permissioned_resources: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PermissionedResourceCollection**](PermissionedResourceCollection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_users**
> ResourceUsersCollection get_resource_users(resource_uri, limit=limit, cursor=cursor)

List users with resource access

Get the resource users with explicit access to the resource. This result is a list of users that have some permission to the resource. Users with access to parent resources and users with access only to a sub-resource will not be returned in this result. In the case that the resource has multiple users, the list will be paginated.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.resource_users_collection import ResourceUsersCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.company.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

resource_uri = '/organizations/org_a/documents/doc_1' # str | The uri path of a resource to validate, must be URL encoded, uri segments are allowed.
limit = 20 # int | Max number of results to return (optional) (default to 20)
cursor = 'cursor_example' # str | Continuation cursor for paging (optional)

try:
    # List users with resource access
    api_response = authress_client.resource_permissions.get_resource_users(resource_uri, limit=limit, cursor=cursor)
    print("The response of ResourcePermissionsApi->get_resource_users:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ResourcePermissionsApi->get_resource_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uri** | **str**| The uri path of a resource to validate, must be URL encoded, uri segments are allowed. |
 **limit** | **int**| Max number of results to return | [optional] [default to 20]
 **cursor** | **str**| Continuation cursor for paging | [optional]

### Return type

[**ResourceUsersCollection**](ResourceUsersCollection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permissioned_resource**
> update_permissioned_resource(resource_uri, permissioned_resource)

Update resource configuration

Updates the global permissions on a resource. This applies to all users in an account.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.permissioned_resource import PermissionedResource
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.company.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

resource_uri = '/organizations/org_a/documents/doc_1' # str | The uri path of a resource to validate, must be URL encoded, uri segments are allowed.
permissioned_resource = authress.PermissionedResource() # PermissionedResource | The contents of the permission to set on the resource. Overwrites existing data.

try:
    # Update resource configuration
    authress_client.resource_permissions.update_permissioned_resource(resource_uri, permissioned_resource)
except Exception as e:
    print("Exception when calling ResourcePermissionsApi->update_permissioned_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_uri** | **str**| The uri path of a resource to validate, must be URL encoded, uri segments are allowed. |
 **permissioned_resource** | [**PermissionedResource**](PermissionedResource.md)| The contents of the permission to set on the resource. Overwrites existing data. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to the resource, but they have other permissions to the same resource. |  -  |
**404** | Not found. The user doesn&#39;t have permission to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

