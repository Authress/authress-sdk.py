# MetadataObject

Metadata and additional properties relevant.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**MetadataObjectAccount**](MetadataObjectAccount.md) |  | [optional]
**user_id** | **str** |  |
**metadata** | **object** | A JSON object limited to 10KB. The owner identified by the sub will always have access to read and update this data. Service clients may have access if the related property on the client is set. Access is restricted to authorized users. |

## Example

```python
from authress.models.metadata_object import MetadataObject

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataObject from a JSON string
metadata_object_instance = MetadataObject.from_json(json)
# print the JSON string representation of the object
print MetadataObject.to_json()

# convert the object into a dict
metadata_object_dict = metadata_object_instance.to_dict()
# create an instance of MetadataObject from a dict
metadata_object_form_dict = metadata_object.from_dict(metadata_object_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


