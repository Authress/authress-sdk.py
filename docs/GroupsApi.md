# authress.GroupsApi
Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupsApi.md#create_group) | **POST** /v1/groups | Create group
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /v1/groups/{groupId} | Deletes group
[**get_group**](GroupsApi.md#get_group) | **GET** /v1/groups/{groupId} | Retrieve group
[**get_groups**](GroupsApi.md#get_groups) | **GET** /v1/groups | List groups
[**update_group**](GroupsApi.md#update_group) | **PUT** /v1/groups/{groupId} | Update a group


# **create_group**
> Group create_group(group)

Create group

Specify users to be included in a new group. (Groups have a maximum size of ~100KB)

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.group import Group
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

group = authress.Group() # Group |

try:
    # Create group
    api_response = authress_client.groups.create_group(group)
    print("The response of GroupsApi->create_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GroupsApi->create_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**Group**](Group.md)|  |

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. Group created |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to create groups. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Deletes group

Remove a group, users will lose any role that was assigned through membership of this group. This action cannot be undone.

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

group_id = "group_id" # str | The identifier of the group.

try:
    # Deletes group
    authress_client.groups.delete_group(group_id)
except Exception as e:
    print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of the group. |

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
**204** | Success. The group has been deleted |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete the group. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the resource or the group no longer exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(group_id)

Retrieve group

A group contains multiple users which can be added to an access record, and should be assigned the same roles at the same time.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.group import Group

from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

group_id = "group_id" # str | The identifier of the group.

try:
    # Retrieve group
    api_response = authress_client.groups.get_group(group_id)
    print("The response of GroupsApi->get_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GroupsApi->get_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of the group. |

### Return type

[**Group**](Group.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to the group, but they have other permissions to the same account. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the group or this group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> GroupCollection get_groups(limit=limit, cursor=cursor, filter=filter)

List groups

Returns a paginated groups list for the account. Only groups the user has access to are returned. This query resource is meant for administrative actions only, therefore has a lower rate limit tier than user permissions related resources.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.group_collection import GroupCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

limit = 20 # int | Max number of results to return (optional) (default to 20)
cursor = 'cursor_example' # str | Continuation cursor for paging (optional)
filter = 'filter_example' # str | Filter to search groups by. This is a case insensitive search through every text field. (optional)

try:
    # List groups
    api_response = authress_client.groups.get_groups(limit=limit, cursor=cursor, filter=filter)
    print("The response of GroupsApi->get_groups:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GroupsApi->get_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return | [optional] [default to 20]
 **cursor** | **str**| Continuation cursor for paging | [optional]
 **filter** | **str**| Filter to search groups by. This is a case insensitive search through every text field. | [optional]

### Return type

[**GroupCollection**](GroupCollection.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to fetch groups, but has other account permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> Group update_group(group_id, group)

Update a group

Updates a group adding or removing user. Change a group updates the permissions and roles the users have access to. (Groups have a maximum size of ~100KB)

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.group import Group

from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

group_id = "group_id" # str | The identifier of the group.
group = authress.Group() # Group |

try:
    # Update a group
    api_response = authress_client.groups.update_group(group_id, group)
    print("The response of GroupsApi->update_group:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling GroupsApi->update_group: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of the group. |
 **group** | [**Group**](Group.md)|  |

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Group updated. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to update the group. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

