# UserIdentityCollection

A collection of user identities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserIdentity]**](UserIdentity.md) | A list of users |
**pagination** | [**Pagination**](Pagination.md) |  | [optional]
**links** | [**CollectionLinks**](CollectionLinks.md) |  |

## Example

```python
from authress.models.user_identity_collection import UserIdentityCollection

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentityCollection from a JSON string
user_identity_collection_instance = UserIdentityCollection.from_json(json)
# print the JSON string representation of the object
print UserIdentityCollection.to_json()

# convert the object into a dict
user_identity_collection_dict = user_identity_collection_instance.to_dict()
# create an instance of UserIdentityCollection from a dict
user_identity_collection_form_dict = user_identity_collection.from_dict(user_identity_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


