# ReceiveRivalikaWebhookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**created_at** | **datetime** |  | 
**organization_id** | **UUID** |  | 
**data** | **Dict[str, object]** |  | 

## Example

```python
from rivalika_sdk.models.receive_rivalika_webhook_request import ReceiveRivalikaWebhookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiveRivalikaWebhookRequest from a JSON string
receive_rivalika_webhook_request_instance = ReceiveRivalikaWebhookRequest.from_json(json)
# print the JSON string representation of the object
print(ReceiveRivalikaWebhookRequest.to_json())

# convert the object into a dict
receive_rivalika_webhook_request_dict = receive_rivalika_webhook_request_instance.to_dict()
# create an instance of ReceiveRivalikaWebhookRequest from a dict
receive_rivalika_webhook_request_from_dict = ReceiveRivalikaWebhookRequest.from_dict(receive_rivalika_webhook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


