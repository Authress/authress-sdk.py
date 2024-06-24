# GroupCollection

A collection of groups

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) | A list of groups | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**links** | [**CollectionLinks**](CollectionLinks.md) |  | 

## Example

```python
from authress.models.group_collection import GroupCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GroupCollection from a JSON string
group_collection_instance = GroupCollection.from_json(json)
# print the JSON string representation of the object
print GroupCollection.to_json()

# convert the object into a dict
group_collection_dict = group_collection_instance.to_dict()
# create an instance of GroupCollection from a dict
group_collection_from_dict = GroupCollection.from_dict(group_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


