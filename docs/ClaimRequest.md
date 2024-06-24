# ClaimRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_resource** | **str** | The parent resource to add a sub-resource to. The resource must have a resource configuration that add the permission CLAIM for this to work. | 
**resource_id** | **str** | The sub-resource the user is requesting Admin ownership over. | 

## Example

```python
from authress.models.claim_request import ClaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimRequest from a JSON string
claim_request_instance = ClaimRequest.from_json(json)
# print the JSON string representation of the object
print ClaimRequest.to_json()

# convert the object into a dict
claim_request_dict = claim_request_instance.to_dict()
# create an instance of ClaimRequest from a dict
claim_request_from_dict = ClaimRequest.from_dict(claim_request_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


