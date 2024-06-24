# Client

A client configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The unique ID of the client. | [readonly] 
**created_time** | **datetime** |  | [readonly] 
**name** | **str** | The name of the client | [optional] 
**options** | [**ClientOptions**](ClientOptions.md) |  | [optional] 
**rate_limits** | [**List[ClientRateLimit]**](ClientRateLimit.md) | A list of the service client rate limits. Rate Limits can be used to prevent service clients from creating too many requests to your API. They can also limit the number of requests to Authress management APIs, or contain a maximum quota for a client before it is not longer allowed to make additional requests. | [optional] 
**verification_keys** | [**List[ClientAccessKey]**](ClientAccessKey.md) | A list of the service client access keys. | [optional] [readonly] 
**tags** | **Dict[str, str]** | The tags associated with this resource, this property is an map. { key1: value1, key2: value2 } | [optional] 

## Example

```python
from authress.models.client import Client

# TODO update the JSON string below
json = "{}"
# create an instance of Client from a JSON string
client_instance = Client.from_json(json)
# print the JSON string representation of the object
print Client.to_json()

# convert the object into a dict
client_dict = client_instance.to_dict()
# create an instance of Client from a dict
client_from_dict = Client.from_dict(client_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


