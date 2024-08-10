# ConnectionCollection

A collection of connections.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[Connection]**](Connection.md) |  | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from authress.models.connection_collection import ConnectionCollection

json = "{}"
# create an instance of ConnectionCollection from a JSON string
connection_collection_instance = ConnectionCollection.from_json(json)
# print the JSON string representation of the object
print ConnectionCollection.to_json()

# convert the object into a dict
connection_collection_dict = connection_collection_instance.to_dict()
# create an instance of ConnectionCollection from a dict
connection_collection_from_dict = ConnectionCollection.from_dict(connection_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


