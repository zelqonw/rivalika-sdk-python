# UpdateCommercialProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_product_id** | **UUID** |  | [optional] 
**brand** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**internal_sku** | **str** |  | [optional] 
**external_sku** | **str** |  | [optional] 
**barcode** | **str** |  | [optional] 
**stock_quantity** | **int** |  | [optional] 
**stock_threshold** | **int** |  | [optional] 
**attributes** | **Dict[str, str]** |  | [optional] 

## Example

```python
from rivalika_sdk.models.update_commercial_product_request import UpdateCommercialProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommercialProductRequest from a JSON string
update_commercial_product_request_instance = UpdateCommercialProductRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCommercialProductRequest.to_json())

# convert the object into a dict
update_commercial_product_request_dict = update_commercial_product_request_instance.to_dict()
# create an instance of UpdateCommercialProductRequest from a dict
update_commercial_product_request_from_dict = UpdateCommercialProductRequest.from_dict(update_commercial_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


