# AccountCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**Account**](Account.md) |  | 

## Example

```python
from authress.models.account_collection import AccountCollection

json = "{}"
# create an instance of AccountCollection from a JSON string
account_collection_instance = AccountCollection.from_json(json)
# print the JSON string representation of the object
print AccountCollection.to_json()

# convert the object into a dict
account_collection_dict = account_collection_instance.to_dict()
# create an instance of AccountCollection from a dict
account_collection_from_dict = AccountCollection.from_dict(account_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


