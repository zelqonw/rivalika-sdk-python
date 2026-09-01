# ApplyRepricerRecommendationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**override_amount** | **str** |  | [optional] 
**override_reason** | **str** |  | [optional] 

## Example

```python
from rivalika_sdk.models.apply_repricer_recommendation_request import ApplyRepricerRecommendationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplyRepricerRecommendationRequest from a JSON string
apply_repricer_recommendation_request_instance = ApplyRepricerRecommendationRequest.from_json(json)
# print the JSON string representation of the object
print(ApplyRepricerRecommendationRequest.to_json())

# convert the object into a dict
apply_repricer_recommendation_request_dict = apply_repricer_recommendation_request_instance.to_dict()
# create an instance of ApplyRepricerRecommendationRequest from a dict
apply_repricer_recommendation_request_from_dict = ApplyRepricerRecommendationRequest.from_dict(apply_repricer_recommendation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


