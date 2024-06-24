# ClientAccessKey

A client access key configuration. The configuration contains information about the key. On first creation the configuration also contains the raw `clientSecret` and `accessKey` for use with OAuth and the Authress SDKs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** | The unique ID of the client. | [optional] [readonly] 
**client_id** | **str** | The unique ID of the client. | [readonly] 
**public_key** | **str** | Specify a public key on access key creation to bring your own private key. When left blank, Authress will automatically generate a private and public key pair and then return the private key as part of the request. This property holds the public key. | [optional] 
**generation_date** | **datetime** |  | [optional] [readonly] 
**client_secret** | **str** | The unencoded OAuth client secret used with the OAuth endpoints to request a JWT using the &#x60;client_credentials&#x60; grant type. Pass the clientId and the clientSecret to the documented /tokens endpoint. | [optional] [readonly] 
**access_key** | **str** | An encoded access key which contains identifying information for client access token creation. For direct use with the Authress SDKs. This private access key must be saved on first creation as it is discarded afterwards. Authress only saves the corresponding public key to verify the private access key. | [optional] [readonly] 

## Example

```python
from authress.models.client_access_key import ClientAccessKey

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAccessKey from a JSON string
client_access_key_instance = ClientAccessKey.from_json(json)
# print the JSON string representation of the object
print ClientAccessKey.to_json()

# convert the object into a dict
client_access_key_dict = client_access_key_instance.to_dict()
# create an instance of ClientAccessKey from a dict
client_access_key_from_dict = ClientAccessKey.from_dict(client_access_key_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


