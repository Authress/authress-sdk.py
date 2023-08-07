# ClientOptions

A set of client specific options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_user_permissions_access** | **bool** | Grant the client access to verify authorization on behalf of any user. | [optional] [default to False]
**grant_token_generation** | **bool** | Grant the client access to generate oauth tokens on behalf of the Authress account. **Security Warning**: This means that this client can impersonate any user, and should only be used when connecting an existing custom Authorization Server to Authress, when that server does not support a standard OAuth connection. | [optional] [default to False]

## Example

```python
from authress.models.client_options import ClientOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ClientOptions from a JSON string
client_options_instance = ClientOptions.from_json(json)
# print the JSON string representation of the object
print ClientOptions.to_json()

# convert the object into a dict
client_options_dict = client_options_instance.to_dict()
# create an instance of ClientOptions from a dict
client_options_form_dict = client_options.from_dict(client_options_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


