# AccessRequestCollection

A collection of access requests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[AccessRequest]**](AccessRequest.md) | A list of access requests | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**links** | [**CollectionLinks**](CollectionLinks.md) |  | 

## Example

```python
from authress.models.access_request_collection import AccessRequestCollection

json = "{}"
# create an instance of AccessRequestCollection from a JSON string
access_request_collection_instance = AccessRequestCollection.from_json(json)
# print the JSON string representation of the object
print AccessRequestCollection.to_json()

# convert the object into a dict
access_request_collection_dict = access_request_collection_instance.to_dict()
# create an instance of AccessRequestCollection from a dict
access_request_collection_from_dict = AccessRequestCollection.from_dict(access_request_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


