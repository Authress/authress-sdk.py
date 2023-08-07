# ExtensionClient

The extension's client configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The unique ID of the client. | [readonly]
**links** | [**Links**](Links.md) |  |

## Example

```python
from authress.models.extension_client import ExtensionClient

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionClient from a JSON string
extension_client_instance = ExtensionClient.from_json(json)
# print the JSON string representation of the object
print ExtensionClient.to_json()

# convert the object into a dict
extension_client_dict = extension_client_instance.to_dict()
# create an instance of ExtensionClient from a dict
extension_client_form_dict = extension_client.from_dict(extension_client_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


