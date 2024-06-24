# AccessRecordCollection

A collection of access records

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[AccessRecord]**](AccessRecord.md) | A list of access records | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**links** | [**CollectionLinks**](CollectionLinks.md) |  | 

## Example

```python
from authress.models.access_record_collection import AccessRecordCollection

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRecordCollection from a JSON string
access_record_collection_instance = AccessRecordCollection.from_json(json)
# print the JSON string representation of the object
print AccessRecordCollection.to_json()

# convert the object into a dict
access_record_collection_dict = access_record_collection_instance.to_dict()
# create an instance of AccessRecordCollection from a dict
access_record_collection_from_dict = AccessRecordCollection.from_dict(access_record_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


