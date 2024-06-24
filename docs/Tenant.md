# Tenant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**tenant_lookup_identifier** | **str** |  | [optional] 
**data** | [**TenantData**](TenantData.md) |  | [optional] 
**domains** | [**List[TenantDomain]**](TenantDomain.md) | The associated user email domains that are mapped to this tenant. When a user starts the authentication process, if they are using SSO, Authress will use their specified email address to identify which Authress Tenant to log the user in with. | [optional] 
**connection** | [**TenantConnection**](TenantConnection.md) |  | [optional] 
**created_time** | **datetime** |  | [optional] [readonly] 

## Example

```python
from authress.models.tenant import Tenant

# TODO update the JSON string below
json = "{}"
# create an instance of Tenant from a JSON string
tenant_instance = Tenant.from_json(json)
# print the JSON string representation of the object
print Tenant.to_json()

# convert the object into a dict
tenant_dict = tenant_instance.to_dict()
# create an instance of Tenant from a dict
tenant_from_dict = Tenant.from_dict(tenant_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


