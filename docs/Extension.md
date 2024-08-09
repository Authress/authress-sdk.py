# Extension


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_id** | **str** |  | [readonly] 
**name** | **str** | The name of the extension. This name is visible in the Authress management portal | [optional] 
**created_time** | **datetime** |  | [readonly] 
**application** | [**ExtensionApplication**](ExtensionApplication.md) |  | [optional] 
**client** | [**ExtensionClient**](ExtensionClient.md) |  | [optional] 
**tags** | **Dict[str, str]** | The tags associated with this resource, this property is an map. { key1: value1, key2: value2 } | [optional] 

## Example

```python
from authress.models.extension import Extension

json = "{}"
# create an instance of Extension from a JSON string
extension_instance = Extension.from_json(json)
# print the JSON string representation of the object
print Extension.to_json()

# convert the object into a dict
extension_dict = extension_instance.to_dict()
# create an instance of Extension from a dict
extension_from_dict = Extension.from_dict(extension_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


