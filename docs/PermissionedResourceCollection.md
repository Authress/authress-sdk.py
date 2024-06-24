# PermissionedResourceCollection

A collection of resource permissions that have been defined.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**List[PermissionedResource]**](PermissionedResource.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**links** | [**CollectionLinks**](CollectionLinks.md) |  | 

## Example

```python
from authress.models.permissioned_resource_collection import PermissionedResourceCollection

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionedResourceCollection from a JSON string
permissioned_resource_collection_instance = PermissionedResourceCollection.from_json(json)
# print the JSON string representation of the object
print PermissionedResourceCollection.to_json()

# convert the object into a dict
permissioned_resource_collection_dict = permissioned_resource_collection_instance.to_dict()
# create an instance of PermissionedResourceCollection from a dict
permissioned_resource_collection_from_dict = PermissionedResourceCollection.from_dict(permissioned_resource_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


