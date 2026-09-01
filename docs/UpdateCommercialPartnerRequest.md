# UpdateCommercialPartnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from rivalika_sdk.models.update_commercial_partner_request import UpdateCommercialPartnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommercialPartnerRequest from a JSON string
update_commercial_partner_request_instance = UpdateCommercialPartnerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCommercialPartnerRequest.to_json())

# convert the object into a dict
update_commercial_partner_request_dict = update_commercial_partner_request_instance.to_dict()
# create an instance of UpdateCommercialPartnerRequest from a dict
update_commercial_partner_request_from_dict = UpdateCommercialPartnerRequest.from_dict(update_commercial_partner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


