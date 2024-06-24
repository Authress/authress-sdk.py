# UserIdentity

The composite user identity stored in Authress sourced by the customer SSO/SAML/OAuth IdP.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**name** | **str** | The user's formatted display name. | [optional] 
**picture** | **str** | A url that resolves to a picture that can be rendered. | [optional] 
**email** | **str** | The user's verified email address sourced from their SSO IdP. | [optional] 

## Example

```python
from authress.models.user_identity import UserIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of UserIdentity from a JSON string
user_identity_instance = UserIdentity.from_json(json)
# print the JSON string representation of the object
print UserIdentity.to_json()

# convert the object into a dict
user_identity_dict = user_identity_instance.to_dict()
# create an instance of UserIdentity from a dict
user_identity_from_dict = UserIdentity.from_dict(user_identity_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


