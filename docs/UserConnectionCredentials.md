# UserConnectionCredentials

The user credentials for this connection which can be used to access the connection provider APIs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token. | 

## Example

```python
from authress.models.user_connection_credentials import UserConnectionCredentials

json = "{}"
# create an instance of UserConnectionCredentials from a JSON string
user_connection_credentials_instance = UserConnectionCredentials.from_json(json)
# print the JSON string representation of the object
print UserConnectionCredentials.to_json()

# convert the object into a dict
user_connection_credentials_dict = user_connection_credentials_instance.to_dict()
# create an instance of UserConnectionCredentials from a dict
user_connection_credentials_from_dict = UserConnectionCredentials.from_dict(user_connection_credentials_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


