# UpdateSupplierOfferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **UUID** |  | [optional] 
**partner_id** | **UUID** |  | [optional] 
**supplier_sku** | **str** |  | [optional] 
**cost_amount** | **float** |  | [optional] 
**currency** | **str** |  | [optional] 
**min_order_quantity** | **int** |  | [optional] 
**lead_time_days** | **int** |  | [optional] 
**valid_from** | **date** |  | [optional] 
**valid_to** | **date** |  | [optional] 
**is_preferred** | **bool** |  | [optional] 

## Example

```python
from rivalika_sdk.models.update_supplier_offer_request import UpdateSupplierOfferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSupplierOfferRequest from a JSON string
update_supplier_offer_request_instance = UpdateSupplierOfferRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSupplierOfferRequest.to_json())

# convert the object into a dict
update_supplier_offer_request_dict = update_supplier_offer_request_instance.to_dict()
# create an instance of UpdateSupplierOfferRequest from a dict
update_supplier_offer_request_from_dict = UpdateSupplierOfferRequest.from_dict(update_supplier_offer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


