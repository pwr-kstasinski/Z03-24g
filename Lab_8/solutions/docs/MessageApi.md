# openapi_client.MessageApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_username_get**](MessageApi.md#get_username_get) | **GET** /get/{username} | receiving messages for a specific user
[**send_receiver_username_message_post**](MessageApi.md#send_receiver_username_message_post) | **POST** /send/{receiver_username}/{message} | sending a message to a specific user


# **get_username_get**
> InlineResponse200 get_username_get(username)

receiving messages for a specific user

### Example

```python
import time
import openapi_client
from openapi_client.api import message_api
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
    api_instance = message_api.MessageApi(api_client)
    username = "username_example" # str | Username of chatapp user

    # example passing only required values which don't have defaults set
    try:
        # receiving messages for a specific user
        api_response = api_instance.get_username_get(username)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessageApi->get_username_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| Username of chatapp user |

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | There&#39;s no messages for specific user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_receiver_username_message_post**
> send_receiver_username_message_post(receiver_username, message)

sending a message to a specific user

### Example

```python
import time
import openapi_client
from openapi_client.api import message_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = message_api.MessageApi(api_client)
    receiver_username = "receiver_username_example" # str | Username of message receiver
    message = "message_example" # str | Message to send

    # example passing only required values which don't have defaults set
    try:
        # sending a message to a specific user
        api_instance.send_receiver_username_message_post(receiver_username, message)
    except openapi_client.ApiException as e:
        print("Exception when calling MessageApi->send_receiver_username_message_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receiver_username** | **str**| Username of message receiver |
 **message** | **str**| Message to send |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

