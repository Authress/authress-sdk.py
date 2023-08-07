# authress.ExtensionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extension**](ExtensionsApi.md#create_extension) | **POST** /v1/extensions | Create extension
[**delete_extension**](ExtensionsApi.md#delete_extension) | **DELETE** /v1/extensions/{extensionId} | Delete extension
[**get_extension**](ExtensionsApi.md#get_extension) | **GET** /v1/extensions/{extensionId} | Retrieve extension
[**get_extensions**](ExtensionsApi.md#get_extensions) | **GET** /v1/extensions | List extensions
[**login**](ExtensionsApi.md#login) | **GET** / | OAuth Authorize
[**request_token**](ExtensionsApi.md#request_token) | **POST** /api/authentication/oauth/tokens | OAuth Token
[**update_extension**](ExtensionsApi.md#update_extension) | **PUT** /v1/extensions/{extensionId} | Update extension


# **create_extension**
> Extension create_extension(extension)

Create extension

Specify the extension details for a new developer extension. Creating the extension enables developers to build applications that can log in to your platform and interact with your users' data.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.extension import Extension
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

extension = authress.Extension() # Extension |

try:
    # Create extension
    api_response = authress_client.extensions.create_extension(extension)
    print("The response of ExtensionsApi->create_extension:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ExtensionsApi->create_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | [**Extension**](Extension.md)|  |

### Return type

[**Extension**](Extension.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. Extension created |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to create extension. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_extension**
> delete_extension(extension_id)

Delete extension

Deletes the specified extension. When deleted an extension can no longer be accessed. Additionally users cannot use that extension to log in, nor can the service client associated with the extension be used to access data secured by Authress. The related Access Records will automatically be deleted.

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

extension_id = 'extension_id_example' # str | The extension identifier.

try:
    # Delete extension
    authress_client.extensions.delete_extension(extension_id)
except Exception as e:
    print("Exception when calling ExtensionsApi->delete_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension identifier. |

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
**204** | Success. Extension deleted. Completed disabling and deleting an extension is done asynchronously. |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete extension. |  -  |
**404** | Not found. The extension does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extension**
> Extension get_extension(extension_id)

Retrieve extension

Gets the platform extension details for the existing extension.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.extension import Extension
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

extension_id = 'extension_id_example' # str | The extension identifier.

try:
    # Retrieve extension
    api_response = authress_client.extensions.get_extension(extension_id)
    print("The response of ExtensionsApi->get_extension:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ExtensionsApi->get_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension identifier. |

### Return type

[**Extension**](Extension.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to get extension. |  -  |
**404** | Not found. The extension does not extension. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions**
> ExtensionCollection get_extensions()

List extensions

Lists the platform extensions. Extensions are the applications that developers of your platform have created for your users to interact with. Returns a paginated extension list for the account. Only extensions the user has access to are returned.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.extension_collection import ExtensionCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)


try:
    # List extensions
    api_response = authress_client.extensions.get_extensions()
    print("The response of ExtensionsApi->get_extensions:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ExtensionsApi->get_extensions: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ExtensionCollection**](ExtensionCollection.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to fetch account extensions, but has other account permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> OAuthAuthorizeResponse login(client_id, code_challenge, redirect_uri, code_challenge_method=code_challenge_method)

OAuth Authorize

*Note*: This endpoint is only to be used for [Authress Platform Extensions](https://authress.io/knowledge-base/docs/extensions/). If you are not building an app marketplace, then tokens can be directly requested for Service Clients, using the relevant [SDK](https://authress.io/app/#/api).<br><br>Start the OAuth login by redirecting the user to the OAuth Authorize endpoint. This generates a JWT for the user using the configured application, client ID, and connection.<br><br>The OAuth 2.1 authorization request that follows [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749). Enables users to request a JWT signed by Authress and Returns an OAuth JWT containing the relevant user claims. Tokens generated must be verified before usage by validating the `sub`, `iss`, and `aud` properties in the JWT. Please note, that the properties in the request and response use snake_case to explicitly follow the standard.<br><br>The ExtensionClient in the [@authress/login](https://github.com/Authress/authress-login.js#platform-extension-login) npm package provides all the necessary logic to make this easy.

### Example

```python
import time
import os
import authress
from authress.models.o_auth_authorize_response import OAuthAuthorizeResponse
from authress.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = authress.Configuration(
    host = "http://localhost"
)


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

client_id = 'ext_00AA' # str | The client identifier to constrain the token to.
code_challenge = '6fdkQaPm51l13DSukcAH3Mdx7_ntecHYd1vi3n0hMZY' # str | The PKCE Code challenge generated by the extension UI to secure the code exchange from [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636).
redirect_uri = 'https://extension.application.com/login-redirect' # str | The location to redirect the user back to after login. This redirect_uri must be a URL that matches one of the preconfigured urls in the Authress Application.
code_challenge_method = 'S256' # str | The method used to generate the code_challenge from the code_verifier. `code_challenge_method(code_verifier) = code_challenge` (optional) (default to 'S256')

try:
    # OAuth Authorize
    api_response = authress_client.extensions.login(client_id, code_challenge, redirect_uri, code_challenge_method=code_challenge_method)
    print("The response of ExtensionsApi->login:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ExtensionsApi->login: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client identifier to constrain the token to. |
 **code_challenge** | **str**| The PKCE Code challenge generated by the extension UI to secure the code exchange from [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636). |
 **redirect_uri** | **str**| The location to redirect the user back to after login. This redirect_uri must be a URL that matches one of the preconfigured urls in the Authress Application. |
 **code_challenge_method** | **str**| The method used to generate the code_challenge from the code_verifier. &#x60;code_challenge_method(code_verifier) &#x3D; code_challenge&#x60; | [optional] [default to &#39;S256&#39;]

### Return type

[**OAuthAuthorizeResponse**](OAuthAuthorizeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**400** | Bad Request. There are one or more issues with the request that prevent the service from returning a valid token |  -  |
**401** | Unauthorized. The credentials and temporary security token provided in the request is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_token**
> OAuthTokenResponse request_token(o_auth_token_request)

OAuth Token

*Note*: This endpoint is only to be used for [Authress Platform Extensions](https://authress.io/knowledge-base/docs/extensions/). If you are not building an app marketplace, then tokens can be directly requested for Service Clients, using the relevant [SDK](https://authress.io/app/#/api).<br><br>Request an OAuth JWT. Can either be called with service client credentials or as the second part of the user authorize login flow.<br>When using the `password` grant_type, service client authentication must be used via the Authress SDKs, and requires the `Authress:AuthenticateUser` role.<br><br>The OAuth 2.1 token request that follows [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749). Enables users to request a JWT signed by Authress, and returns an OAuth JWT containing the relevant user claims. Tokens generated must be verified before usage by validating the `sub`, `iss`, and `aud` properties in the JWT. Please note, that the properties in the request and response use snake_case to explicitly follow the standard.<br><br>The ExtensionClient in the [@authress/login](https://github.com/Authress/authress-login.js#platform-extension-login) npm package provides all the necessary logic to make this easy.

### Example

```python
import time
import os
import authress
from authress.models.o_auth_token_request import OAuthTokenRequest
from authress.models.o_auth_token_response import OAuthTokenResponse
from authress.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = authress.Configuration(
    host = "http://localhost"
)


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

o_auth_token_request = authress.OAuthTokenRequest() # OAuthTokenRequest | The contents of an OAuth token request.

try:
    # OAuth Token
    api_response = authress_client.extensions.request_token(o_auth_token_request)
    print("The response of ExtensionsApi->request_token:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ExtensionsApi->request_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_token_request** | [**OAuthTokenRequest**](OAuthTokenRequest.md)| The contents of an OAuth token request. |

### Return type

[**OAuthTokenResponse**](OAuthTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The credentials provided are valid and token has been created. |  -  |
**400** | Bad Request. There are one or more issues with the request that prevent the service from returning a valid token |  -  |
**401** | Unauthorized. The credentials and temporary security token provided in the request is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_extension**
> Extension update_extension(extension_id, extension)

Update extension

Specify the updated extension. The extension will be updated and these changes will be reflected to the access control and user authentication associated with the extension.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.extension import Extension
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

extension_id = 'extension_id_example' # str | The extension identifier.
extension = authress.Extension() # Extension |

try:
    # Update extension
    api_response = authress_client.extensions.update_extension(extension_id, extension)
    print("The response of ExtensionsApi->update_extension:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ExtensionsApi->update_extension: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| The extension identifier. |
 **extension** | [**Extension**](Extension.md)|  |

### Return type

[**Extension**](Extension.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. The extension has been successfully updated |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to update extension. |  -  |
**404** | Not found. The extension does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

