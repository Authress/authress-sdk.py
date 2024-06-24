# Link

A url linking object that complies to application/links+json RFC. Either is an IANA approved link relation or has a custom rel specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The absolute url pointing to the reference resource. | 
**rel** | **str** | Optional property indicating the type of link if it is not a default IANA approved global link relation. | [optional] 

## Example

```python
from authress.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print Link.to_json()

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_from_dict = Link.from_dict(link_dict)
```
[[API Models]](./README.md#documentation-for-models) ☆ [[API Endpoints]](./README.md#documentation-for-api-endpoints) ☆ [[Back to Repo]](../README.md)


