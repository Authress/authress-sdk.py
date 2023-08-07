# UserRole

A role with associated role data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** |  |

## Example

```python
from authress.models.user_role import UserRole

# TODO update the JSON string below
json = "{}"
# create an instance of UserRole from a JSON string
user_role_instance = UserRole.from_json(json)
# print the JSON string representation of the object
print UserRole.to_json()

# convert the object into a dict
user_role_dict = user_role_instance.to_dict()
# create an instance of UserRole from a dict
user_role_form_dict = user_role.from_dict(user_role_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


