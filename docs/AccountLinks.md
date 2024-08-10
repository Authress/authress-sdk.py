# AccountLinks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**Link**](Link.md) |  | 

## Example

```python
from authress.models.account_links import AccountLinks

json = "{}"
# create an instance of AccountLinks from a JSON string
account_links_instance = AccountLinks.from_json(json)
# print the JSON string representation of the object
print AccountLinks.to_json()

# convert the object into a dict
account_links_dict = account_links_instance.to_dict()
# create an instance of AccountLinks from a dict
account_links_from_dict = AccountLinks.from_dict(account_links_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


