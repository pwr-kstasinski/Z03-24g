# openapi_client.BulkDownloadsApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_files_file_get**](BulkDownloadsApi.md#bulk_files_file_get) | **GET** /bulk/files/{file} | Download pre-generated bulk datasets


# **bulk_files_file_get**
> Error bulk_files_file_get(file, key)

Download pre-generated bulk datasets

**(Advanceed/Enterprise plans only)** Downloads bulk data files - OPTIONS: ( current.json.gz - Current observations for cities > 1000 population). Units are Metric (Celcius, m/s, etc).

### Example

```python
import time
import openapi_client
from openapi_client.api import bulk_downloads_api
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bulk_downloads_api.BulkDownloadsApi(api_client)
    file = "file_example" # str | Filename (ie. current.json.gz)
    key = "key_example" # str | Your registered API key.

    # example passing only required values which don't have defaults set
    try:
        # Download pre-generated bulk datasets
        api_response = api_instance.bulk_files_file_get(file, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BulkDownloadsApi->bulk_files_file_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| Filename (ie. current.json.gz) |
 **key** | **str**| Your registered API key. |

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

