# Identity

The identifying information which uniquely links a JWT OIDC token to an identity provider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** | The issuer of the JWT token. This can be any OIDC compliant provider. | 
**audience** | **str** | The audience of the JWT token. This can be either an audience for your entire app, or one particular audience for it. If there is more than one audience, multiple identities can be created. | 
**user_id_expression** | **str** | By default, the **sub** claim of the JWT is used to identify the user from this provider. To use an alternate claim or a compound userId resolution, specify an expression. The resolved userId must be the same one that is later used in Authress access records. | [optional] [default to '{sub}']

## Example

```python
from authress.models.identity import Identity

json = "{}"
# create an instance of Identity from a JSON string
identity_instance = Identity.from_json(json)
# print the JSON string representation of the object
print Identity.to_json()

# convert the object into a dict
identity_dict = identity_instance.to_dict()
# create an instance of Identity from a dict
identity_from_dict = Identity.from_dict(identity_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


