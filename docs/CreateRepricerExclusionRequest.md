# CreateRepricerExclusionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **Dict[str, object]** |  | 
**reason** | **str** |  | 
**enabled** | **bool** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from rivalika_sdk.models.create_repricer_exclusion_request import CreateRepricerExclusionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRepricerExclusionRequest from a JSON string
create_repricer_exclusion_request_instance = CreateRepricerExclusionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRepricerExclusionRequest.to_json())

# convert the object into a dict
create_repricer_exclusion_request_dict = create_repricer_exclusion_request_instance.to_dict()
# create an instance of CreateRepricerExclusionRequest from a dict
create_repricer_exclusion_request_from_dict = CreateRepricerExclusionRequest.from_dict(create_repricer_exclusion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


