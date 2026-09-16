# UpdatePriceBookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from rivalika_sdk.models.update_price_book_request import UpdatePriceBookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePriceBookRequest from a JSON string
update_price_book_request_instance = UpdatePriceBookRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePriceBookRequest.to_json())

# convert the object into a dict
update_price_book_request_dict = update_price_book_request_instance.to_dict()
# create an instance of UpdatePriceBookRequest from a dict
update_price_book_request_from_dict = UpdatePriceBookRequest.from_dict(update_price_book_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


