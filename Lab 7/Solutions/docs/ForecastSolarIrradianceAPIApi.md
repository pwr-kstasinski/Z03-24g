# openapi_client.ForecastSolarIrradianceAPIApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_energylatlatlonlon_get**](ForecastSolarIrradianceAPIApi.md#forecast_energylatlatlonlon_get) | **GET** /forecast/energy?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns Energy Forecast API response  - Given a single lat/lon. 


# **forecast_energylatlatlonlon_get**
> EnergyObsGroupForecast forecast_energylatlatlonlon_get(lat, lon, key)

Returns Energy Forecast API response  - Given a single lat/lon. 

Retrieve an 8 day forecast relevant to te Energy Sector (degree days, solar radiation, precipitation, wind).

### Example

```python
import time
import openapi_client
from openapi_client.api import forecast_solar_irradiance_api_api
from openapi_client.model.error import Error
from openapi_client.model.energy_obs_group_forecast import EnergyObsGroupForecast
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = forecast_solar_irradiance_api_api.ForecastSolarIrradianceAPIApi(api_client)
    lat = 3.14 # float | Latitude component of location.
    lon = 3.14 # float | Longitude component of location.
    key = "key_example" # str | Your registered API key.
    threshold = 3.14 # float | Temperature threshold to use to calculate degree days (default 18 C)  (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    tp = "hourly" # str | Time period (default: daily) (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns Energy Forecast API response  - Given a single lat/lon. 
        api_response = api_instance.forecast_energylatlatlonlon_get(lat, lon, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ForecastSolarIrradianceAPIApi->forecast_energylatlatlonlon_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns Energy Forecast API response  - Given a single lat/lon. 
        api_response = api_instance.forecast_energylatlatlonlon_get(lat, lon, key, threshold=threshold, units=units, tp=tp, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ForecastSolarIrradianceAPIApi->forecast_energylatlatlonlon_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude component of location. |
 **lon** | **float**| Longitude component of location. |
 **key** | **str**| Your registered API key. |
 **threshold** | **float**| Temperature threshold to use to calculate degree days (default 18 C)  | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **tp** | **str**| Time period (default: daily) | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

### Return type

[**EnergyObsGroupForecast**](EnergyObsGroupForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Energy Data Object. |  -  |
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

