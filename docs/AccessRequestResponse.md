# AccessRequestResponse

A dynamic body to support request PATCH operations

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | New result, either approve or deny the request | 

## Example

```python
from authress.models.access_request_response import AccessRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequestResponse from a JSON string
access_request_response_instance = AccessRequestResponse.from_json(json)
# print the JSON string representation of the object
print AccessRequestResponse.to_json()

# convert the object into a dict
access_request_response_dict = access_request_response_instance.to_dict()
# create an instance of AccessRequestResponse from a dict
access_request_response_from_dict = AccessRequestResponse.from_dict(access_request_response_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


