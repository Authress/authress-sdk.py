# AuthenticationTokenConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_duration** | **duration** | How long should Authress generated access tokens (JWTs) last for in minutes. This controls how often tokens expiry (*exp*). The default is 24 hours. The minimum is one minute and the max is twenty-four hours. | [optional] [default to 'PT24H']
**session_duration** | **duration** | How long should user authentication sessions last for in minutes. This controls how often users are forced to log in again. User sessions are optimized to provide the best user experience for your application. The default is 90 days. The minimum is one minute and the max is 90 days. | [optional] [default to 'P30D']

## Example

```python
from authress.models.authentication_token_configuration import AuthenticationTokenConfiguration

token_configuration = AuthenticationTokenConfiguration(
    access_token_duration="PT24H",
    session_duration="P30D"
)

print token_configuration.to_json()
```

[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)