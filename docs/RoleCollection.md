# RoleCollection

A collection of roles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**List[Role]**](Role.md) | A list of roles |
**pagination** | [**Pagination**](Pagination.md) |  | [optional]
**links** | [**CollectionLinks**](CollectionLinks.md) |  |

## Example

```python
from authress.models.role_collection import RoleCollection

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCollection from a JSON string
role_collection_instance = RoleCollection.from_json(json)
# print the JSON string representation of the object
print RoleCollection.to_json()

# convert the object into a dict
role_collection_dict = role_collection_instance.to_dict()
# create an instance of RoleCollection from a dict
role_collection_form_dict = role_collection.from_dict(role_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


