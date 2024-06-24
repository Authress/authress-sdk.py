# authress.ApplicationsApi


Method | HTTP request | Description
------------- | ------------- | -------------
[**delegate_user_login**](ApplicationsApi.md#delegate_user_login) | **POST** /v1/applications/{applicationId}/users/{userId}/delegation | Log user into third-party application


# **delegate_user_login**
> ApplicationDelegation delegate_user_login(application_id, user_id)

Log user into third-party application

Redirect the user to an external application to login them in. Use this endpoint when you want to enable a user in your platform, identified by an Authress User ID, to log into a third party external application you do not control. The user will then be logged into that platform. Authress uses OpenID and SAML configuration to securely pass the user's login session in your platform to an external platform.<br><br>For first party applications, use the Authress Login SDK. First party applications are those that your team, org, and company own, operate, and run (even if they are open source solutions). Third party applications are those that are operated by another company on a separate eTLD and you have no control over.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.application_delegation import ApplicationDelegation
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://authress.yourdomain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

application_id = 'application_id_example' # str | The application to have the user log into.
user_id = 'user_id' # str | The user.

try:
    # Log user into third-party application
    api_response = authress_client.applications.delegate_user_login(application_id, user_id)
    print("The response of ApplicationsApi->delegate_user_login:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling ApplicationsApi->delegate_user_login: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The third party application, the users wants to login using their Authress User Identity. Application IDs begin with app_. | 
 **user_id** | **str**| The Authress user identifier. | 

### Return type

[**ApplicationDelegation**](ApplicationDelegation.md)

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
**403** | Forbidden. The user doesn't have permission to log a user into this application. |  -  |
**404** | Not found. The application or user does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

