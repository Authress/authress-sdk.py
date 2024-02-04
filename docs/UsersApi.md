# authress.UsersApi
Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /v1/users/{userId} | Delete a user
[**get_user**](UsersApi.md#get_user) | **GET** /v1/users/{userId} | Retrieve a user
[**get_users**](UsersApi.md#get_users) | **GET** /v1/users | List users


# **delete_user**
> delete_user(user_id)

Delete a user

Removes the user, all access the user has been granted through Authress access records, and any related user data. This action is completed asynchronously.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress

from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.company.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

user_id = "user_id" # str | The user identifier.

try:
    # Delete a user
    authress_client.users.delete_user(user_id)
except Exception as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user identifier. |

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
**202** | Success. User will be deleted. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete users. |  -  |
**404** | Not found. The user does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserIdentity get_user(user_id)

Retrieve a user

Get the user data associated with a user. The data returned by this endpoint is highly variable based on the source OAuth provider. Avoid depending on undocumented properties.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress

from authress.models.user_identity import UserIdentity
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.company.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

user_id = "user_id" # str | The user identifier.

try:
    # Retrieve a user
    api_response = authress_client.users.get_user(user_id)
    print("The response of UsersApi->get_user:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The user identifier. |

### Return type

[**UserIdentity**](UserIdentity.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to get user data. |  -  |
**404** | Not found. The user does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> UserIdentityCollection get_users(limit=limit, cursor=cursor, filter=filter, tenant_id=tenant_id)

List users

Returns a paginated user list for the account. The data returned by this endpoint is highly variable based on the source OAuth provider. Avoid depending on undocumented properties.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress

from authress.models.user_identity_collection import UserIdentityCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.company.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

limit = 100 # int | Max number of results to return (optional) (default to 100)
cursor = 'cursor_example' # str | Continuation cursor for paging (optional)
filter = 'filter_example' # str | Filter to search users by. This is a case insensitive search through every text field. (optional)
tenant_id = "tenant_id" # str | Return only users that are part of the specified tenant. Users can only be part of one tenant, using this parameter will limit returned users that have logged into this tenant. (optional)

try:
    # List users
    api_response = authress_client.users.get_users(limit=limit, cursor=cursor, filter=filter, tenant_id=tenant_id)
    print("The response of UsersApi->get_users:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return | [optional] [default to 100]
 **cursor** | **str**| Continuation cursor for paging | [optional]
 **filter** | **str**| Filter to search users by. This is a case insensitive search through every text field. | [optional]
 **tenant_id** | **str**| Return only users that are part of the specified tenant. Users can only be part of one tenant, using this parameter will limit returned users that have logged into this tenant. | [optional]

### Return type

[**UserIdentityCollection**](UserIdentityCollection.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to fetch users for the specified, but has other account permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

