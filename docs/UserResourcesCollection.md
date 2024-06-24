# UserResourcesCollection

A collect of permissions that the user has to a resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**PermissionCollectionAccount**](PermissionCollectionAccount.md) |  | [optional] 
**user_id** | **str** |  | 
**resources** | [**List[Resource]**](Resource.md) | A list of the resources the user has some permission to. | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**links** | [**CollectionLinks**](CollectionLinks.md) |  | 

## Example

```python
from authress.models.user_resources_collection import UserResourcesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of UserResourcesCollection from a JSON string
user_resources_collection_instance = UserResourcesCollection.from_json(json)
# print the JSON string representation of the object
print UserResourcesCollection.to_json()

# convert the object into a dict
user_resources_collection_dict = user_resources_collection_instance.to_dict()
# create an instance of UserResourcesCollection from a dict
user_resources_collection_from_dict = UserResourcesCollection.from_dict(user_resources_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


