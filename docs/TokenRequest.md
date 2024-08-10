# TokenRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statements** | [**List[Statement]**](Statement.md) | A list of statements which match roles to resources. The token will have all statements apply to it. | 
**expires** | **datetime** | The ISO8601 datetime when the token will expire. Default is 24 hours from now. | 

## Example

```python
from authress.models.token_request import TokenRequest

json = "{}"
# create an instance of TokenRequest from a JSON string
token_request_instance = TokenRequest.from_json(json)
# print the JSON string representation of the object
print TokenRequest.to_json()

# convert the object into a dict
token_request_dict = token_request_instance.to_dict()
# create an instance of TokenRequest from a dict
token_request_from_dict = TokenRequest.from_dict(token_request_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


