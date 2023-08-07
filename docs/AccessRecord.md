# AccessRecord

The access record which links users to roles.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_id** | **str** | Unique identifier for the record, can be specified on record creation. | [optional]
**name** | **str** | A helpful name for this record |
**description** | **str** | More details about this record | [optional]
**capacity** | **float** | Percentage capacity of record that is filled. | [optional] [readonly]
**last_updated** | **datetime** | The expected last time the record was updated | [optional] [readonly]
**status** | **str** | Current status of the access record. | [optional] [readonly]
**account** | [**AccessRecordAccount**](AccessRecordAccount.md) |  |
**users** | [**List[User]**](User.md) | The list of users this record applies to | [optional]
**admins** | [**List[User]**](User.md) | The list of admin that can edit this record even if they do not have global record edit permissions. | [optional]
**groups** | [**List[LinkedGroup]**](LinkedGroup.md) | The list of groups this record applies to. Users in these groups will be receive access to the resources listed. | [optional]
**statements** | [**List[Statement]**](Statement.md) | A list of statements which match roles to resources. |
**links** | [**AccountLinks**](AccountLinks.md) |  |
**tags** | **Dict[str, str]** | The tags associated with this resource, this property is an map. { key1: value1, key2: value2 } | [optional]

## Example

```python
from authress.models.access_record import AccessRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRecord from a JSON string
access_record_instance = AccessRecord.from_json(json)
# print the JSON string representation of the object
print AccessRecord.to_json()

# convert the object into a dict
access_record_dict = access_record_instance.to_dict()
# create an instance of AccessRecord from a dict
access_record_form_dict = access_record.from_dict(access_record_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


