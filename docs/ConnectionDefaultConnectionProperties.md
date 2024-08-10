# ConnectionDefaultConnectionProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Default OAuth scopes to use for every request (leave blank to remove scopes). | [optional] [default to 'profile email openid']

## Example

```python
from authress.models.connection_default_connection_properties import ConnectionDefaultConnectionProperties

json = "{}"
# create an instance of ConnectionDefaultConnectionProperties from a JSON string
connection_default_connection_properties_instance = ConnectionDefaultConnectionProperties.from_json(json)
# print the JSON string representation of the object
print ConnectionDefaultConnectionProperties.to_json()

# convert the object into a dict
connection_default_connection_properties_dict = connection_default_connection_properties_instance.to_dict()
# create an instance of ConnectionDefaultConnectionProperties from a dict
connection_default_connection_properties_from_dict = ConnectionDefaultConnectionProperties.from_dict(connection_default_connection_properties_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


