# IdentityCollection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identities** | [**List[Identity]**](Identity.md) |  | 

## Example

```python
from authress.models.identity_collection import IdentityCollection

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityCollection from a JSON string
identity_collection_instance = IdentityCollection.from_json(json)
# print the JSON string representation of the object
print IdentityCollection.to_json()

# convert the object into a dict
identity_collection_dict = identity_collection_instance.to_dict()
# create an instance of IdentityCollection from a dict
identity_collection_from_dict = IdentityCollection.from_dict(identity_collection_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


