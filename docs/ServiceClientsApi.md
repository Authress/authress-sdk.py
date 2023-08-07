# authress.ServiceClientsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_client**](ServiceClientsApi.md#create_client) | **POST** /v1/clients | Create service client
[**delete_access_key**](ServiceClientsApi.md#delete_access_key) | **DELETE** /v1/clients/{clientId}/access-keys/{keyId} | Delete service client access key
[**delete_client**](ServiceClientsApi.md#delete_client) | **DELETE** /v1/clients/{clientId} | Delete service client
[**get_client**](ServiceClientsApi.md#get_client) | **GET** /v1/clients/{clientId} | Retrieve service client
[**get_clients**](ServiceClientsApi.md#get_clients) | **GET** /v1/clients | List service clients
[**request_access_key**](ServiceClientsApi.md#request_access_key) | **POST** /v1/clients/{clientId}/access-keys | Generate service client access key
[**update_client**](ServiceClientsApi.md#update_client) | **PUT** /v1/clients/{clientId} | Update service client


# **create_client**
> Client create_client(client)

Create service client

Creates a service client to interact with Authress or any other service on behalf of users. Each client has secret private keys used to authenticate with Authress. To use service clients created through other mechanisms, skip creating a client and create access records with the client identifier.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.client import Client
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

client = authress.Client() # Client |

try:
    # Create service client
    api_response = authress_client.service_clients.create_client(client)
    print("The response of ServiceClientsApi->create_client:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceClientsApi->create_client: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**Client**](Client.md)|  |

### Return type

[**Client**](Client.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_key**
> delete_access_key(client_id, key_id)

Delete service client access key

Deletes an access key for a client prevent it from being used to authenticate with Authress.

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

client_id = 'client_id_example' # str | The unique identifier of the client.
key_id = 'key_id_example' # str | The ID of the access key to remove from the client.

try:
    # Delete service client access key
    authress_client.service_clients.delete_access_key(client_id, key_id)
except Exception as e:
    print("Exception when calling ServiceClientsApi->delete_access_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The unique identifier of the client. |
 **key_id** | **str**| The ID of the access key to remove from the client. |

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
**204** | Success. The access key has been deleted. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete access keys from a client. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to the client or the client does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(client_id)

Delete service client

This deletes the service client.

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

client_id = 'client_id_example' # str | The unique identifier for the client.

try:
    # Delete service client
    authress_client.service_clients.delete_client(client_id)
except Exception as e:
    print("Exception when calling ServiceClientsApi->delete_client: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The unique identifier for the client. |

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
**204** | Success. The client was deleted. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete the client. |  -  |
**404** | Not found. The user doesn&#39;t have any permission to the client or the client does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client**
> Client get_client(client_id)

Retrieve service client

Returns all information related to client except for the private access keys.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.client import Client
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

client_id = 'client_id_example' # str | The unique identifier for the client.

try:
    # Retrieve service client
    api_response = authress_client.service_clients.get_client(client_id)
    print("The response of ServiceClientsApi->get_client:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceClientsApi->get_client: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The unique identifier for the client. |

### Return type

[**Client**](Client.md)

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
**404** | Not found. The user doesn&#39;t have permissions to the client or the client does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients**
> ClientCollection get_clients(limit=limit, cursor=cursor)

List service clients

Returns all clients that the user has access to in the account.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.client_collection import ClientCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

limit = 20 # int | Max number of results to return (optional) (default to 20)
cursor = 'cursor_example' # str | Continuation cursor for paging. (optional)

try:
    # List service clients
    api_response = authress_client.service_clients.get_clients(limit=limit, cursor=cursor)
    print("The response of ServiceClientsApi->get_clients:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceClientsApi->get_clients: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of results to return | [optional] [default to 20]
 **cursor** | **str**| Continuation cursor for paging. | [optional]

### Return type

[**ClientCollection**](ClientCollection.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to the resource, but they have other permissions to the same resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_access_key**
> ClientAccessKey request_access_key(client_id)

Generate service client access key

Create a new access key for the client so that a service can authenticate with Authress as that client. Using the client will allow delegation of permission checking of users. (Limited to 5 Active keys per client)

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.client_access_key import ClientAccessKey
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

client_id = 'client_id_example' # str | The unique identifier of the client.

try:
    # Generate service client access key
    api_response = authress_client.service_clients.request_access_key(client_id)
    print("The response of ServiceClientsApi->request_access_key:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceClientsApi->request_access_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The unique identifier of the client. |

### Return type

[**ClientAccessKey**](ClientAccessKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to create access keys for the client. |  -  |
**404** | Not found. The user doesn&#39;t have any permissions to client or the client does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> Client update_client(client_id, client)

Update service client

Updates a client information.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.client import Client
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

client_id = 'client_id_example' # str | The unique identifier for the client.
client = authress.Client() # Client |

try:
    # Update service client
    api_response = authress_client.service_clients.update_client(client_id, client)
    print("The response of ServiceClientsApi->update_client:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ServiceClientsApi->update_client: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The unique identifier for the client. |
 **client** | [**Client**](Client.md)|  |

### Return type

[**Client**](Client.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The client was updated |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to update the client. |  -  |
**404** | Not found. The user doesn&#39;t have permission to the account or the client does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

