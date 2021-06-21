# openapi_client.DefaultApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logged_get**](DefaultApi.md#logged_get) | **GET** /logged | Endpoint for getting active users
[**login_get**](DefaultApi.md#login_get) | **GET** /login | Endpoint for logging users
[**logout_get**](DefaultApi.md#logout_get) | **GET** /logout | Endpoint for user logout
[**read_put**](DefaultApi.md#read_put) | **PUT** /read | Endpoint for marking messages as read
[**receive_get**](DefaultApi.md#receive_get) | **GET** /receive | Endpoint for receiving messages
[**register_post**](DefaultApi.md#register_post) | **POST** /register | Endpoint for registering users
[**send_post**](DefaultApi.md#send_post) | **POST** /send | Endpoint for sending messages
[**unread_get**](DefaultApi.md#unread_get) | **GET** /unread | Endpoint for getting active users
[**users_get**](DefaultApi.md#users_get) | **GET** /users | Endpoint for getting all users


# **logged_get**
> [str] logged_get()

Endpoint for getting active users

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
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
**200** | Succesfully obtained logged users |  -  |

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
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
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

# **logout_get**
> logout_get(id)

Endpoint for user logout

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for user logout
        api_instance.logout_get(id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->logout_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |

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
**200** | Succesfully logged out |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_put**
> read_put(id)

Endpoint for marking messages as read

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = None # bool, date, datetime, dict, float, int, list, str, none_type | Id of message to mark as read

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for marking messages as read
        api_instance.read_put(id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->read_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **bool, date, datetime, dict, float, int, list, str, none_type**| Id of message to mark as read |

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
**200** | Succesfully marked as read |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_get**
> [InlineResponse200] receive_get(id, fr)

Endpoint for receiving messages

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response200 import InlineResponse200
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | User id
    fr = "fr_example" # str | Other user id

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for receiving messages
        api_response = api_instance.receive_get(id, fr)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->receive_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |
 **fr** | **str**| Other user id |

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
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
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
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
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

# **unread_get**
> str unread_get(fr, id)

Endpoint for getting active users

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    fr = "fr_example" # str | Id of user who sent messages
    id = "id_example" # str | Current user id

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for getting active users
        api_response = api_instance.unread_get(fr, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->unread_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fr** | **str**| Id of user who sent messages |
 **id** | **str**| Current user id |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Number of unread messages in that conversation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> [InlineResponse2001] users_get(id)

Endpoint for getting all users

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.inline_response2001 import InlineResponse2001
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Endpoint for getting all users
        api_response = api_instance.users_get(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->users_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |

### Return type

[**[InlineResponse2001]**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesfully parsed request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

