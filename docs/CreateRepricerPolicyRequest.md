# CreateRepricerPolicyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**enabled** | **bool** |  | 
**priority** | **int** |  | 
**scope** | **Dict[str, object]** |  | 
**config** | **Dict[str, object]** |  | 
**guardrails** | **Dict[str, object]** |  | 

## Example

```python
from rivalika_sdk.models.create_repricer_policy_request import CreateRepricerPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRepricerPolicyRequest from a JSON string
create_repricer_policy_request_instance = CreateRepricerPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRepricerPolicyRequest.to_json())

# convert the object into a dict
create_repricer_policy_request_dict = create_repricer_policy_request_instance.to_dict()
# create an instance of CreateRepricerPolicyRequest from a dict
create_repricer_policy_request_from_dict = CreateRepricerPolicyRequest.from_dict(create_repricer_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


