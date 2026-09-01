# CreateWebhookEndpointRequestSubscriptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | 
**store_id** | **UUID** |  | 

## Example

```python
from rivalika_sdk.models.create_webhook_endpoint_request_subscriptions_inner import CreateWebhookEndpointRequestSubscriptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhookEndpointRequestSubscriptionsInner from a JSON string
create_webhook_endpoint_request_subscriptions_inner_instance = CreateWebhookEndpointRequestSubscriptionsInner.from_json(json)
# print the JSON string representation of the object
print(CreateWebhookEndpointRequestSubscriptionsInner.to_json())

# convert the object into a dict
create_webhook_endpoint_request_subscriptions_inner_dict = create_webhook_endpoint_request_subscriptions_inner_instance.to_dict()
# create an instance of CreateWebhookEndpointRequestSubscriptionsInner from a dict
create_webhook_endpoint_request_subscriptions_inner_from_dict = CreateWebhookEndpointRequestSubscriptionsInner.from_dict(create_webhook_endpoint_request_subscriptions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


