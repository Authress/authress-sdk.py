# PermissionCollection

A collect of permissions that the user has to a resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**PermissionCollectionAccount**](PermissionCollectionAccount.md) |  | [optional] 
**user_id** | **str** |  | 
**permissions** | [**List[PermissionObject]**](PermissionObject.md) | A list of the permissions | 

## Example

```python
from authress.models.permission_collection import PermissionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionCollection from a JSON string
permission_collection_instance = PermissionCollection.from_json(json)
# print the JSON string representation of the object
print PermissionCollection.to_json()

# convert the object into a dict
permission_collection_dict = permission_collection_instance.to_dict()
# create an instance of PermissionCollection from a dict
permission_collection_from_dict = PermissionCollection.from_dict(permission_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


