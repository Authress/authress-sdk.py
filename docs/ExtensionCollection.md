# ExtensionCollection

A collection of platform extensions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extensions** | [**List[Extension]**](Extension.md) |  |
**pagination** | [**Pagination**](Pagination.md) |  | [optional]

## Example

```python
from authress.models.extension_collection import ExtensionCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionCollection from a JSON string
extension_collection_instance = ExtensionCollection.from_json(json)
# print the JSON string representation of the object
print ExtensionCollection.to_json()

# convert the object into a dict
extension_collection_dict = extension_collection_instance.to_dict()
# create an instance of ExtensionCollection from a dict
extension_collection_form_dict = extension_collection.from_dict(extension_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


