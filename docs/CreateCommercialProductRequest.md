# CreateCommercialProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
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
from rivalika_sdk.models.create_commercial_product_request import CreateCommercialProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommercialProductRequest from a JSON string
create_commercial_product_request_instance = CreateCommercialProductRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCommercialProductRequest.to_json())

# convert the object into a dict
create_commercial_product_request_dict = create_commercial_product_request_instance.to_dict()
# create an instance of CreateCommercialProductRequest from a dict
create_commercial_product_request_from_dict = CreateCommercialProductRequest.from_dict(create_commercial_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


