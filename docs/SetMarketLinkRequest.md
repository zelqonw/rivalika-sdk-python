# SetMarketLinkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_product_id** | **UUID** |  | 

## Example

```python
from rivalika_sdk.models.set_market_link_request import SetMarketLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetMarketLinkRequest from a JSON string
set_market_link_request_instance = SetMarketLinkRequest.from_json(json)
# print the JSON string representation of the object
print(SetMarketLinkRequest.to_json())

# convert the object into a dict
set_market_link_request_dict = set_market_link_request_instance.to_dict()
# create an instance of SetMarketLinkRequest from a dict
set_market_link_request_from_dict = SetMarketLinkRequest.from_dict(set_market_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


