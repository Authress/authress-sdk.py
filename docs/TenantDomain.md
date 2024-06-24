# TenantDomain

The tenant linked domain configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The tenant linked domain. | 

## Example

```python
from authress.models.tenant_domain import TenantDomain

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDomain from a JSON string
tenant_domain_instance = TenantDomain.from_json(json)
# print the JSON string representation of the object
print TenantDomain.to_json()

# convert the object into a dict
tenant_domain_dict = tenant_domain_instance.to_dict()
# create an instance of TenantDomain from a dict
tenant_domain_from_dict = TenantDomain.from_dict(tenant_domain_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


