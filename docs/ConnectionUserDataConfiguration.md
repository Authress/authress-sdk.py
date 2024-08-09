# ConnectionUserDataConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | User data residency - The data residency to store the user specific data in. To ensure high performance and reliability, set to **null**, or to store the user's data only in one specific region, set the region here. Specifying the region reduces reliability, durability, and performance at the benefit of controlling the locality.  | [optional] 

## Example

```python
from authress.models.connection_user_data_configuration import ConnectionUserDataConfiguration

json = "{}"
# create an instance of ConnectionUserDataConfiguration from a JSON string
connection_user_data_configuration_instance = ConnectionUserDataConfiguration.from_json(json)
# print the JSON string representation of the object
print ConnectionUserDataConfiguration.to_json()

# convert the object into a dict
connection_user_data_configuration_dict = connection_user_data_configuration_instance.to_dict()
# create an instance of ConnectionUserDataConfiguration from a dict
connection_user_data_configuration_from_dict = ConnectionUserDataConfiguration.from_dict(connection_user_data_configuration_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


