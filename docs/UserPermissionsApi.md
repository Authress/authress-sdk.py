# authress.UserPermissionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_user**](UserPermissionsApi.md#authorize_user) | **GET** /v1/users/{userId}/resources/{resourceUri}/permissions/{permission} | Verify user authorization
[**get_user_permissions_for_resource**](UserPermissionsApi.md#get_user_permissions_for_resource) | **GET** /v1/users/{userId}/resources/{resourceUri}/permissions | Get user permissions for resource
[**get_user_resources**](UserPermissionsApi.md#get_user_resources) | **GET** /v1/users/{userId}/resources | List user resources
[**get_user_roles_for_resource**](UserPermissionsApi.md#get_user_roles_for_resource) | **GET** /v1/users/{userId}/resources/{resourceUri}/roles | Get user roles for resource


# **authorize_user**
> authorize_user(user_id, resource_uri, permission)

Verify user authorization

Performs the user authorization check. Does the user have the specified permission to the resource?

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress


from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

    user_id = "user_id" # str | The user to check permissions on
    resource_uri = '/organizations/org_a/documents/doc_1' # str | The uri path of a resource to validate, must be URL encoded, uri segments are allowed, the resource must be a full path.
    permission = "action" # str | Permission to check, '*' and scoped permissions can also be checked here.

    try:
        # Verify user authorization
        authress_client.user_permissions.authorize_user(user_id, resource_uri, permission)
    except Exception as e:
        print("Exception when calling UserPermissionsApi->authorize_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user to check permissions on |
 **resource_uri** | **str**| The uri path of a resource to validate, must be URL encoded, uri segments are allowed, the resource must be a full path. |
 **permission** | **str** | Permission to check, &#39;*&#39; and scoped permissions can also be checked here. |

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The user has permissions |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The requestor of the authorization check doesn&#39;t have the required permission to check the user&#39;s authorization. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the resource including the one requested. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_permissions_for_resource**
> PermissionCollection get_user_permissions_for_resource(user_id, resource_uri)

Get user permissions for resource

Get a summary of the permissions a user has to a particular resource.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.permission_collection import PermissionCollection

from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

    user_id = "user_id" # str | The user to check permissions on
    resource_uri = '/organizations/org_a/documents/doc_1' # str | The uri path of a resource to validate, must be URL encoded, uri segments are allowed.

    try:
        # Get user permissions for resource
        api_response = authress_client.user_permissions.get_user_permissions_for_resource(user_id, resource_uri)
        print("The response of UserPermissionsApi->get_user_permissions_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserPermissionsApi->get_user_permissions_for_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user to check permissions on |
 **resource_uri** | **str**| The uri path of a resource to validate, must be URL encoded, uri segments are allowed. |

### Return type

[**PermissionCollection**](PermissionCollection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The user has permissions |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_resources**
> UserResourcesCollection get_user_resources(user_id, resource_uri=resource_uri, collection_configuration=collection_configuration, permissions=permissions, limit=limit, cursor=cursor)

List user resources

Get the users resources. This result is a list of resource uris that a user has an permission to. By default only the top level matching resources are returned. To get a user's list of deeply nested resources, set the `collectionConfiguration` to be `INCLUDE_NESTED`. This collection is paginated.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress


from authress.models.user_resources_collection import UserResourcesCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

user_id = "user_id" # str | The user to check permissions on
resource_uri = '/organizations' # str | The top level uri path of a resource to query for. Will only match explicit or nested sub-resources. Will not partial match resource names. (optional)
collection_configuration = 'TOP_LEVEL_ONLY' # str | `TOP_LEVEL_ONLY` - returns only directly nested resources under the resourceUri. A query to `resourceUri=Collection` will return `Collection/resource_1`.<br>`INCLUDE_NESTED` - will return all sub-resources as well as deeply nested resources that the user has the specified permission to. A query to `resourceUri=Collection` will return `Collection/namespaces/ns/resources/resource_1`.<br><br>To return matching resources for nested resources, set this parameter to `INCLUDE_NESTED`. (optional) (default to 'TOP_LEVEL_ONLY')
permissions = "action" # str | Permission to check, '*' and scoped permissions can also be checked here. By default if the user has any permission explicitly to a resource, it will be included in the list. (optional)
limit = 20 # int | Max number of results to return (optional) (default to 20)
cursor = 'cursor_example' # str | Continuation cursor for paging (optional)

try:
    # List user resources
    api_response = authress_client.user_permissions.get_user_resources(user_id, resource_uri=resource_uri, collection_configuration=collection_configuration, permissions=permissions, limit=limit, cursor=cursor)
    print("The response of UserPermissionsApi->get_user_resources:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling UserPermissionsApi->get_user_resources: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user to check permissions on |
 **resource_uri** | **str**| The top level uri path of a resource to query for. Will only match explicit or nested sub-resources. Will not partial match resource names. | [optional]
 **collection_configuration** | **str**| &#x60;TOP_LEVEL_ONLY&#x60; - returns only directly nested resources under the resourceUri. A query to &#x60;resourceUri&#x3D;Collection&#x60; will return &#x60;Collection/resource_1&#x60;.&lt;br&gt;&#x60;INCLUDE_NESTED&#x60; - will return all sub-resources as well as deeply nested resources that the user has the specified permission to. A query to &#x60;resourceUri&#x3D;Collection&#x60; will return &#x60;Collection/namespaces/ns/resources/resource_1&#x60;.&lt;br&gt;&lt;br&gt;To return matching resources for nested resources, set this parameter to &#x60;INCLUDE_NESTED&#x60;. | [optional] [default to &#39;TOP_LEVEL_ONLY&#39;]
 **permissions** | **str**| Permission to check, &#39;*&#39; and scoped permissions can also be checked here. By default if the user has any permission explicitly to a resource, it will be included in the list. | [optional]
 **limit** | **int**| Max number of results to return | [optional] [default to 20]
 **cursor** | **str**| Continuation cursor for paging | [optional]

### Return type

[**UserResourcesCollection**](UserResourcesCollection.md)

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

# **get_user_roles_for_resource**
> UserRoleCollection get_user_roles_for_resource(user_id, resource_uri)

Get user roles for resource

Get a summary of the roles a user has to a particular resource. Users can be assigned roles from multiple access records, this may cause the same role to appear in the list more than once.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress

from authress.models.user_role_collection import UserRoleCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

user_id = "user_id" # str | The user to get roles for.
resource_uri = '/organizations/org_a/documents/doc_1' # str | The uri path of a resource to get roles for, must be URL encoded. Checks for explicit resource roles, roles attached to parent resources are not returned.

try:
    # Get user roles for resource
    api_response = authress_client.user_permissions.get_user_roles_for_resource(user_id, resource_uri)
    print("The response of UserPermissionsApi->get_user_roles_for_resource:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling UserPermissionsApi->get_user_roles_for_resource: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user to get roles for. |
 **resource_uri** | **str**| The uri path of a resource to get roles for, must be URL encoded. Checks for explicit resource roles, roles attached to parent resources are not returned. |

### Return type

[**UserRoleCollection**](UserRoleCollection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The user has roles |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

