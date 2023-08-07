# Tenant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  |
**tenant_lookup_identifier** | **str** |  | [optional]
**data** | [**TenantData**](TenantData.md) |  | [optional]
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
tenant_form_dict = tenant.from_dict(tenant_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


