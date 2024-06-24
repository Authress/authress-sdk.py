# TenantUser


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 

## Example

```python
from authress.models.tenant_user import TenantUser

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUser from a JSON string
tenant_user_instance = TenantUser.from_json(json)
# print the JSON string representation of the object
print TenantUser.to_json()

# convert the object into a dict
tenant_user_dict = tenant_user_instance.to_dict()
# create an instance of TenantUser from a dict
tenant_user_from_dict = TenantUser.from_dict(tenant_user_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


