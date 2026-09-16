# rivalika_sdk.WebhooksApi

All URIs are relative to *https://api.rivalika.md*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_endpoint**](WebhooksApi.md#create_webhook_endpoint) | **POST** /api/v1/webhook-endpoints | Create a webhook endpoint
[**delete_webhook_endpoint**](WebhooksApi.md#delete_webhook_endpoint) | **DELETE** /api/v1/webhook-endpoints/{endpoint_id} | Delete a webhook endpoint
[**get_webhook_delivery**](WebhooksApi.md#get_webhook_delivery) | **GET** /api/v1/webhook-deliveries/{delivery_id} | Get a webhook delivery
[**get_webhook_endpoint**](WebhooksApi.md#get_webhook_endpoint) | **GET** /api/v1/webhook-endpoints/{endpoint_id} | Get a webhook endpoint
[**list_webhook_deliveries**](WebhooksApi.md#list_webhook_deliveries) | **GET** /api/v1/webhook-deliveries | List webhook deliveries
[**list_webhook_endpoints**](WebhooksApi.md#list_webhook_endpoints) | **GET** /api/v1/webhook-endpoints | List webhook endpoints
[**replay_webhook_delivery**](WebhooksApi.md#replay_webhook_delivery) | **POST** /api/v1/webhook-deliveries/{delivery_id}/replay | Replay a webhook delivery
[**rotate_webhook_signing_secret**](WebhooksApi.md#rotate_webhook_signing_secret) | **POST** /api/v1/webhook-endpoints/{endpoint_id}/rotate-secret | Rotate a webhook signing secret
[**test_webhook_endpoint**](WebhooksApi.md#test_webhook_endpoint) | **POST** /api/v1/webhook-endpoints/{endpoint_id}/test | Send a signed test event
[**update_webhook_endpoint**](WebhooksApi.md#update_webhook_endpoint) | **PATCH** /api/v1/webhook-endpoints/{endpoint_id} | Update a webhook endpoint


# **create_webhook_endpoint**
> DataEnvelope create_webhook_endpoint(idempotency_key, create_webhook_endpoint_request)

Create a webhook endpoint

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_webhook_endpoint_request import CreateWebhookEndpointRequest
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_webhook_endpoint_request = rivalika_sdk.CreateWebhookEndpointRequest() # CreateWebhookEndpointRequest | 

    try:
        # Create a webhook endpoint
        api_response = await api_instance.create_webhook_endpoint(idempotency_key, create_webhook_endpoint_request)
        print("The response of WebhooksApi->create_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->create_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_webhook_endpoint_request** | [**CreateWebhookEndpointRequest**](CreateWebhookEndpointRequest.md)|  | 

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook_endpoint**
> DataEnvelope delete_webhook_endpoint(idempotency_key, endpoint_id)

Delete a webhook endpoint

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    endpoint_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Delete a webhook endpoint
        api_response = await api_instance.delete_webhook_endpoint(idempotency_key, endpoint_id)
        print("The response of WebhooksApi->delete_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->delete_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **endpoint_id** | **UUID**|  | 

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

# **get_webhook_delivery**
> DataEnvelope get_webhook_delivery(delivery_id)

Get a webhook delivery

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    delivery_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a webhook delivery
        api_response = await api_instance.get_webhook_delivery(delivery_id)
        print("The response of WebhooksApi->get_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_id** | **UUID**|  | 

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

# **get_webhook_endpoint**
> DataEnvelope get_webhook_endpoint(endpoint_id)

Get a webhook endpoint

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    endpoint_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a webhook endpoint
        api_response = await api_instance.get_webhook_endpoint(endpoint_id)
        print("The response of WebhooksApi->get_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->get_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **UUID**|  | 

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

# **list_webhook_deliveries**
> ListEnvelope list_webhook_deliveries(endpoint_id=endpoint_id)

List webhook deliveries

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.list_envelope import ListEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    endpoint_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID |  (optional)

    try:
        # List webhook deliveries
        api_response = await api_instance.list_webhook_deliveries(endpoint_id=endpoint_id)
        print("The response of WebhooksApi->list_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **UUID**|  | [optional] 

### Return type

[**ListEnvelope**](ListEnvelope.md)

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

# **list_webhook_endpoints**
> ListEnvelope list_webhook_endpoints()

List webhook endpoints

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.list_envelope import ListEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)

    try:
        # List webhook endpoints
        api_response = await api_instance.list_webhook_endpoints()
        print("The response of WebhooksApi->list_webhook_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->list_webhook_endpoints: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListEnvelope**](ListEnvelope.md)

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

# **replay_webhook_delivery**
> AcceptedEnvelope replay_webhook_delivery(idempotency_key, delivery_id)

Replay a webhook delivery

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.accepted_envelope import AcceptedEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    delivery_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Replay a webhook delivery
        api_response = await api_instance.replay_webhook_delivery(idempotency_key, delivery_id)
        print("The response of WebhooksApi->replay_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->replay_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **delivery_id** | **UUID**|  | 

### Return type

[**AcceptedEnvelope**](AcceptedEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_webhook_signing_secret**
> DataEnvelope rotate_webhook_signing_secret(idempotency_key, endpoint_id)

Rotate a webhook signing secret

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    endpoint_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Rotate a webhook signing secret
        api_response = await api_instance.rotate_webhook_signing_secret(idempotency_key, endpoint_id)
        print("The response of WebhooksApi->rotate_webhook_signing_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->rotate_webhook_signing_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **endpoint_id** | **UUID**|  | 

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

# **test_webhook_endpoint**
> AcceptedEnvelope test_webhook_endpoint(idempotency_key, endpoint_id)

Send a signed test event

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.accepted_envelope import AcceptedEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    endpoint_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Send a signed test event
        api_response = await api_instance.test_webhook_endpoint(idempotency_key, endpoint_id)
        print("The response of WebhooksApi->test_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->test_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **endpoint_id** | **UUID**|  | 

### Return type

[**AcceptedEnvelope**](AcceptedEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_endpoint**
> DataEnvelope update_webhook_endpoint(idempotency_key, endpoint_id, create_webhook_endpoint_request)

Update a webhook endpoint

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_webhook_endpoint_request import CreateWebhookEndpointRequest
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rivalika.md
# See configuration.py for a list of all supported configuration parameters.
configuration = rivalika_sdk.Configuration(
    host = "https://api.rivalika.md"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RivalikaApiKey
configuration = rivalika_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with rivalika_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rivalika_sdk.WebhooksApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    endpoint_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    create_webhook_endpoint_request = rivalika_sdk.CreateWebhookEndpointRequest() # CreateWebhookEndpointRequest | 

    try:
        # Update a webhook endpoint
        api_response = await api_instance.update_webhook_endpoint(idempotency_key, endpoint_id, create_webhook_endpoint_request)
        print("The response of WebhooksApi->update_webhook_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->update_webhook_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **endpoint_id** | **UUID**|  | 
 **create_webhook_endpoint_request** | [**CreateWebhookEndpointRequest**](CreateWebhookEndpointRequest.md)|  | 

### Return type

[**DataEnvelope**](DataEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

