# OAuthTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | An expiring access token that can be used to access either Authress or any platform service. | 

## Example

```python
from authress.models.o_auth_token_response import OAuthTokenResponse

json = "{}"
# create an instance of OAuthTokenResponse from a JSON string
o_auth_token_response_instance = OAuthTokenResponse.from_json(json)
# print the JSON string representation of the object
print OAuthTokenResponse.to_json()

# convert the object into a dict
o_auth_token_response_dict = o_auth_token_response_instance.to_dict()
# create an instance of OAuthTokenResponse from a dict
o_auth_token_response_from_dict = OAuthTokenResponse.from_dict(o_auth_token_response_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


