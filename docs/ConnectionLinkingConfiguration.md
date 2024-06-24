# ConnectionLinkingConfiguration

Linking configuration enables users to connect identities from different connections together, so that they can log in with either connection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Specify the type of linking supported by this connection. The default configuration is DISABLED, meaning that users cannot link their identity from one connection to another connection. Both connections must allow for linking for a link to be successful. By default linking is disabled because it comes with security implications, users can potentially use linking through malicious connections to steal identities from other users.&lt;br&gt;&lt;ul&gt;&lt;li&gt;EXPLICIT - Users can use the linking API to link accounts.&lt;/li&gt;&lt;li&gt;AUTOMATIC - When a user signs up with a new account, if the verified email address matches an existing account, the two accounts will be automatically linked.&lt;/li&gt;&lt;li&gt;Set to &lt;code&gt;null&lt;/code&gt; or leave unspecified to disable identity linking.&lt;/li&gt;&lt;/ul&gt; | [optional] 

## Example

```python
from authress.models.connection_linking_configuration import ConnectionLinkingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionLinkingConfiguration from a JSON string
connection_linking_configuration_instance = ConnectionLinkingConfiguration.from_json(json)
# print the JSON string representation of the object
print ConnectionLinkingConfiguration.to_json()

# convert the object into a dict
connection_linking_configuration_dict = connection_linking_configuration_instance.to_dict()
# create an instance of ConnectionLinkingConfiguration from a dict
connection_linking_configuration_from_dict = ConnectionLinkingConfiguration.from_dict(connection_linking_configuration_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


