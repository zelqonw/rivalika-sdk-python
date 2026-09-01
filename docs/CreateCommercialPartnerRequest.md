# CreateCommercialPartnerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**roles** | **List[str]** |  | 
**contact_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from rivalika_sdk.models.create_commercial_partner_request import CreateCommercialPartnerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommercialPartnerRequest from a JSON string
create_commercial_partner_request_instance = CreateCommercialPartnerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCommercialPartnerRequest.to_json())

# convert the object into a dict
create_commercial_partner_request_dict = create_commercial_partner_request_instance.to_dict()
# create an instance of CreateCommercialPartnerRequest from a dict
create_commercial_partner_request_from_dict = CreateCommercialPartnerRequest.from_dict(create_commercial_partner_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


