# TenantData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from authress.models.tenant_data import TenantData

# TODO update the JSON string below
json = "{}"
# create an instance of TenantData from a JSON string
tenant_data_instance = TenantData.from_json(json)
# print the JSON string representation of the object
print TenantData.to_json()

# convert the object into a dict
tenant_data_dict = tenant_data_instance.to_dict()
# create an instance of TenantData from a dict
tenant_data_from_dict = TenantData.from_dict(tenant_data_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


