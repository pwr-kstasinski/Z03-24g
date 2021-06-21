# openapi_client.MessagesApi

All URIs are relative to *http://127.0.0.1:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message0**](MessagesApi.md#create_message0) | **POST** /Messages/ | Create Message
[**delete_messagefrom_messages0**](MessagesApi.md#delete_messagefrom_messages0) | **DELETE** /Messages/{MessageId}/ | Delete Message from Messages
[**retrieve_messageinstance0**](MessagesApi.md#retrieve_messageinstance0) | **GET** /Messages/{MessageId}/ | Retrieve Message instance
[**retrieveacollectionof_messageobjects0**](MessagesApi.md#retrieveacollectionof_messageobjects0) | **GET** /Messages/ | Retrieve a collection of Message objects


# **create_message0**
> MessageInst1 create_message0(post_body)

Create Message

### Example

```python
import time
import openapi_client
from openapi_client.api import messages_api
from openapi_client.model.jsonapi_error409 import JsonapiError409
from openapi_client.model.message_inst1 import MessageInst1
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://127.0.0.1:5000"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    post_body = MessageInst1(
        data="",
    )  # MessageInst1 | Message attributes

    # example passing only required values which don't have defaults set
    try:
        # Create Message
        api_response = api_instance.create_message(post_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->create_message0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_body** | [**MessageInst1**](MessageInst1.md)| Message attributes |
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**MessageInst1**](MessageInst1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**202** | Accepted |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Specified method is invalid for this resource |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_messagefrom_messages0**
> MessageInst1 delete_messagefrom_messages0()

Delete Message from Messages

### Example

```python
import time
import openapi_client
from openapi_client.api import messages_api
from openapi_client.model.message_inst1 import MessageInst1
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://127.0.0.1:5000"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api

    # example passing only required values which don't have defaults set
    try:
        # Delete Message from Messages
        api_response = api_instance.delete_message()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->delete_messagefrom_messages0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | defaults to "1232"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**MessageInst1**](MessageInst1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**202** | Accepted |  -  |
**204** | Request fulfilled, nothing follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Specified method is invalid for this resource |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_messageinstance0**
> MessageInst1 retrieve_messageinstance0()

Retrieve Message instance

Retrieve Message from Messages

### Example

```python
import time
import openapi_client
from openapi_client.api import messages_api
from openapi_client.model.message_inst1 import MessageInst1
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    include = "include_example" # str | Message relationships to include (csv) (optional)
    fields_message = "content,from_user_id,to_user_id" # str | Message fields to include (csv) (optional) if omitted the server will use the default value of "content,from_user_id,to_user_id"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Message instance
        api_response = api_instance.retrieve_messageinstance0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->retrieve_messageinstance0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Message instance
        api_response = api_instance.retrieve_messageinstance0(include=include, fields_message=fields_message)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->retrieve_messageinstance0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | defaults to "1232"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| Message relationships to include (csv) | [optional]
 **fields_message** | **str**| Message fields to include (csv) | [optional] if omitted the server will use the default value of "content,from_user_id,to_user_id"

### Return type

[**MessageInst1**](MessageInst1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Specified method is invalid for this resource |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveacollectionof_messageobjects0**
> MessageColl1 retrieveacollectionof_messageobjects0()

Retrieve a collection of Message objects

Retrieve Message from Messages

### Example

```python
import time
import openapi_client
from openapi_client.api import messages_api
from openapi_client.model.message_coll1 import MessageColl1
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint
# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = messages_api.MessagesApi(api_client)
    include = "include_example" # str | Message relationships to include (csv) (optional)
    fields_message = "content,from_user_id,to_user_id" # str | Message fields to include (csv) (optional) if omitted the server will use the default value of "content,from_user_id,to_user_id"
    page_offset = 0 # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10 # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "content,from_user_id,to_user_id,id" # str | Sort order (optional) if omitted the server will use the default value of "content,from_user_id,to_user_id,id"
    filter_content = "filter[content]_example" # str | content attribute filter (csv) (optional)
    filter_from_user_id = "filter[from_user_id]_example" # str | from_user_id attribute filter (csv) (optional)
    filter_to_user_id = "filter[to_user_id]_example" # str | to_user_id attribute filter (csv) (optional)
    filter_id = "filter[id]_example" # str | id attribute filter (csv) (optional)
    filter = "filter_example" # str | Custom Message filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a collection of Message objects
        api_response = api_instance.retrieveacollectionof_messageobjects0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->retrieveacollectionof_messageobjects0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a collection of Message objects
        api_response = api_instance.retrieveacollectionof_messageobjects0(include=include, fields_message=fields_message, page_offset=page_offset, page_limit=page_limit, sort=sort, filter_content=filter_content, filter_from_user_id=filter_from_user_id, filter_to_user_id=filter_to_user_id, filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MessagesApi->retrieveacollectionof_messageobjects0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| Message relationships to include (csv) | [optional]
 **fields_message** | **str**| Message fields to include (csv) | [optional] if omitted the server will use the default value of "content,from_user_id,to_user_id"
 **page_offset** | **int**| Page offset | [optional] if omitted the server will use the default value of 0
 **page_limit** | **int**| Max number of items | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "content,from_user_id,to_user_id,id"
 **filter_content** | **str**| content attribute filter (csv) | [optional]
 **filter_from_user_id** | **str**| from_user_id attribute filter (csv) | [optional]
 **filter_to_user_id** | **str**| to_user_id attribute filter (csv) | [optional]
 **filter_id** | **str**| id attribute filter (csv) | [optional]
 **filter** | **str**| Custom Message filter | [optional]

### Return type

[**MessageColl1**](MessageColl1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Specified method is invalid for this resource |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

