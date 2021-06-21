# openapi_client.CurrentWeatherDataApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentcity_idcity_id_get**](CurrentWeatherDataApi.md#currentcity_idcity_id_get) | **GET** /current?city_id&#x3D;{city_id} | Returns a current observation by city id.


# **currentcity_idcity_id_get**
> CurrentObsGroup currentcity_idcity_id_get(city_id, key)

Returns a current observation by city id.

Returns current weather observation - Given a City ID. 

### Example

```python
import time
import openapi_client
from openapi_client.api import current_weather_data_api
from openapi_client.model.error import Error
from openapi_client.model.current_obs_group import CurrentObsGroup
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = current_weather_data_api.CurrentWeatherDataApi(api_client)
    city_id = "city_id_example" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    key = "key_example" # str | Your registered API key.
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    include = "minutely" # str | Include 1 hour - minutely forecast in the response (optional) if omitted the server will use the default value of "minutely"
    marine = "t" # str | Marine stations only (buoys, oil platforms, etc) (optional) if omitted the server will use the default value of "t"
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback - Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a current observation by city id.
        api_response = api_instance.currentcity_idcity_id_get(city_id, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentcity_idcity_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a current observation by city id.
        api_response = api_instance.currentcity_idcity_id_get(city_id, key, units=units, include=include, marine=marine, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentcity_idcity_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city_id** | **str**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR |
 **key** | **str**| Your registered API key. |
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **include** | **str**| Include 1 hour - minutely forecast in the response | [optional] if omitted the server will use the default value of "minutely"
 **marine** | **str**| Marine stations only (buoys, oil platforms, etc) | [optional] if omitted the server will use the default value of "t"
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback - Example - callback&#x3D;func | [optional]

### Return type

[**CurrentObsGroup**](CurrentObsGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An Observation Group object. |  -  |
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

