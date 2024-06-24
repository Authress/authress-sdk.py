# PermissionObject

The collective action and associate grants on a permission

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action the permission grants, can be scoped using &#x60;:&#x60; and parent actions imply sub-resource permissions, action:* or action implies action:sub-action. This property is case-insensitive, it will always be cast to lowercase before comparing actions to user permissions. | 
**allow** | **bool** | Does this permission grant the user the ability to execute the action? | 
**grant** | **bool** | Allows the user to give the permission to others without being able to execute the action. | 
**delegate** | **bool** | Allows delegating or granting the permission to others without being able to execute the action. | 

## Example

```python
from authress.models.permission_object import PermissionObject

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionObject from a JSON string
permission_object_instance = PermissionObject.from_json(json)
# print the JSON string representation of the object
print PermissionObject.to_json()

# convert the object into a dict
permission_object_dict = permission_object_instance.to_dict()
# create an instance of PermissionObject from a dict
permission_object_from_dict = PermissionObject.from_dict(permission_object_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


