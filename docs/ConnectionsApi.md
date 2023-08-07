# authress.ConnectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connection**](ConnectionsApi.md#create_connection) | **POST** /v1/connections | Create SSO connection
[**delete_connection**](ConnectionsApi.md#delete_connection) | **DELETE** /v1/connections/{connectionId} | Delete SSO connection
[**get_connection**](ConnectionsApi.md#get_connection) | **GET** /v1/connections/{connectionId} | Retrieve SSO connection
[**get_connection_credentials**](ConnectionsApi.md#get_connection_credentials) | **GET** /v1/connections/{connectionId}/users/{userId}/credentials | Retrieve user connection credentials
[**get_connections**](ConnectionsApi.md#get_connections) | **GET** /v1/connections | List SSO connections
[**update_connection**](ConnectionsApi.md#update_connection) | **PUT** /v1/connections/{connectionId} | Update SSO connection


# **create_connection**
> Connection create_connection(connection)

Create SSO connection

Specify identity connection details for Authress identity aggregation.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.connection import Connection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

connection = authress.Connection() # Connection |

try:
    # Create SSO connection
    api_response = authress_client.connections.create_connection(connection)
    print("The response of ConnectionsApi->create_connection:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConnectionsApi->create_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection** | [**Connection**](Connection.md)|  |

### Return type

[**Connection**](Connection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. Connection created |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to create connection. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connection**
> delete_connection(connection_id)

Delete SSO connection

Delete an identity connection details for Authress identity aggregation.

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

connection_id = 'connection_id_example' # str | The connection identifier.

try:
    # Delete SSO connection
    authress_client.connections.delete_connection(connection_id)
except Exception as e:
    print("Exception when calling ConnectionsApi->delete_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The connection identifier. |

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
**204** | Success. Connection deleted |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete connection. |  -  |
**404** | Not found. The connection does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection**
> Connection get_connection(connection_id)

Retrieve SSO connection

Get the identity connection details for Authress identity aggregation.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.connection import Connection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

connection_id = 'connection_id_example' # str | The connection identifier.

try:
    # Retrieve SSO connection
    api_response = authress_client.connections.get_connection(connection_id)
    print("The response of ConnectionsApi->get_connection:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConnectionsApi->get_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The connection identifier. |

### Return type

[**Connection**](Connection.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to get connection. |  -  |
**404** | Not found. The connection does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connection_credentials**
> UserConnectionCredentials get_connection_credentials(connection_id, user_id)

Retrieve user connection credentials

Get the credentials for the user that were generated as part of the latest user login flow. Returns an access token that can be used with originating connection provider, based on the original scopes and approved permissions by that service.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.user_connection_credentials import UserConnectionCredentials

from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

connection_id = 'connection_id_example' # str | The connection identifier.
user_id = "user_id" # str | The connection user.

try:
    # Retrieve user connection credentials
    api_response = authress_client.connections.get_connection_credentials(connection_id, user_id)
    print("The response of ConnectionsApi->get_connection_credentials:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConnectionsApi->get_connection_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The connection identifier. |
 **user_id** | **str**| The connection user. |

### Return type

[**UserConnectionCredentials**](UserConnectionCredentials.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to get user connection credentials. |  -  |
**404** | Not found. The connection or user does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connections**
> ConnectionCollection get_connections()

List SSO connections

Returns a paginated connection list for the account. Only connections the user has access to are returned.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.connection_collection import ConnectionCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

try:
    # List SSO connections
    api_response = authress_client.connections.get_connections()
    print("The response of ConnectionsApi->get_connections:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConnectionsApi->get_connections: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectionCollection**](ConnectionCollection.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to fetch account connections, but has other account permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connection**
> Connection update_connection(connection_id, connection)

Update SSO connection

Specify identity connection details for Authress identity aggregation.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.connection import Connection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

connection_id = 'connection_id_example' # str | The connection identifier.
connection = authress.Connection() # Connection |

try:
    # Update SSO connection
    api_response = authress_client.connections.update_connection(connection_id, connection)
    print("The response of ConnectionsApi->update_connection:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ConnectionsApi->update_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The connection identifier. |
 **connection** | [**Connection**](Connection.md)|  |

### Return type

[**Connection**](Connection.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Connection updated |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to update connection. |  -  |
**404** | Not found. The connection does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

