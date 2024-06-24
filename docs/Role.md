# Role

The role which contains a list of permissions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** | Unique identifier for the role, can be specified on creation, and used by records to map to permissions. | [optional] 
**name** | **str** | A helpful name for this role | 
**description** | **str** | A description for when to the user as well as additional information. | [optional] 
**permissions** | [**List[PermissionObject]**](PermissionObject.md) | A list of the permissions | 

## Example

```python
from authress.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print Role.to_json()

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_from_dict = Role.from_dict(role_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


