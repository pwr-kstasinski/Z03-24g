# openapi_client.CurrentWeatherDataApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currentcitiescities_get**](CurrentWeatherDataApi.md#currentcitiescities_get) | **GET** /current?cities&#x3D;{cities} | Returns a group of observations given a list of cities
[**currentcity_idcity_id_get**](CurrentWeatherDataApi.md#currentcity_idcity_id_get) | **GET** /current?city_id&#x3D;{city_id} | Returns a current observation by city id.
[**currentcitycitycountrycountry_get**](CurrentWeatherDataApi.md#currentcitycitycountrycountry_get) | **GET** /current?city&#x3D;{city}&amp;country&#x3D;{country} | Returns a Current Observation - Given City and/or State, Country.
[**currentlatlatlonlon_get**](CurrentWeatherDataApi.md#currentlatlatlonlon_get) | **GET** /current?lat&#x3D;{lat}&amp;lon&#x3D;{lon} | Returns a Current Observation - Given a lat/lon.
[**currentpostal_codepostal_code_get**](CurrentWeatherDataApi.md#currentpostal_codepostal_code_get) | **GET** /current?postal_code&#x3D;{postal_code} | Returns a current observation by postal code.
[**currentstationsstations_get**](CurrentWeatherDataApi.md#currentstationsstations_get) | **GET** /current?stations&#x3D;{stations} | Returns a group of observations given a list of stations
[**currentstationstation_get**](CurrentWeatherDataApi.md#currentstationstation_get) | **GET** /current?station&#x3D;{station} | Returns a Current Observation. - Given a station ID.


# **currentcitiescities_get**
> CurrentObsGroup currentcitiescities_get(cities, key)

Returns a group of observations given a list of cities

Returns a group of Current Observations - Given a list of City IDs. 

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
    cities = "cities_example" # str | Comma separated list of City ID's. Example: 4487042, 4494942, 4504871
    key = "key_example" # str | Your registered API key.
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    marine = "t" # str | Marine stations only (buoys, oil platforms, etc) (optional) if omitted the server will use the default value of "t"
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback - Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a group of observations given a list of cities
        api_response = api_instance.currentcitiescities_get(cities, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentcitiescities_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a group of observations given a list of cities
        api_response = api_instance.currentcitiescities_get(cities, key, units=units, marine=marine, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentcitiescities_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cities** | **str**| Comma separated list of City ID&#39;s. Example: 4487042, 4494942, 4504871 |
 **key** | **str**| Your registered API key. |
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
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
    city_id = "city_id_example" # str | City ID. Example: 4487042
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
 **city_id** | **str**| City ID. Example: 4487042 |
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

# **currentcitycitycountrycountry_get**
> CurrentObsGroup currentcitycitycountrycountry_get(city, country, key)

Returns a Current Observation - Given City and/or State, Country.

Returns a Current Observation - Given a city in the format of City,ST or City. The state, and country parameters can be provided to make the search more accurate.

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
    city = "city_example" # str | City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
    country = "country_example" # str | Country Code (2 letter).
    key = "key_example" # str | Your registered API key.
    include = "minutely" # str | Include 1 hour - minutely forecast in the response (optional) if omitted the server will use the default value of "minutely"
    state = "state_example" # str | Full name of state. (optional)
    marine = "t" # str | Marine stations only (buoys, oil platforms, etc) (optional) if omitted the server will use the default value of "t"
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback - Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a Current Observation - Given City and/or State, Country.
        api_response = api_instance.currentcitycitycountrycountry_get(city, country, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentcitycitycountrycountry_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a Current Observation - Given City and/or State, Country.
        api_response = api_instance.currentcitycitycountrycountry_get(city, country, key, include=include, state=state, marine=marine, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentcitycitycountrycountry_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **city** | **str**| City search.. Example - &amp;city&#x3D;Raleigh,NC or &amp;city&#x3D;Berlin,DE or city&#x3D;Paris&amp;country&#x3D;FR |
 **country** | **str**| Country Code (2 letter). |
 **key** | **str**| Your registered API key. |
 **include** | **str**| Include 1 hour - minutely forecast in the response | [optional] if omitted the server will use the default value of "minutely"
 **state** | **str**| Full name of state. | [optional]
 **marine** | **str**| Marine stations only (buoys, oil platforms, etc) | [optional] if omitted the server will use the default value of "t"
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
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

# **currentlatlatlonlon_get**
> CurrentObsGroup currentlatlatlonlon_get(lat, lon, key)

Returns a Current Observation - Given a lat/lon.

Returns a Current Observation - given a lat, and a lon.

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
    lat = 3.14 # float | Latitude component of location.
    lon = 3.14 # float | Longitude component of location.
    key = "key_example" # str | Your registered API key.
    include = "minutely" # str | Include 1 hour - minutely forecast in the response (optional) if omitted the server will use the default value of "minutely"
    marine = "t" # str | Marine stations only (buoys, oil platforms, etc) (optional) if omitted the server will use the default value of "t"
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback - Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a Current Observation - Given a lat/lon.
        api_response = api_instance.currentlatlatlonlon_get(lat, lon, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentlatlatlonlon_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a Current Observation - Given a lat/lon.
        api_response = api_instance.currentlatlatlonlon_get(lat, lon, key, include=include, marine=marine, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentlatlatlonlon_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude component of location. |
 **lon** | **float**| Longitude component of location. |
 **key** | **str**| Your registered API key. |
 **include** | **str**| Include 1 hour - minutely forecast in the response | [optional] if omitted the server will use the default value of "minutely"
 **marine** | **str**| Marine stations only (buoys, oil platforms, etc) | [optional] if omitted the server will use the default value of "t"
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
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

# **currentpostal_codepostal_code_get**
> CurrentObsGroup currentpostal_codepostal_code_get(postal_code, key)

Returns a current observation by postal code.

Returns current weather observation - Given a Postal Code. 

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
    postal_code = "postal_code_example" # str | Postal Code. Example: 28546
    key = "key_example" # str | Your registered API key.
    country = "country_example" # str | Country Code (2 letter). (optional)
    include = "minutely" # str | Include 1 hour - minutely forecast in the response (optional) if omitted the server will use the default value of "minutely"
    marine = "t" # str | Marine stations only (buoys, oil platforms, etc) (optional) if omitted the server will use the default value of "t"
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback - Example - callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a current observation by postal code.
        api_response = api_instance.currentpostal_codepostal_code_get(postal_code, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentpostal_codepostal_code_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a current observation by postal code.
        api_response = api_instance.currentpostal_codepostal_code_get(postal_code, key, country=country, include=include, marine=marine, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentpostal_codepostal_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **postal_code** | **str**| Postal Code. Example: 28546 |
 **key** | **str**| Your registered API key. |
 **country** | **str**| Country Code (2 letter). | [optional]
 **include** | **str**| Include 1 hour - minutely forecast in the response | [optional] if omitted the server will use the default value of "minutely"
 **marine** | **str**| Marine stations only (buoys, oil platforms, etc) | [optional] if omitted the server will use the default value of "t"
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
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

# **currentstationsstations_get**
> CurrentObsGroup currentstationsstations_get(stations, key)

Returns a group of observations given a list of stations

Returns a group of Current Observations - Given a list of Station Call IDs. 

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
    stations = "stations_example" # str | Comma separated list of Station Call ID's. Example: KRDU,KBFI,KVNY
    key = "key_example" # str | Your registered API key.
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a group of observations given a list of stations
        api_response = api_instance.currentstationsstations_get(stations, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentstationsstations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a group of observations given a list of stations
        api_response = api_instance.currentstationsstations_get(stations, key, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentstationsstations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stations** | **str**| Comma separated list of Station Call ID&#39;s. Example: KRDU,KBFI,KVNY |
 **key** | **str**| Your registered API key. |
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

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

# **currentstationstation_get**
> CurrentObsGroup currentstationstation_get(station, key)

Returns a Current Observation. - Given a station ID.

Returns a Current Observation - Given a station ID.

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
    station = "station_example" # str | Station Call ID.
    key = "key_example" # str | Your registered API key.
    include = "minutely" # str | Include 1 hour - minutely forecast in the response (optional) if omitted the server will use the default value of "minutely"
    units = "S" # str | Convert to units. Default Metric See <a target='blank' href='/api/requests'>units field description</a> (optional)
    lang = "ar" # str | Language (Default: English) See <a target='blank' href='/api/requests'>language field description</a> (optional)
    param_callback = "callback_example" # str | Wraps return in jsonp callback. Example: callback=func (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a Current Observation. - Given a station ID.
        api_response = api_instance.currentstationstation_get(station, key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentstationstation_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a Current Observation. - Given a station ID.
        api_response = api_instance.currentstationstation_get(station, key, include=include, units=units, lang=lang, param_callback=param_callback)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->currentstationstation_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **station** | **str**| Station Call ID. |
 **key** | **str**| Your registered API key. |
 **include** | **str**| Include 1 hour - minutely forecast in the response | [optional] if omitted the server will use the default value of "minutely"
 **units** | **str**| Convert to units. Default Metric See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;units field description&lt;/a&gt; | [optional]
 **lang** | **str**| Language (Default: English) See &lt;a target&#x3D;&#39;blank&#39; href&#x3D;&#39;/api/requests&#39;&gt;language field description&lt;/a&gt; | [optional]
 **param_callback** | **str**| Wraps return in jsonp callback. Example: callback&#x3D;func | [optional]

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

