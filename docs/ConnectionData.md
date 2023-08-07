# ConnectionData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional]
**name** | **str** |  | [optional]
**supported_content_type** | **str** |  | [optional] [default to 'application/json']

## Example

```python
from authress.models.connection_data import ConnectionData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionData from a JSON string
connection_data_instance = ConnectionData.from_json(json)
# print the JSON string representation of the object
print ConnectionData.to_json()

# convert the object into a dict
connection_data_dict = connection_data_instance.to_dict()
# create an instance of ConnectionData from a dict
connection_data_form_dict = connection_data.from_dict(connection_data_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


