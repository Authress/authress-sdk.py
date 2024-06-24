# UserToken

A JWT token with represents the user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**PermissionCollectionAccount**](PermissionCollectionAccount.md) |  | [optional] 
**user_id** | **str** |  | 
**token_id** | **str** | The unique identifier for the token | 
**token** | **str** | The access token | 
**links** | [**AccountLinks**](AccountLinks.md) |  | [optional] 

## Example

```python
from authress.models.user_token import UserToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserToken from a JSON string
user_token_instance = UserToken.from_json(json)
# print the JSON string representation of the object
print UserToken.to_json()

# convert the object into a dict
user_token_dict = user_token_instance.to_dict()
# create an instance of UserToken from a dict
user_token_from_dict = UserToken.from_dict(user_token_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


