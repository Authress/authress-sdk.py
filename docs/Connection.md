# Connection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'OAUTH2']
**connection_id** | **str** |  | [optional] 
**authentication_url** | **str** | Authorization URL of the provider (where the user logs in). For OAuth this is the authorization URL. For SAML, specify the **SSO URL** in this property. | [optional] 
**token_url** | **str** | The token exchange url (where we validate the token). | [optional] 
**issuer_url** | **str** | The unique identifier tied to the provider's domain used for TLS verification. In OAuth, this is the JWT **iss** property. For SAML, specify the **Entity ID** in this property. | [optional] 
**provider_certificate** | **str** | The Provider's SAML public certificate which can be used to verify the signature in signed SAML assertions from the provider. | [optional] 
**client_id** | **str** | Provider's client ID used to verify the token | [optional] 
**client_secret_id** | **str** | Provider's client secret identifier used to identify the client secret within your account. Some provider require this property. | [optional] 
**client_secret** | **str** | Provider's client secret used to verify the token | [optional] 
**user_data_configuration** | [**ConnectionUserDataConfiguration**](ConnectionUserDataConfiguration.md) |  | [optional] 
**data** | [**ConnectionData**](ConnectionData.md) |  | [optional] 
**default_connection_properties** | [**ConnectionDefaultConnectionProperties**](ConnectionDefaultConnectionProperties.md) |  | [optional] 
**conditions** | [**ConnectionConditions**](ConnectionConditions.md) |  | [optional] 
**linking_configuration** | [**ConnectionLinkingConfiguration**](ConnectionLinkingConfiguration.md) |  | [optional] 
**created_time** | **datetime** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**is_active_connection** | **bool** |  | [optional] [readonly] 
**tags** | **Dict[str, str]** | The tags associated with this resource, this property is an map. { key1: value1, key2: value2 } | [optional] 

## Example

```python
from authress.models.connection import Connection

json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print Connection.to_json()

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


