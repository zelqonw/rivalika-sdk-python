# rivalika_sdk.CommercialImportsApi

All URIs are relative to *https://api.rivalika.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_commercial_import**](CommercialImportsApi.md#cancel_commercial_import) | **POST** /api/v1/commercial/imports/{import_id}/cancel | Cancel a commercial import
[**create_commercial_import**](CommercialImportsApi.md#create_commercial_import) | **POST** /api/v1/commercial/imports | Create a commercial import
[**get_commercial_import**](CommercialImportsApi.md#get_commercial_import) | **GET** /api/v1/commercial/imports/{importId} | Get a commercial import
[**list_commercial_imports**](CommercialImportsApi.md#list_commercial_imports) | **GET** /api/v1/commercial/imports | List commercial imports
[**prepare_commercial_import_upload**](CommercialImportsApi.md#prepare_commercial_import_upload) | **POST** /api/v1/commercial/imports/prepare-upload | Prepare a commercial import upload


# **cancel_commercial_import**
> DataEnvelope cancel_commercial_import(idempotency_key, import_id)

Cancel a commercial import

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
    api_instance = rivalika_sdk.CommercialImportsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    import_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Cancel a commercial import
        api_response = await api_instance.cancel_commercial_import(idempotency_key, import_id)
        print("The response of CommercialImportsApi->cancel_commercial_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialImportsApi->cancel_commercial_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **import_id** | **UUID**|  | 

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

# **create_commercial_import**
> AcceptedEnvelope create_commercial_import(idempotency_key, create_commercial_import_request)

Create a commercial import

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.accepted_envelope import AcceptedEnvelope
from rivalika_sdk.models.create_commercial_import_request import CreateCommercialImportRequest
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
    api_instance = rivalika_sdk.CommercialImportsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    create_commercial_import_request = rivalika_sdk.CreateCommercialImportRequest() # CreateCommercialImportRequest | 

    try:
        # Create a commercial import
        api_response = await api_instance.create_commercial_import(idempotency_key, create_commercial_import_request)
        print("The response of CommercialImportsApi->create_commercial_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialImportsApi->create_commercial_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **create_commercial_import_request** | [**CreateCommercialImportRequest**](CreateCommercialImportRequest.md)|  | 

### Return type

[**AcceptedEnvelope**](AcceptedEnvelope.md)

### Authorization

[RivalikaApiKey](../README.md#RivalikaApiKey)

### HTTP request headers

 - **Content-Type**: application/json
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

# **get_commercial_import**
> CommercialImportDetailEnvelope get_commercial_import(import_id)

Get a commercial import

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.commercial_import_detail_envelope import CommercialImportDetailEnvelope
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
    api_instance = rivalika_sdk.CommercialImportsApi(api_client)
    import_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        # Get a commercial import
        api_response = await api_instance.get_commercial_import(import_id)
        print("The response of CommercialImportsApi->get_commercial_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialImportsApi->get_commercial_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_id** | **UUID**|  | 

### Return type

[**CommercialImportDetailEnvelope**](CommercialImportDetailEnvelope.md)

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
**404** | Resource not found |  -  |
**409** | Conflict or idempotency mismatch |  -  |
**429** | Rate or concurrency limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_commercial_imports**
> ListEnvelope list_commercial_imports(page=page, size=size, search=search, kind=kind, status=status, dry_run=dry_run, sort_by=sort_by, sort_direction=sort_direction)

List commercial imports

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.list_envelope import ListEnvelope
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
    api_instance = rivalika_sdk.CommercialImportsApi(api_client)
    page = 56 # int |  (optional)
    size = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    kind = 'kind_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    dry_run = True # bool |  (optional)
    sort_by = 'sort_by_example' # str |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)

    try:
        # List commercial imports
        api_response = await api_instance.list_commercial_imports(page=page, size=size, search=search, kind=kind, status=status, dry_run=dry_run, sort_by=sort_by, sort_direction=sort_direction)
        print("The response of CommercialImportsApi->list_commercial_imports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialImportsApi->list_commercial_imports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **size** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **dry_run** | **bool**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 

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

# **prepare_commercial_import_upload**
> CommercialImportPreparedUploadEnvelope prepare_commercial_import_upload(idempotency_key, prepare_commercial_import_upload_request)

Prepare a commercial import upload

### Example

* Bearer (Rivalika API key) Authentication (RivalikaApiKey):

```python
import rivalika_sdk
from rivalika_sdk.models.commercial_import_prepared_upload_envelope import CommercialImportPreparedUploadEnvelope
from rivalika_sdk.models.prepare_commercial_import_upload_request import PrepareCommercialImportUploadRequest
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
    api_instance = rivalika_sdk.CommercialImportsApi(api_client)
    idempotency_key = 'idempotency_key_example' # str | Unique key retained for 24 hours. Reusing a key with another payload returns 409.
    prepare_commercial_import_upload_request = rivalika_sdk.PrepareCommercialImportUploadRequest() # PrepareCommercialImportUploadRequest | 

    try:
        # Prepare a commercial import upload
        api_response = await api_instance.prepare_commercial_import_upload(idempotency_key, prepare_commercial_import_upload_request)
        print("The response of CommercialImportsApi->prepare_commercial_import_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommercialImportsApi->prepare_commercial_import_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idempotency_key** | **str**| Unique key retained for 24 hours. Reusing a key with another payload returns 409. | 
 **prepare_commercial_import_upload_request** | [**PrepareCommercialImportUploadRequest**](PrepareCommercialImportUploadRequest.md)|  | 

### Return type

[**CommercialImportPreparedUploadEnvelope**](CommercialImportPreparedUploadEnvelope.md)

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

