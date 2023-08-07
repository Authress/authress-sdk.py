# Connection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'OAUTH2']
**connection_id** | **str** |  | [optional]
**authentication_url** | **str** |  | [optional]
**token_url** | **str** |  | [optional]
**issuer_url** | **str** |  | [optional]
**provider_certificate** | **str** |  | [optional]
**client_id** | **str** |  | [optional]
**client_secret** | **str** |  | [optional]
**data** | [**ConnectionData**](ConnectionData.md) |  | [optional]
**default_connection_properties** | [**ConnectionDefaultConnectionProperties**](ConnectionDefaultConnectionProperties.md) |  | [optional]
**created_time** | **datetime** |  | [optional] [readonly]
**tags** | **Dict[str, str]** | The tags associated with this resource, this property is an map. { key1: value1, key2: value2 } | [optional]

## Example

```python
from authress.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print Connection.to_json()

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_form_dict = connection.from_dict(connection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


