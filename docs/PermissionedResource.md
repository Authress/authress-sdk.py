# PermissionedResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | [**List[ResourcePermission]**](ResourcePermission.md) |  | 

## Example

```python
from authress.models.permissioned_resource import PermissionedResource

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionedResource from a JSON string
permissioned_resource_instance = PermissionedResource.from_json(json)
# print the JSON string representation of the object
print PermissionedResource.to_json()

# convert the object into a dict
permissioned_resource_dict = permissioned_resource_instance.to_dict()
# create an instance of PermissionedResource from a dict
permissioned_resource_from_dict = PermissionedResource.from_dict(permissioned_resource_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


