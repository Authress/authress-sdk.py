# Group

A group of users, which can be added to access records.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Unique identifier for the groupId, can be specified on record creation. Must begin with grp_. | [optional] 
**name** | **str** | A helpful name for this record | 
**last_updated** | **datetime** | The expected last time the group was updated | [optional] [readonly] 
**users** | [**List[User]**](User.md) | The list of users in this group. A group can have a maximum of 100 users. | 
**admins** | [**List[User]**](User.md) | The list of admins that can edit this record even if they do not have global record edit permissions. | 
**links** | [**AccountLinks**](AccountLinks.md) |  | [optional] 
**tags** | **Dict[str, str]** | The tags associated with this resource, this property is an map. { key1: value1, key2: value2 } | [optional] 

## Example

```python
from authress.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print Group.to_json()

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


