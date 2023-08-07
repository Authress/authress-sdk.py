# authress.TenantsApi
Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tenant**](TenantsApi.md#create_tenant) | **POST** /v1/tenants | Create tenant
[**delete_tenant**](TenantsApi.md#delete_tenant) | **DELETE** /v1/tenants/{tenantId} | Delete tenant
[**get_tenant**](TenantsApi.md#get_tenant) | **GET** /v1/tenants/{tenantId} | Retrieve tenant
[**get_tenants**](TenantsApi.md#get_tenants) | **GET** /v1/tenants | List tenants
[**update_tenant**](TenantsApi.md#update_tenant) | **PUT** /v1/tenants/{tenantId} | Update tenant


# **create_tenant**
> Tenant create_tenant(tenant)

Create tenant

Specify tenant identity details for tenant tracking, separation, and user management. Tenant identifiers are persisted to access tokens created by Authress.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.tenant import Tenant
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

tenant = authress.Tenant() # Tenant |

try:
    # Create tenant
    api_response = authress_client.tenants.create_tenant(tenant)
    print("The response of TenantsApi->create_tenant:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling TenantsApi->create_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant** | [**Tenant**](Tenant.md)|  |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success. Tenant created |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to create tenants. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant**
> delete_tenant(tenant_id)

Delete tenant

Delete a tenant. If a connection was created for the tenant then it is deleted as well.

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
tenant_id = "tenant_id" # str | The tenantId.

try:
    # Delete tenant
    authress_client.tenants.delete_tenant(tenant_id)
except Exception as e:
    print("Exception when calling TenantsApi->delete_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenantId. |

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
**204** | Success. Tenant deleted |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to delete tenant. |  -  |
**404** | Not found. The tenant does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> Tenant get_tenant(tenant_id)

Retrieve tenant

Get the tenant details for an Authress tenant.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.tenant import Tenant

from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

tenant_id = "tenant_id" # str | The tenantId.

try:
    # Retrieve tenant
    api_response = authress_client.tenants.get_tenant(tenant_id)
    print("The response of TenantsApi->get_tenant:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling TenantsApi->get_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenantId. |

### Return type

[**Tenant**](Tenant.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to get the tenant. |  -  |
**404** | Not found. The tenant does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenants**
> TenantCollection get_tenants()

List tenants

Returns a paginated tenants list for the account. Only tenants the user has access to are returned.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.tenant_collection import TenantCollection
from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

try:
    # List tenants
    api_response = authress_client.tenants.get_tenants()
    print("The response of TenantsApi->get_tenants:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling TenantsApi->get_tenants: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**TenantCollection**](TenantCollection.md)

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
**403** | Forbidden. The user doesn&#39;t have permission to fetch account tenants, but has other account permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant**
> Tenant update_tenant(tenant_id, tenant)

Update tenant

Updates the tenants information and linked tenant if it exists.

### Example

* Bearer (JWT) Authentication (oauth2):
```python
import time
import os
import authress
from authress.models.tenant import Tenant

from authress.rest import ApiException
from pprint import pprint


# Authress custom domain or if there isn't one yet, use the authress account specific url
authress_api_url = "https://login.your.domain.com" # or "https://ACCOUNT_ID.api.authress.io"

# The Service Client Access Key for your service client.
service_client_access_key = "sc_key_001"
authress_client = AuthressClient(authress_api_url=authress_api_url , service_client_access_key=service_client_access_key)

tenant_id = "tenant_id" # str | The tenantId.
tenant = authress.Tenant() # Tenant |

try:
    # Update tenant
    api_response = authress_client.tenants.update_tenant(tenant_id, tenant)
    print("The response of TenantsApi->update_tenant:\n")
    pprint(api_response)
except Exception as e:
    print("Exception when calling TenantsApi->update_tenant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| The tenantId. |
 **tenant** | [**Tenant**](Tenant.md)|  |

### Return type

[**Tenant**](Tenant.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/links+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. Tenant updated |  -  |
**401** | Unauthorized. The request JWT found in the Authorization header is no longer valid. |  -  |
**403** | Forbidden. The user doesn&#39;t have permission to update tenant. |  -  |
**404** | Not found. The tenant does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

