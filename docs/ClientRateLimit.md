# ClientRateLimit

A service client rate limit. Rate Limits can be used to prevent service clients from creating too many requests to your API. They can also limit the number of requests to Authress management APIs, or contain a maximum quota for a client before it is not longer allowed to make additional requests.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The sliding window timeslice duration for which this quota applies. This value must conform to the ISO8601 format, see the enum for allow values. | 
**quota** | **int** | The maximum number of requests allowed during the duration. | 

## Example

```python
from authress.models.client_rate_limit import ClientRateLimit

# TODO update the JSON string below
json = "{}"
# create an instance of ClientRateLimit from a JSON string
client_rate_limit_instance = ClientRateLimit.from_json(json)
# print the JSON string representation of the object
print ClientRateLimit.to_json()

# convert the object into a dict
client_rate_limit_dict = client_rate_limit_instance.to_dict()
# create an instance of ClientRateLimit from a dict
client_rate_limit_from_dict = ClientRateLimit.from_dict(client_rate_limit_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


