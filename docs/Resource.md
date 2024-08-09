# Resource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_uri** | **str** | A resource path which can be top level, fully qualified, or end with a *. Parent resources imply permissions to sub-resources. | 

## Example

```python
from authress.models.resource import Resource

json = "{}"
# create an instance of Resource from a JSON string
resource_instance = Resource.from_json(json)
# print the JSON string representation of the object
print Resource.to_json()

# convert the object into a dict
resource_dict = resource_instance.to_dict()
# create an instance of Resource from a dict
resource_from_dict = Resource.from_dict(resource_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


