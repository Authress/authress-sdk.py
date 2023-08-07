# ResourcePermission


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  |
**allow** | **bool** |  |

## Example

```python
from authress.models.resource_permission import ResourcePermission

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcePermission from a JSON string
resource_permission_instance = ResourcePermission.from_json(json)
# print the JSON string representation of the object
print ResourcePermission.to_json()

# convert the object into a dict
resource_permission_dict = resource_permission_instance.to_dict()
# create an instance of ResourcePermission from a dict
resource_permission_form_dict = resource_permission.from_dict(resource_permission_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


