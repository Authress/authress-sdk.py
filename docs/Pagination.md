# Pagination

Details containing how to pagination through the collection. Consists of an optional *next* property that may contain a cursor. Pagination is mutable and the list can change between requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next** | [**PaginationNext**](PaginationNext.md) |  | [optional]

## Example

```python
from authress.models.pagination import Pagination

# TODO update the JSON string below
json = "{}"
# create an instance of Pagination from a JSON string
pagination_instance = Pagination.from_json(json)
# print the JSON string representation of the object
print Pagination.to_json()

# convert the object into a dict
pagination_dict = pagination_instance.to_dict()
# create an instance of Pagination from a dict
pagination_form_dict = pagination.from_dict(pagination_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


