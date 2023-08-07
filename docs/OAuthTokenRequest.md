# OAuthTokenRequest

The OAuth 2.1 token request that follows [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749). The properties in the request must be snake_case to follow the standard.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client identifier to constrain the token to. |
**client_secret** | **str** | The secret associated with the client that authorizes the generation of token it&#39;s behalf. (Either the &#x60;client_secret&#x60; or the &#x60;code_verifier&#x60; is required) | [optional]
**code_verifier** | **str** | The code verifier is the the value used in the generation of the OAuth authorization request &#x60;code_challenge&#x60; property. (Either the &#x60;client_secret&#x60; or the &#x60;code_verifier&#x60; is required) | [optional]
**grant_type** | **str** | A suggestion to the token generation which type of credentials are being provided. | [optional]
**username** | **str** | When using the user password grant_type, specify the username. Authress recommends this should always be an email address. | [optional]
**password** | **str** | When using the user password grant_type, specify the user&#39;s password. | [optional]
**type** | **str** | Enables additional configuration of the grant_type. In the case of user password grant_type, set this to **signup**, to enable the creation of users. Set this to **update**, force update the password associated with the user. | [optional]

## Example

```python
from authress.models.o_auth_token_request import OAuthTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthTokenRequest from a JSON string
o_auth_token_request_instance = OAuthTokenRequest.from_json(json)
# print the JSON string representation of the object
print OAuthTokenRequest.to_json()

# convert the object into a dict
o_auth_token_request_dict = o_auth_token_request_instance.to_dict()
# create an instance of OAuthTokenRequest from a dict
o_auth_token_request_form_dict = o_auth_token_request.from_dict(o_auth_token_request_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


