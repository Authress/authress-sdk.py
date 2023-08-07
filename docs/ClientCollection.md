# ClientCollection

The collection of a list of clients

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | [**List[Client]**](Client.md) | A list of clients |
**pagination** | [**Pagination**](Pagination.md) |  | [optional]
**links** | [**CollectionLinks**](CollectionLinks.md) |  |

## Example

```python
from authress.models.client_collection import ClientCollection

# TODO update the JSON string below
json = "{}"
# create an instance of ClientCollection from a JSON string
client_collection_instance = ClientCollection.from_json(json)
# print the JSON string representation of the object
print ClientCollection.to_json()

# convert the object into a dict
client_collection_dict = client_collection_instance.to_dict()
# create an instance of ClientCollection from a dict
client_collection_form_dict = client_collection.from_dict(client_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


