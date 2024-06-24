# PaginationNext

A reference to the next page in the collection, pass the cursor as a query parameter in the subsequent request to get the next page.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** |  | 

## Example

```python
from authress.models.pagination_next import PaginationNext

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationNext from a JSON string
pagination_next_instance = PaginationNext.from_json(json)
# print the JSON string representation of the object
print PaginationNext.to_json()

# convert the object into a dict
pagination_next_dict = pagination_next_instance.to_dict()
# create an instance of PaginationNext from a dict
pagination_next_from_dict = PaginationNext.from_dict(pagination_next_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


