# OAuthAuthorizeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The authorization code to be used with the /tokens endpoint to retrieve an access_token. | 

## Example

```python
from authress.models.o_auth_authorize_response import OAuthAuthorizeResponse

json = "{}"
# create an instance of OAuthAuthorizeResponse from a JSON string
o_auth_authorize_response_instance = OAuthAuthorizeResponse.from_json(json)
# print the JSON string representation of the object
print OAuthAuthorizeResponse.to_json()

# convert the object into a dict
o_auth_authorize_response_dict = o_auth_authorize_response_instance.to_dict()
# create an instance of OAuthAuthorizeResponse from a dict
o_auth_authorize_response_from_dict = OAuthAuthorizeResponse.from_dict(o_auth_authorize_response_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


