# CollectionLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 
**next** | [**Link**](Link.md) |  | [optional] 

## Example

```python
from authress.models.collection_links import CollectionLinks

json = "{}"
# create an instance of CollectionLinks from a JSON string
collection_links_instance = CollectionLinks.from_json(json)
# print the JSON string representation of the object
print CollectionLinks.to_json()

# convert the object into a dict
collection_links_dict = collection_links_instance.to_dict()
# create an instance of CollectionLinks from a dict
collection_links_from_dict = CollectionLinks.from_dict(collection_links_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


