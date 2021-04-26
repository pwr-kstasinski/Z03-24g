# openapi_client.CurrentWeatherDataApi

All URIs are relative to *http://api.openweathermap.org/data/2.5*

Method | HTTP request | Description
------------- | ------------- | -------------
[**current_weather_data**](CurrentWeatherDataApi.md#current_weather_data) | **GET** /weather | Call current weather data for one location


# **current_weather_data**
> Model200 current_weather_data()

Call current weather data for one location

Access current weather data for any location on Earth including over 200,000 cities! Current weather is frequently updated based on global models and data from more than 40,000 weather stations.

### Example

* Api Key Authentication (app_id):
```python
import time
import openapi_client
from openapi_client.api import current_weather_data_api
from openapi_client.model.model200 import Model200
from pprint import pprint
# Defining the host is optional and defaults to http://api.openweathermap.org/data/2.5
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.openweathermap.org/data/2.5"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: app_id
configuration.api_key['app_id'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['app_id'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = current_weather_data_api.CurrentWeatherDataApi(api_client)
    q = "q_example" # str | **City name**. *Example: London*. You can call by city name, or by city name and country code. The API responds with a list of results that match a searching word. For the query value, type the city name and optionally the country code divided by comma; use ISO 3166 country codes. (optional)
    id = "id_example" # str | **City ID**. *Example: `2172797`*. You can call by city ID. API responds with exact result. The List of city IDs can be downloaded [here](http://bulk.openweathermap.org/sample/). You can include multiple cities in parameter &mdash; just separate them by commas. The limit of locations is 20. *Note: A single ID counts as a one API call. So, if you have city IDs. it's treated as 3 API calls.* (optional)
    lat = "lat_example" # str | **Latitude**. *Example: 35*. The latitude cordinate of the location of your interest. Must use with `lon`. (optional)
    lon = "lon_example" # str | **Longitude**. *Example: 139*. Longitude cordinate of the location of your interest. Must use with `lat`. (optional)
    zip = "zip_example" # str | **Zip code**. Search by zip code. *Example: 95050,us*. Please note if country is not specified then the search works for USA as a default. (optional)
    units = "imperial" # str | **Units**. *Example: imperial*. Possible values: `standard`, `metric`, and `imperial`. When you do not use units parameter, format is `standard` by default. (optional) if omitted the server will use the default value of "imperial"
    lang = "en" # str | **Language**. *Example: en*. You can use lang parameter to get the output in your language. We support the following languages that you can use with the corresponded lang values: Arabic - `ar`, Bulgarian - `bg`, Catalan - `ca`, Czech - `cz`, German - `de`, Greek - `el`, English - `en`, Persian (Farsi) - `fa`, Finnish - `fi`, French - `fr`, Galician - `gl`, Croatian - `hr`, Hungarian - `hu`, Italian - `it`, Japanese - `ja`, Korean - `kr`, Latvian - `la`, Lithuanian - `lt`, Macedonian - `mk`, Dutch - `nl`, Polish - `pl`, Portuguese - `pt`, Romanian - `ro`, Russian - `ru`, Swedish - `se`, Slovak - `sk`, Slovenian - `sl`, Spanish - `es`, Turkish - `tr`, Ukrainian - `ua`, Vietnamese - `vi`, Chinese Simplified - `zh_cn`, Chinese Traditional - `zh_tw`. (optional) if omitted the server will use the default value of "en"
    mode = "json" # str | **Mode**. *Example: html*. Determines format of response. Possible values are `xml` and `html`. If mode parameter is empty the format is `json` by default. (optional) if omitted the server will use the default value of "json"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Call current weather data for one location
        api_response = api_instance.current_weather_data(q=q, id=id, lat=lat, lon=lon, zip=zip, units=units, lang=lang, mode=mode)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CurrentWeatherDataApi->current_weather_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| **City name**. *Example: London*. You can call by city name, or by city name and country code. The API responds with a list of results that match a searching word. For the query value, type the city name and optionally the country code divided by comma; use ISO 3166 country codes. | [optional]
 **id** | **str**| **City ID**. *Example: &#x60;2172797&#x60;*. You can call by city ID. API responds with exact result. The List of city IDs can be downloaded [here](http://bulk.openweathermap.org/sample/). You can include multiple cities in parameter &amp;mdash; just separate them by commas. The limit of locations is 20. *Note: A single ID counts as a one API call. So, if you have city IDs. it&#39;s treated as 3 API calls.* | [optional]
 **lat** | **str**| **Latitude**. *Example: 35*. The latitude cordinate of the location of your interest. Must use with &#x60;lon&#x60;. | [optional]
 **lon** | **str**| **Longitude**. *Example: 139*. Longitude cordinate of the location of your interest. Must use with &#x60;lat&#x60;. | [optional]
 **zip** | **str**| **Zip code**. Search by zip code. *Example: 95050,us*. Please note if country is not specified then the search works for USA as a default. | [optional]
 **units** | **str**| **Units**. *Example: imperial*. Possible values: &#x60;standard&#x60;, &#x60;metric&#x60;, and &#x60;imperial&#x60;. When you do not use units parameter, format is &#x60;standard&#x60; by default. | [optional] if omitted the server will use the default value of "imperial"
 **lang** | **str**| **Language**. *Example: en*. You can use lang parameter to get the output in your language. We support the following languages that you can use with the corresponded lang values: Arabic - &#x60;ar&#x60;, Bulgarian - &#x60;bg&#x60;, Catalan - &#x60;ca&#x60;, Czech - &#x60;cz&#x60;, German - &#x60;de&#x60;, Greek - &#x60;el&#x60;, English - &#x60;en&#x60;, Persian (Farsi) - &#x60;fa&#x60;, Finnish - &#x60;fi&#x60;, French - &#x60;fr&#x60;, Galician - &#x60;gl&#x60;, Croatian - &#x60;hr&#x60;, Hungarian - &#x60;hu&#x60;, Italian - &#x60;it&#x60;, Japanese - &#x60;ja&#x60;, Korean - &#x60;kr&#x60;, Latvian - &#x60;la&#x60;, Lithuanian - &#x60;lt&#x60;, Macedonian - &#x60;mk&#x60;, Dutch - &#x60;nl&#x60;, Polish - &#x60;pl&#x60;, Portuguese - &#x60;pt&#x60;, Romanian - &#x60;ro&#x60;, Russian - &#x60;ru&#x60;, Swedish - &#x60;se&#x60;, Slovak - &#x60;sk&#x60;, Slovenian - &#x60;sl&#x60;, Spanish - &#x60;es&#x60;, Turkish - &#x60;tr&#x60;, Ukrainian - &#x60;ua&#x60;, Vietnamese - &#x60;vi&#x60;, Chinese Simplified - &#x60;zh_cn&#x60;, Chinese Traditional - &#x60;zh_tw&#x60;. | [optional] if omitted the server will use the default value of "en"
 **mode** | **str**| **Mode**. *Example: html*. Determines format of response. Possible values are &#x60;xml&#x60; and &#x60;html&#x60;. If mode parameter is empty the format is &#x60;json&#x60; by default. | [optional] if omitted the server will use the default value of "json"

### Return type

[**Model200**](Model200.md)

### Authorization

[app_id](../README.md#app_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Not found response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

