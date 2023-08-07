# IdentityRequest

Request to link an identity provider's audience and your app's audience with Authress.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwt** | **str** | A valid JWT OIDC compliant token which will still pass authentication requests to the identity provider. Must contain a unique audience and issuer. | [optional]
**issuer** | **str** | The issuer of the OAuth OIDC provider&#39;s JWTs. This value should match the &#x60;iss&#x60; claim in the provided tokens exactly. | [optional]
**preferred_audience** | **str** | If the &#x60;jwt&#x60; token contains more than one valid audience, then the single audience that should associated with Authress. If more than one audience is preferred, repeat this call with each one. | [optional] [default to '*']

## Example

```python
from authress.models.identity_request import IdentityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityRequest from a JSON string
identity_request_instance = IdentityRequest.from_json(json)
# print the JSON string representation of the object
print IdentityRequest.to_json()

# convert the object into a dict
identity_request_dict = identity_request_instance.to_dict()
# create an instance of IdentityRequest from a dict
identity_request_form_dict = identity_request.from_dict(identity_request_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


