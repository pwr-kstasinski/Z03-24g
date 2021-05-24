# openapi_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logged_get**](DefaultApi.md#logged_get) | **GET** /logged | Endpoint for getting active users
[**login_get**](DefaultApi.md#login_get) | **GET** /login | Endpoint for logging users
[**receive_get**](DefaultApi.md#receive_get) | **GET** /receive | Endpoint for receiving messages
[**register_post**](DefaultApi.md#register_post) | **POST** /register | Endpoint for registering users
[**send_post**](DefaultApi.md#send_post) | **POST** /send | Endpoint for sending messages


# **logged_get**
> [str] logged_get()

Endpoint for getting active users

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Endpoint for getting active users
        api_response = api_instance.logged_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->logged_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully logged in |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_get**
> login_get(id, _pass)

Endpoint for logging users

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | User id
    _pass = "pass_example" # str | User password

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for logging users
        api_instance.login_get(id, _pass)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->login_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |
 **_pass** | **str**| User password |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully logged in |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_get**
> [InlineResponse200] receive_get(id)

Endpoint for receiving messages

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for receiving messages
        api_response = api_instance.receive_get(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->receive_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |

### Return type

[**[InlineResponse200]**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Messages given |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_post**
> register_post(id, _pass)

Endpoint for registering users

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | User id
    _pass = "pass_example" # str | User password

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for registering users
        api_instance.register_post(id, _pass)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->register_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |
 **_pass** | **str**| User password |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully registered |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_post**
> send_post(message)

Endpoint for sending messages

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_object import InlineObject
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    message = InlineObject(
        fr="you",
        msg="Hello there",
        to="me",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for sending messages
        api_instance.send_post(message)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->send_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | [**InlineObject**](InlineObject.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message sent |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

