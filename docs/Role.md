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
from authress import Role, PermissionObject

role = Role(
    name = "Documents Viewer",
    role_id = "ro_documents_viewer",
    permissions = [
        PermissionObject(
            action = "documents:read",
            allow = True,
            grant = True,
            delegate = False
        )
    ]
)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


