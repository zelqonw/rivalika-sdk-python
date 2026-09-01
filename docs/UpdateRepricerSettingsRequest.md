# UpdateRepricerSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 
**schedule** | **Dict[str, object]** |  | [optional] 
**recommendation_lifetime_hours** | **int** |  | [optional] 
**evidence_max_age_hours** | **int** |  | [optional] 
**minimum_in_stock_observations** | **int** |  | [optional] 
**maximum_move_percent** | **str** |  | [optional] 
**batch_apply_limit** | **int** |  | [optional] 
**evidence_cap** | **int** |  | [optional] 
**rounding_mode** | **str** |  | [optional] 
**price_ending** | **str** |  | [optional] 
**low_stock_protection_enabled** | **bool** |  | [optional] 
**low_stock_threshold** | **int** |  | [optional] 
**b2b_tier_mode** | **str** |  | [optional] 
**excluded_store_ids** | **List[UUID]** |  | [optional] 

## Example

```python
from rivalika_sdk.models.update_repricer_settings_request import UpdateRepricerSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRepricerSettingsRequest from a JSON string
update_repricer_settings_request_instance = UpdateRepricerSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRepricerSettingsRequest.to_json())

# convert the object into a dict
update_repricer_settings_request_dict = update_repricer_settings_request_instance.to_dict()
# create an instance of UpdateRepricerSettingsRequest from a dict
update_repricer_settings_request_from_dict = UpdateRepricerSettingsRequest.from_dict(update_repricer_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


