# openapi_client.AlertsApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertslatlatlonlon_get**](AlertsApi.md#alertslatlatlonlon_get) | **GET** /alerts?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.


# **alertslatlatlonlon_get**
> WeatherAlert alertslatlatlonlon_get(lat, lon, key)

Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.

Returns severe weather alerts issued by meteorological agencies - given a lat, and a lon.

### Example

```python
import time
import openapi_client
from openapi_client.api import alerts_api
from openapi_client.model.error import Error
from openapi_client.model.weather_alert import WeatherAlert
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = alerts_api.AlertsApi(api_client)
    lat = 3.14 # float | Latitude component of location.
    lon = 3.14 # float | Longitude component of location.
    key = "key_example" # str | Your registered API key.
    param_callback = "callback_example" # str | Wraps return in jsonp callback - Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.
        api_response = api_instance.alertslatlatlonlon_get(lat, lon, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alertslatlatlonlon_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns severe weather alerts issued by meteorological agencies - Given a lat/lon.
        api_response = api_instance.alertslatlatlonlon_get(lat, lon, key, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AlertsApi->alertslatlatlonlon_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude component of location. |
 **lon** | **float**| Longitude component of location. |
 **key** | **str**| Your registered API key. |
 **param_callback** | **str**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional]

### Return type

[**WeatherAlert**](WeatherAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Weather Alert Object. |  -  |
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

