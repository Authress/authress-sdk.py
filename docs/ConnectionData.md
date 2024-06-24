# ConnectionData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**developer_account_id** | **str** | The Developer Account ID associated with the credentials. This is necessary for some providers, such as Apple Login. | [optional] 
**name** | **str** | The name of this connection when displayed in the Authress management portal | [optional] 
**supported_content_type** | **str** | URL encode OAuth token parameters - Some authentication APIs don't support JSON, in these cases enable the url encoded form data parameters. | [optional] [default to 'application/json']
**oidc_user_endpoint_url** | **str** | By default, the **sub** claim of the JWT is used to identify the user from this provider. However, not all providers are OpenID compliant. Here you can provide an optional user data endpoint to fetch additional user profile information and an expression to identify a new user ID from available properties. | [optional] 
**user_id_expression** | **str** | By default, the **sub** claim of the JWT is used to identify the user from this provider. However, not all providers are OpenID compliant. Here you can provide an optional user expression to identify a new user ID from available properties found from the oidcUserEndpointUrl. (The default is **{sub}**, any claims may be used.) | [optional] [default to '{sub}']
**trust_identity_user_id** | **bool** | Authress generates unique user IDs for every user, however if you trust your identity provider to handle unique ID generate across **ALL customers**, then it is safe to reuse the user ID from the provider. | [optional] [default to False]

## Example

```python
from authress.models.connection_data import ConnectionData

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionData from a JSON string
connection_data_instance = ConnectionData.from_json(json)
# print the JSON string representation of the object
print ConnectionData.to_json()

# convert the object into a dict
connection_data_dict = connection_data_instance.to_dict()
# create an instance of ConnectionData from a dict
connection_data_from_dict = ConnectionData.from_dict(connection_data_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


