# ResourceUsersCollection

A collection of users with explicit permission to a resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[UserRoleCollection]**](UserRoleCollection.md) | A list of users | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**links** | [**CollectionLinks**](CollectionLinks.md) |  | 

## Example

```python
from authress.models.resource_users_collection import ResourceUsersCollection

json = "{}"
# create an instance of ResourceUsersCollection from a JSON string
resource_users_collection_instance = ResourceUsersCollection.from_json(json)
# print the JSON string representation of the object
print ResourceUsersCollection.to_json()

# convert the object into a dict
resource_users_collection_dict = resource_users_collection_instance.to_dict()
# create an instance of ResourceUsersCollection from a dict
resource_users_collection_from_dict = ResourceUsersCollection.from_dict(resource_users_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


