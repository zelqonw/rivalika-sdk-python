# rivalika_sdk.ContextApi

All URIs are relative to *https://api.rivalika.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_context**](ContextApi.md#get_context) | **GET** /api/v1/context | Get API principal context


# **get_context**
> DataEnvelope get_context()

Get API principal context

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
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
    api_instance = rivalika_sdk.ContextApi(api_client)

    try:
        # Get API principal context
        api_response = await api_instance.get_context()
        print("The response of ContextApi->get_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContextApi->get_context: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

