# UserRoleCollection

A collect of roles that the user has to a resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  |
**roles** | [**List[UserRole]**](UserRole.md) | A list of the roles |

## Example

```python
from authress.models.user_role_collection import UserRoleCollection

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleCollection from a JSON string
user_role_collection_instance = UserRoleCollection.from_json(json)
# print the JSON string representation of the object
print UserRoleCollection.to_json()

# convert the object into a dict
user_role_collection_dict = user_role_collection_instance.to_dict()
# create an instance of UserRoleCollection from a dict
user_role_collection_form_dict = user_role_collection.from_dict(user_role_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


