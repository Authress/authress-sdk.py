# TenantCollection

A collection of tenants.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenants** | [**List[Tenant]**](Tenant.md) |  |
**pagination** | [**Pagination**](Pagination.md) |  | [optional]

## Example

```python
from authress.models.tenant_collection import TenantCollection

# TODO update the JSON string below
json = "{}"
# create an instance of TenantCollection from a JSON string
tenant_collection_instance = TenantCollection.from_json(json)
# print the JSON string representation of the object
print TenantCollection.to_json()

# convert the object into a dict
tenant_collection_dict = tenant_collection_instance.to_dict()
# create an instance of TenantCollection from a dict
tenant_collection_form_dict = tenant_collection.from_dict(tenant_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


