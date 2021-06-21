# openapi_client.A16DayDailyForecastApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_daily_get**](A16DayDailyForecastApi.md#forecast_daily_get) | **GET** /forecast/daily | Returns a daily forecast - Given City and/or State, Country.


# **forecast_daily_get**
> ForecastDay forecast_daily_get(city, key)

Returns a daily forecast - Given City and/or State, Country.

Returns a daily forecast, where each point represents one day (24hr) period. Every point has a datetime string in the format \"YYYY-MM-DD\". One day begins at 00:00 UTC, and ends at 23:59 UTC. Accepts a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate. 

### Example

```python
import time
import openapi_client
from openapi_client.api import a_16_day___daily_forecast_api
from openapi_client.model.error import Error
from openapi_client.model.forecast_day import ForecastDay
from pprint import pprint
# Defining the host is optional and defaults to https://api.weatherbit.io/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.weatherbit.io/v2.0"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = a_16_day___daily_forecast_api.A16DayDailyForecastApi(api_client)
    city = "city_example" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    key = "key_example" # str | Your registered API key.
    state = "state_example" # str | Full name of state. (optional)
    country = "country_example" # str | Country Code (2 letter). (optional)
    days = 3.14 # float | Number of days to return. Default 16. (optional)
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a daily forecast - Given City and/or State, Country.
        api_response = api_instance.forecast_daily_get(city, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling A16DayDailyForecastApi->forecast_daily_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a daily forecast - Given City and/or State, Country.
        api_response = api_instance.forecast_daily_get(city, key, state=state, country=country, days=days, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling A16DayDailyForecastApi->forecast_daily_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR |
 **key** | **str**| Your registered API key. |
 **state** | **str**| Full name of state. | [optional]
 **country** | **str**| Country Code (2 letter). | [optional]
 **days** | **float**| Number of days to return. Default 16. | [optional]
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example - callback&#x3D;func | [optional]

### Return type

[**ForecastDay**](ForecastDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A forecast object. |  -  |
**0** | No Data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

