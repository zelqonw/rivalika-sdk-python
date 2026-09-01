# rivalika_sdk.WebhookReceiverApi

All URIs are relative to *https://api.rivalika.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receive_rivalika_webhook**](WebhookReceiverApi.md#receive_rivalika_webhook) | **POST** /event | Receive a signed Rivalika webhook event


# **receive_rivalika_webhook**
> receive_rivalika_webhook(webhook_id, webhook_timestamp, webhook_signature, receive_rivalika_webhook_request)

Receive a signed Rivalika webhook event

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.com
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (Rivalika API key): RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhookReceiverApi(api_client)
    webhook_id = 'webhook_id_example' # str | 
    webhook_timestamp = 'webhook_timestamp_example' # str | 
    webhook_signature = 'webhook_signature_example' # str | 
    receive_rivalika_webhook_request = rivalika_sdk.ReceiveRivalikaWebhookRequest() # ReceiveRivalikaWebhookRequest | 

    try:
        # Receive a signed Rivalika webhook event
        await api_instance.receive_rivalika_webhook(webhook_id, webhook_timestamp, webhook_signature, receive_rivalika_webhook_request)
    except Exception as e:
        print("Exception when calling WebhookReceiverApi->receive_rivalika_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**|  | 
 **webhook_timestamp** | **str**|  | 
 **webhook_signature** | **str**|  | 
 **receive_rivalika_webhook_request** | [**ReceiveRivalikaWebhookRequest**](ReceiveRivalikaWebhookRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

