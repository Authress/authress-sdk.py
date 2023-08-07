# AccessRequest

The access requested by a user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Unique identifier for the request. | [readonly]
**last_updated** | **datetime** | The expected last time the request was updated | [optional] [readonly]
**status** | **str** | Current status of the access request. | [optional] [readonly]
**access** | [**AccessTemplate**](AccessTemplate.md) |  |
**links** | [**AccountLinks**](AccountLinks.md) |  |
**tags** | **Dict[str, str]** | The tags associated with this resource, this property is an map. { key1: value1, key2: value2 } | [optional]

## Example

```python
from authress.models.access_request import AccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccessRequest from a JSON string
access_request_instance = AccessRequest.from_json(json)
# print the JSON string representation of the object
print AccessRequest.to_json()

# convert the object into a dict
access_request_dict = access_request_instance.to_dict()
# create an instance of AccessRequest from a dict
access_request_form_dict = access_request.from_dict(access_request_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


