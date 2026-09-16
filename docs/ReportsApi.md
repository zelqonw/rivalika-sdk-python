# rivalika_sdk.ReportsApi

All URIs are relative to *https://api.rivalika.md*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_report**](ReportsApi.md#create_report) | **POST** /api/v1/reports | Create a report definition
[**create_report_run**](ReportsApi.md#create_report_run) | **POST** /api/v1/reports/{report_id}/runs | Start a report run
[**delete_report**](ReportsApi.md#delete_report) | **DELETE** /api/v1/reports/{report_id} | Retire a report definition and retain its history
[**download_report_run**](ReportsApi.md#download_report_run) | **GET** /api/v1/report-runs/{report_run_id}/download | Download a completed report
[**get_report**](ReportsApi.md#get_report) | **GET** /api/v1/reports/{report_id} | Get a report definition
[**list_report_runs**](ReportsApi.md#list_report_runs) | **GET** /api/v1/reports/{report_id}/runs | List report generation attempts
[**list_reports**](ReportsApi.md#list_reports) | **GET** /api/v1/reports | List report definitions
[**update_report**](ReportsApi.md#update_report) | **PATCH** /api/v1/reports/{report_id} | Update a report definition


# **create_report**
> DataEnvelope create_report(idempotency_key, create_report_request)

Create a report definition

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.create_report_request import CreateReportRequest
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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_report_request = rivalika_sdk.CreateReportRequest() # CreateReportRequest | 

    try:
        # Create a report definition
        api_response = await api_instance.create_report(idempotency_key, create_report_request)
        print("The response of ReportsApi->create_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->create_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_report_request** | [**CreateReportRequest**](CreateReportRequest.md)|  | 

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

# **create_report_run**
> DataEnvelope create_report_run(idempotency_key, report_id)

Start a report run

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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    report_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Start a report run
        api_response = await api_instance.create_report_run(idempotency_key, report_id)
        print("The response of ReportsApi->create_report_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->create_report_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **report_id** | **UUID**|  | 

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
**202** | Accepted |  -  |
**400** | Invalid request |  -  |
**401** | Invalid or expired API key |  -  |
**403** | Missing required scope |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_report**
> DataEnvelope delete_report(idempotency_key, report_id)

Retire a report definition and retain its history

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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    report_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Retire a report definition and retain its history
        api_response = await api_instance.delete_report(idempotency_key, report_id)
        print("The response of ReportsApi->delete_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->delete_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **report_id** | **UUID**|  | 

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

# **download_report_run**
> DataEnvelope download_report_run(report_run_id)

Download a completed report

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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    report_run_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Download a completed report
        api_response = await api_instance.download_report_run(report_run_id)
        print("The response of ReportsApi->download_report_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->download_report_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_run_id** | **UUID**|  | 

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

# **get_report**
> DataEnvelope get_report(report_id)

Get a report definition

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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    report_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a report definition
        api_response = await api_instance.get_report(report_id)
        print("The response of ReportsApi->get_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->get_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **UUID**|  | 

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

# **list_report_runs**
> ListEnvelope list_report_runs(report_id)

List report generation attempts

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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    report_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # List report generation attempts
        api_response = await api_instance.list_report_runs(report_id)
        print("The response of ReportsApi->list_report_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->list_report_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **UUID**|  | 

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

# **list_reports**
> ListEnvelope list_reports(page=page, size=size, search=search, status=status, type=type, is_active=is_active, scheduled=scheduled)

List report definitions

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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    type = 'type_example' # str |  (optional)
    is_active = True # bool |  (optional)
    scheduled = True # bool |  (optional)

    try:
        # List report definitions
        api_response = await api_instance.list_reports(page=page, size=size, search=search, status=status, type=type, is_active=is_active, scheduled=scheduled)
        print("The response of ReportsApi->list_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->list_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **is_active** | **bool**|  | [optional] 
 **scheduled** | **bool**|  | [optional] 

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

# **update_report**
> DataEnvelope update_report(idempotency_key, report_id, update_report_request)

Update a report definition

### Example

* Bearer Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.data_envelope import DataEnvelope
from rivalika_sdk.models.update_report_request import UpdateReportRequest
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
    api_instance = rivalika_sdk.ReportsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    report_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 
    update_report_request = rivalika_sdk.UpdateReportRequest() # UpdateReportRequest | 

    try:
        # Update a report definition
        api_response = await api_instance.update_report(idempotency_key, report_id, update_report_request)
        print("The response of ReportsApi->update_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportsApi->update_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **report_id** | **UUID**|  | 
 **update_report_request** | [**UpdateReportRequest**](UpdateReportRequest.md)|  | 

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

