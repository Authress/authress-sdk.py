# authress.AccountsApi
Method | HTTP request | Description
------------- | ------------- | -------------
[**delegate_authentication**](AccountsApi.md#delegate_authentication) | **POST** /v1/identities | Link external provider
[**get_account**](AccountsApi.md#get_account) | **GET** /v1/accounts/{accountId} | Retrieve account information
[**get_account_identities**](AccountsApi.md#get_account_identities) | **GET** /v1/identities | List linked external providers
[**get_accounts**](AccountsApi.md#get_accounts) | **GET** /v1/accounts | List user Authress accounts


# **delegate_authentication**
> delegate_authentication(identity_request)

Link external provider

An identity is a JWT subscriber *sub* and issuer *iss*. Only one account my be linked to a particular JWT combination. Allows calling the API with a federated token directly instead of using a client access key.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.identity_request import IdentityRequest
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)
# Create an instance of the API class
identity_request = authress_client.access_recordsIdentityRequest() # IdentityRequest |

try:
    # Link external provider
    authress_client.access_records.delegate_authentication(identity_request)
except Exception as e:
    print("Exception when calling AccountsApi->delegate_authentication: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_request** | [**IdentityRequest**](IdentityRequest.md)|  |

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
**201** | Success. New identity linked. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to update identities for the account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account**
> Account get_account(account_id)

Retrieve account information

Includes the original configuration information.

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
account_id = 'account_id_example' # str | The unique identifier for the account

try:
    # Retrieve account information
    api_response = authress_client.access_records.get_account(account_id)
    print("The response of AccountsApi->get_account:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AccountsApi->get_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| The unique identifier for the account |

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
**200** | Success. The account |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to this account or it does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_identities**
> IdentityCollection get_account_identities()

List linked external providers

Returns a list of identities linked for this account.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.identity_collection import IdentityCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

try:
    # List linked external providers
    api_response = authress_client.access_records.get_account_identities()
    print("The response of AccountsApi->get_account_identities:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AccountsApi->get_account_identities: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityCollection**](IdentityCollection.md)

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
**403** | Not found. The user doesn&#39;t have permission to list identities for this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> AccountCollection get_accounts(earliest_cache_time=earliest_cache_time)

List user Authress accounts

Returns a list of accounts that the user has access to.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.account_collection import AccountCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

earliest_cache_time = '2013-10-20T19:20:30+01:00' # datetime | Ensure the accounts list is not cached before this time. (optional)

try:
    # List user Authress accounts
    api_response = authress_client.access_records.get_accounts(earliest_cache_time=earliest_cache_time)
    print("The response of AccountsApi->get_accounts:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling AccountsApi->get_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **earliest_cache_time** | **datetime**| Ensure the accounts list is not cached before this time. | [optional]

### Return type

[**AccountCollection**](AccountCollection.md)

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

