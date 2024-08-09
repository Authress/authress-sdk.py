# ExtensionClient

The extension's client configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The unique ID of the client. | [readonly] 
**rate_limits** | [**List[ClientRateLimit]**](ClientRateLimit.md) | A list of the service client rate limits. Rate Limits can be used to prevent service clients from creating too many requests to your API. They can also limit the number of requests to Authress management APIs, or contain a maximum quota for a client before it is not longer allowed to make additional requests. | [optional] 
**links** | [**Links**](Links.md) |  | [optional] 

## Example

```python
from authress.models.extension_client import ExtensionClient

json = "{}"
# create an instance of ExtensionClient from a JSON string
extension_client_instance = ExtensionClient.from_json(json)
# print the JSON string representation of the object
print ExtensionClient.to_json()

# convert the object into a dict
extension_client_dict = extension_client_instance.to_dict()
# create an instance of ExtensionClient from a dict
extension_client_from_dict = ExtensionClient.from_dict(extension_client_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


