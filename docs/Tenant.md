# Tenant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**tenant_lookup_identifier** | **str** |  | [optional] 
**data** | [**TenantData**](TenantData.md) |  | [optional] 
**domains** | [**List[TenantDomain]**](TenantDomain.md) | The associated user email domains that are mapped to this tenant. When a user starts the authentication process, if they are using SSO, Authress will use their specified email address to identify which Authress Tenant to log the user in with. | [optional] 
**connection** | [**TenantConnection**](TenantConnection.md) |  | [optional] 
**token_configuration** | [**AuthenticationTokenConfiguration**](AuthenticationTokenConfiguration.md) |  | [optional] 
**created_time** | **datetime** |  | [optional] [readonly] 

## Example

```python
from authress.models.tenant import Tenant

tenant = Tenant(
    tenant_id="Tenant_ID-001",
    tenant_lookup_identifier="example.com",
    data=TenantData(name="Tenant for Customer Example 001"),
    domains=[
        TenantDomain(domain="example.com"), TenantDomain(domain="alternate.example.com")
    ],
    connection=TenantConnection(
        connection_id="google"
    ),
    token_configuration = AuthenticationTokenConfiguration(
        access_token_duration="PT24H",
        session_duration="P30D"
    )
)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


