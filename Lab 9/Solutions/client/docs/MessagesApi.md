# openapi_client.MessagesApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**receive**](MessagesApi.md#receive) | **GET** /download | Receive messages for conversation
[**send**](MessagesApi.md#send) | **POST** /send | Send a message


# **receive**
> [Message] receive(user_id, partner_id)

Receive messages for conversation

### Example

```python
import time
import openapi_client
from openapi_client.api import messages_api
from openapi_client.model.message import Message
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    user_id = 1 # int | User id
    partner_id = 1 # int | Id of conversation partner

    # example passing only required values which don't have defaults set
    try:
        # Receive messages for conversation
        api_response = api_instance.receive(user_id, partner_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->receive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User id |
 **partner_id** | **int**| Id of conversation partner |

### Return type

[**[Message]**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Messages given |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send**
> send(message)

Send a message

### Example

```python
import time
import openapi_client
from openapi_client.api import messages_api
from openapi_client.model.message import Message
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    message = Message(
        sender_id=2,
        receiver_id=1,
        message="Hello there",
        date="2021-05-17 14:49:21.861093",
    ) # Message | Message definition

    # example passing only required values which don't have defaults set
    try:
        # Send a message
        api_instance.send(message)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->send: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | [**Message**](Message.md)| Message definition |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message sent |  -  |
**400** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

