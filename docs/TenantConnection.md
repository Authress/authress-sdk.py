# TenantConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** |  | [optional] 

## Example

```python
from authress.models.tenant_connection import TenantConnection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantConnection from a JSON string
tenant_connection_instance = TenantConnection.from_json(json)
# print the JSON string representation of the object
print TenantConnection.to_json()

# convert the object into a dict
tenant_connection_dict = tenant_connection_instance.to_dict()
# create an instance of TenantConnection from a dict
tenant_connection_from_dict = TenantConnection.from_dict(tenant_connection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


