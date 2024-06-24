# LinkedGroup

The referenced group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Unique identifier for the groupId, can be specified on record creation. Must begin with grp_. | 

## Example

```python
from authress.models.linked_group import LinkedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LinkedGroup from a JSON string
linked_group_instance = LinkedGroup.from_json(json)
# print the JSON string representation of the object
print LinkedGroup.to_json()

# convert the object into a dict
linked_group_dict = linked_group_instance.to_dict()
# create an instance of LinkedGroup from a dict
linked_group_from_dict = LinkedGroup.from_dict(linked_group_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


