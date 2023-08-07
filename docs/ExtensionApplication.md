# ExtensionApplication

The extension's application configuration. The application contains the necessary information for users to log in to the extension.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | The unique ID of the application. | [readonly]
**redirect_urls** | **List[str]** |  | [optional]
**links** | [**Links**](Links.md) |  |

## Example

```python
from authress.models.extension_application import ExtensionApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionApplication from a JSON string
extension_application_instance = ExtensionApplication.from_json(json)
# print the JSON string representation of the object
print ExtensionApplication.to_json()

# convert the object into a dict
extension_application_dict = extension_application_instance.to_dict()
# create an instance of ExtensionApplication from a dict
extension_application_form_dict = extension_application.from_dict(extension_application_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


