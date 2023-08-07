# authress.InvitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invite**](InvitesApi.md#create_invite) | **POST** /v1/invites | Create user invite
[**delete_invite**](InvitesApi.md#delete_invite) | **DELETE** /v1/invites/{inviteId} | Delete invite
[**get_invite**](InvitesApi.md#get_invite) | **GET** /v1/invites/{inviteId} | Retrieve invite
[**respond_to_invite**](InvitesApi.md#respond_to_invite) | **PATCH** /v1/invites/{inviteId} | Accept invite


# **create_invite**
> Invite create_invite(invite)

Create user invite

Invites are used to easily assign permissions to users that have not been created in your identity provider yet. 1. This generates an invite record. 2. Send the invite ID to the user. 3. Log the user in. 4. As the user PATCH the /invite/{inviteId} endpoint 5. This accepts the invite.         When the user accepts the invite they will automatically receive the permissions assigned in the Invite. Invites automatically expire after 7 days.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.invite import Invite
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

invite = authress.Invite() # Invite |

try:
    # Create user invite
    api_response = authress_client.invites.create_invite(invite)
    print("The response of InvitesApi->create_invite:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling InvitesApi->create_invite: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite** | [**Invite**](Invite.md)|  |

### Return type

[**Invite**](Invite.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. Invite created |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have the permissions to create an invite. They may have specified too many permissions in the invite. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_invite**
> delete_invite(invite_id)

Delete invite

Deletes an invite.

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

invite_id = 'invite_id_example' # str | The identifier of the invite.

try:
    # Delete invite
    authress_client.invites.delete_invite(invite_id)
except Exception as e:
    print("Exception when calling InvitesApi->delete_invite: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**| The identifier of the invite. |

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
**204** | Success. Invite deleted. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete the invite. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the invite. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite**
> Invite get_invite(invite_id)

Retrieve invite

Gets the invite along with the relevant invite data. Invites enable users inviting other users to their tenant, organization, or account.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.invite import Invite
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

invite_id = 'invite_id_example' # str | The identifier of the invite.

try:
    # Retrieve invite
    api_response = authress_client.invites.get_invite(invite_id)
    print("The response of InvitesApi->get_invite:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling InvitesApi->get_invite: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**| The identifier of the invite. |

### Return type

[**Invite**](Invite.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to this invite, but they have other permissions to the same account. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the invite or the invite does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_to_invite**
> Account respond_to_invite(invite_id)

Accept invite

Accepts an invite by claiming this invite by this user. The user access token used for this request will gain the permissions associated with the invite.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.account import Account
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

invite_id = 'invite_id_example' # str | The identifier of the invite.

try:
    # Accept invite
    api_response = authress_client.invites.respond_to_invite(invite_id)
    print("The response of InvitesApi->respond_to_invite:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling InvitesApi->respond_to_invite: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_id** | **str**| The identifier of the invite. |

### Return type

[**Account**](Account.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Invite accepted. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to update the access record. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the access record. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

