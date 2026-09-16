# ListEnvelopePage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | 
**size** | **int** |  | 
**total** | **int** |  | 
**has_more** | **bool** |  | 
**next_cursor** | **UUID** |  | [optional] 

## Example

```python
from rivalika_sdk.models.list_envelope_page import ListEnvelopePage

# TODO update the JSON string below
json = "{}"
# create an instance of ListEnvelopePage from a JSON string
list_envelope_page_instance = ListEnvelopePage.from_json(json)
# print the JSON string representation of the object
print(ListEnvelopePage.to_json())

# convert the object into a dict
list_envelope_page_dict = list_envelope_page_instance.to_dict()
# create an instance of ListEnvelopePage from a dict
list_envelope_page_from_dict = ListEnvelopePage.from_dict(list_envelope_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


