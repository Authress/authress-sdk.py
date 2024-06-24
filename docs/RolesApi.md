# authress.RolesApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /v1/roles | Create role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /v1/roles/{roleId} | Delete role
[**get_role**](RolesApi.md#get_role) | **GET** /v1/roles/{roleId} | Retrieve role
[**get_roles**](RolesApi.md#get_roles) | **GET** /v1/roles | List roles
[**update_role**](RolesApi.md#update_role) | **PUT** /v1/roles/{roleId} | Update role


# **create_role**
> Role create_role(role)

Create role

Creates a role with permissions.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.role import Role
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.yourdomain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

role = authress.Role() # Role |

try:
    # Create role
    api_response = authress_client.roles.create_role(role)
    print("The response of RolesApi->create_role:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RolesApi->create_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. Role created. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn't have permission to the role, but they have other permissions to the same account. |  -  |
**409** | RoleAlreadyExists. A role with this identifier already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role_id)

Delete role

Remove a role. If a record references the role, that record will not be modified.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.yourdomain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

role_id = 'role_id_example' # str | The identifier of the role.

try:
    # Deletes role
    authress_client.roles.delete_role(role_id)
except Exception as e:
    print("Exception when calling RolesApi->delete_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The identifier of the role. | 

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
**204** | Success. The role has been deleted |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn't have permission to delete the role. |  -  |
**404** | Not found. The user doesn't have any permissions to the resource or the role no longer exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> Role get_role(role_id)

Retrieve role

Roles contain a list of permissions that will be applied to any user or resource

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.role import Role
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.yourdomain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

role_id = 'role_id_example' # str | The identifier of the role.

try:
    # Retrieve role
    api_response = authress_client.roles.get_role(role_id)
    print("The response of RolesApi->get_role:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The identifier of the role. | 

### Return type

[**Role**](Role.md)

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
**403** | Forbidden. The user doesn't have permission to the role, but they have other permissions to the same account. |  -  |
**404** | Not found. The user doesn't have any permissions to the role or this role does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> RoleCollection get_roles(limit=limit, cursor=cursor, filter=filter)

List roles

Get all the account roles. Roles contain a list of permissions that will be applied to any user or resource

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.role_collection import RoleCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.yourdomain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)


try:
    # List roles
    api_response = authress_client.roles.get_roles()
    print("The response of RolesApi->get_roles:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RolesApi->get_roles: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return. | [optional] [default to 100]
 **cursor** | **str**| Continuation cursor for paging. | [optional] 
 **filter** | **str**| Filter to search roles by. This is a case insensitive search. | [optional] 

### Return type

[**RoleCollection**](RoleCollection.md)

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
**403** | Forbidden. The user doesn't have permission to account roles, but they have other permissions to the same account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> Role update_role(role_id, role)

Update role

Updates a role adding or removing permissions.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.role import Role
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.yourdomain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

role_id = 'role_id_example' # str | The identifier of the role.
role = authress.Role() # Role |

try:
    # Update role
    api_response = authress_client.roles.update_role(role_id, role)
    print("The response of RolesApi->update_role:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling RolesApi->update_role: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| The identifier of the role. | 
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Role updated. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn't have permission to the role, but they have other permissions to the same account. |  -  |
**404** | Not found. The user doesn't have any permissions to the role or this role does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

