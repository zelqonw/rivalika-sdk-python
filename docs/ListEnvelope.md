# ListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[Dict[str, object]]** |  | 
**page** | [**ListEnvelopePage**](ListEnvelopePage.md) |  | 

## Example

```python
from rivalika_sdk.models.list_envelope import ListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ListEnvelope from a JSON string
list_envelope_instance = ListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ListEnvelope.to_json())

# convert the object into a dict
list_envelope_dict = list_envelope_instance.to_dict()
# create an instance of ListEnvelope from a dict
list_envelope_from_dict = ListEnvelope.from_dict(list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


