# openapi_client.ConversationsApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_conversation0**](ConversationsApi.md#create_conversation0) | **POST** /Conversations/ | Create Conversation
[**delete_conversationfrom_conversations0**](ConversationsApi.md#delete_conversationfrom_conversations0) | **DELETE** /Conversations/{ConversationId}/ | Delete Conversation from Conversations
[**retrieve_conversationinstance0**](ConversationsApi.md#retrieve_conversationinstance0) | **GET** /Conversations/{ConversationId}/ | Retrieve Conversation instance
[**retrieve_membershipfrommemberships1**](ConversationsApi.md#retrieve_membershipfrommemberships1) | **GET** /Conversations/{ConversationId}/memberships | Retrieve Membership from memberships
[**retrieve_messagefrommessages0**](ConversationsApi.md#retrieve_messagefrommessages0) | **GET** /Conversations/{ConversationId}/messages | Retrieve Message from messages
[**retrieve_userfromusers0**](ConversationsApi.md#retrieve_userfromusers0) | **GET** /Conversations/{ConversationId}/users | Retrieve User from users
[**retrieveacollectionof_conversationobjects0**](ConversationsApi.md#retrieveacollectionof_conversationobjects0) | **GET** /Conversations/ | Retrieve a collection of Conversation objects


# **create_conversation0**
> ConversationInst1 create_conversation0(post_body)

Create Conversation

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import conversations_api
from openapi_client.model.jsonapi_error409 import JsonapiError409
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.conversation_inst1 import ConversationInst1
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://localhost:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)
    post_body = ConversationInst1(
        data="",
    )  # ConversationInst1 | Conversation attributes

    # example passing only required values which don't have defaults set
    try:
        # Create Conversation
        api_response = api_instance.create_conversation(post_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->create_conversation0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_body** | [**ConversationInst1**](ConversationInst1.md)| Conversation attributes |
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**ConversationInst1**](ConversationInst1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **delete_conversationfrom_conversations0**
> ConversationInst1 delete_conversationfrom_conversations0()

Delete Conversation from Conversations

### Example

* Basic Authentication (BasicAuth):
```python
import time
import openapi_client
from openapi_client.api import conversations_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.conversation_inst1 import ConversationInst1
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete Conversation from Conversations
        api_response = api_instance.delete_conversationfrom_conversations0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->delete_conversationfrom_conversations0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | defaults to "jsonapi_id_string"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**ConversationInst1**](ConversationInst1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **retrieve_conversationinstance0**
> ConversationInst1 retrieve_conversationinstance0()

Retrieve Conversation instance

Retrieve Conversation from Conversations

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import conversations_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.conversation_inst1 import ConversationInst1
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://localhost:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)
    include = "messages,memberships,users"  # str | Conversation relationships to include (csv) (optional) if omitted the server will use the default value of "messages,memberships,users"
    fields_conversation = "name"  # str | Conversation fields to include (csv) (optional) if omitted the server will use the default value of "name"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Conversation instance
        api_response = api_instance.get_conversation()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieve_conversationinstance0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Conversation instance
        api_response = api_instance.get_conversation(include=include, fields_conversation=fields_conversation)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieve_conversationinstance0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**|  | defaults to "jsonapi_id_string"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| Conversation relationships to include (csv) | [optional] if omitted the server will use the default value of "messages,memberships,users"
 **fields_conversation** | **str**| Conversation fields to include (csv) | [optional] if omitted the server will use the default value of "name"

### Return type

[**ConversationInst1**](ConversationInst1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

# **retrieve_membershipfrommemberships1**
> ConversationMembershipsRelColl retrieve_membershipfrommemberships1()

Retrieve Membership from memberships

Retrieve Membership items from the Conversation memberships \"to-many\" relationship

### Example

* Basic Authentication (BasicAuth):
```python
import time
import openapi_client
from openapi_client.api import conversations_api
from openapi_client.model.conversation_memberships_rel_coll import ConversationMembershipsRelColl
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)
    include = "include_example" # str | Membership relationships to include (csv) (optional)
    fields_membership = "user_id,conversation_id,last_download,last_read" # str | Membership fields to include (csv) (optional) if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read"
    page_offset = 0 # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10 # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "user_id,conversation_id,last_download,last_read,id" # str | Sort order (optional) if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read,id"
    filter_user_id = "filter[user_id]_example" # str | user_id attribute filter (csv) (optional)
    filter_conversation_id = "filter[conversation_id]_example" # str | conversation_id attribute filter (csv) (optional)
    filter_last_download = "filter[last_download]_example" # str | last_download attribute filter (csv) (optional)
    filter_last_read = "filter[last_read]_example" # str | last_read attribute filter (csv) (optional)
    filter_id = "filter[id]_example" # str | id attribute filter (csv) (optional)
    filter = "filter_example" # str | Custom Membership filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Membership from memberships
        api_response = api_instance.retrieve_membershipfrommemberships1()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieve_membershipfrommemberships1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Membership from memberships
        api_response = api_instance.retrieve_membershipfrommemberships1(include=include, fields_membership=fields_membership, page_offset=page_offset, page_limit=page_limit, sort=sort, filter_user_id=filter_user_id, filter_conversation_id=filter_conversation_id, filter_last_download=filter_last_download, filter_last_read=filter_last_read, filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieve_membershipfrommemberships1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation item | defaults to "jsonapi_id_string"
 **include** | **str**| Membership relationships to include (csv) | [optional]
 **fields_membership** | **str**| Membership fields to include (csv) | [optional] if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read"
 **page_offset** | **int**| Page offset | [optional] if omitted the server will use the default value of 0
 **page_limit** | **int**| Max number of items | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read,id"
 **filter_user_id** | **str**| user_id attribute filter (csv) | [optional]
 **filter_conversation_id** | **str**| conversation_id attribute filter (csv) | [optional]
 **filter_last_download** | **str**| last_download attribute filter (csv) | [optional]
 **filter_last_read** | **str**| last_read attribute filter (csv) | [optional]
 **filter_id** | **str**| id attribute filter (csv) | [optional]
 **filter** | **str**| Custom Membership filter | [optional]

### Return type

[**ConversationMembershipsRelColl**](ConversationMembershipsRelColl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |
**405** | Specified method is invalid for this resource |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_messagefrommessages0**
> ConversationMessagesRelColl retrieve_messagefrommessages0()

Retrieve Message from messages

Retrieve Message items from the Conversation messages \"to-many\" relationship

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import conversations_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.conversation_messages_rel_coll import ConversationMessagesRelColl
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://localhost:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)
    include = "include_example"  # str | Message relationships to include (csv) (optional)
    fields_message = "content,send_date,user_id,conversation_id"  # str | Message fields to include (csv) (optional) if omitted the server will use the default value of "content,send_date,user_id,conversation_id"
    page_offset = 0  # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10  # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "content,send_date,user_id,conversation_id,id"  # str | Sort order (optional) if omitted the server will use the default value of "content,send_date,user_id,conversation_id,id"
    filter_content = "filter[content]_example"  # str | content attribute filter (csv) (optional)
    filter_send_date = "filter[send_date]_example"  # str | send_date attribute filter (csv) (optional)
    filter_user_id = "filter[user_id]_example"  # str | user_id attribute filter (csv) (optional)
    filter_conversation_id = "filter[conversation_id]_example"  # str | conversation_id attribute filter (csv) (optional)
    filter_id = "filter[id]_example"  # str | id attribute filter (csv) (optional)
    filter = "filter_example"  # str | Custom Message filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Message from messages
        api_response = api_instance.get_messages()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->get_messages: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Message from messages
        api_response = api_instance.get_messages(include=include, fields_message=fields_message,
                                                 page_offset=page_offset, page_limit=page_limit, sort=sort,
                                                 filter_content=filter_content, filter_send_date=filter_send_date,
                                                 filter_user_id=filter_user_id,
                                                 filter_conversation_id=filter_conversation_id, filter_id=filter_id,
                                                 filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->get_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation item | defaults to "jsonapi_id_string"
 **include** | **str**| Message relationships to include (csv) | [optional]
 **fields_message** | **str**| Message fields to include (csv) | [optional] if omitted the server will use the default value of "content,send_date,user_id,conversation_id"
 **page_offset** | **int**| Page offset | [optional] if omitted the server will use the default value of 0
 **page_limit** | **int**| Max number of items | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "content,send_date,user_id,conversation_id,id"
 **filter_content** | **str**| content attribute filter (csv) | [optional]
 **filter_send_date** | **str**| send_date attribute filter (csv) | [optional]
 **filter_user_id** | **str**| user_id attribute filter (csv) | [optional]
 **filter_conversation_id** | **str**| conversation_id attribute filter (csv) | [optional]
 **filter_id** | **str**| id attribute filter (csv) | [optional]
 **filter** | **str**| Custom Message filter | [optional]

### Return type

[**ConversationMessagesRelColl**](ConversationMessagesRelColl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |
**405** | Specified method is invalid for this resource |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_userfromusers0**
> ConversationUsersRelColl retrieve_userfromusers0()

Retrieve User from users

Retrieve User items from the Conversation users \"to-many\" relationship

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import conversations_api
from openapi_client.model.conversation_users_rel_coll import ConversationUsersRelColl
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://localhost:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)
    include = "memberships,conversations"  # str | User relationships to include (csv) (optional) if omitted the server will use the default value of "memberships,conversations"
    fields_user = "last_active,name,password"  # str | User fields to include (csv) (optional) if omitted the server will use the default value of "last_active,name,password"
    page_offset = 0  # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10  # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "last_active,name,password,id"  # str | Sort order (optional) if omitted the server will use the default value of "last_active,name,password,id"
    filter_last_active = "filter[last_active]_example"  # str | last_active attribute filter (csv) (optional)
    filter_name = "filter[name]_example"  # str | name attribute filter (csv) (optional)
    filter_password = "filter[password]_example"  # str | password attribute filter (csv) (optional)
    filter_id = "filter[id]_example"  # str | id attribute filter (csv) (optional)
    filter = "filter_example"  # str | Custom User filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve User from users
        api_response = api_instance.get_users()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieve_userfromusers0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve User from users
        api_response = api_instance.get_users(include=include, fields_user=fields_user, page_offset=page_offset,
                                              page_limit=page_limit, sort=sort, filter_last_active=filter_last_active,
                                              filter_name=filter_name, filter_password=filter_password,
                                              filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieve_userfromusers0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conversation_id** | **str**| Conversation item | defaults to "jsonapi_id_string"
 **include** | **str**| User relationships to include (csv) | [optional] if omitted the server will use the default value of "memberships,conversations"
 **fields_user** | **str**| User fields to include (csv) | [optional] if omitted the server will use the default value of "last_active,name,password"
 **page_offset** | **int**| Page offset | [optional] if omitted the server will use the default value of 0
 **page_limit** | **int**| Max number of items | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "last_active,name,password,id"
 **filter_last_active** | **str**| last_active attribute filter (csv) | [optional]
 **filter_name** | **str**| name attribute filter (csv) | [optional]
 **filter_password** | **str**| password attribute filter (csv) | [optional]
 **filter_id** | **str**| id attribute filter (csv) | [optional]
 **filter** | **str**| Custom User filter | [optional]

### Return type

[**ConversationUsersRelColl**](ConversationUsersRelColl.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request fulfilled, document follows |  -  |
**400** | Bad request syntax or unsupported method |  -  |
**404** | Nothing matches the given URI |  -  |
**405** | Specified method is invalid for this resource |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieveacollectionof_conversationobjects0**
> ConversationColl1 retrieveacollectionof_conversationobjects0()

Retrieve a collection of Conversation objects

Retrieve Conversation from Conversations

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import conversations_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
from openapi_client.model.conversation_coll1 import ConversationColl1
from openapi_client.model.jsonapi_error400 import JsonapiError400
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://localhost:5000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = openapi_client.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = conversations_api.ConversationsApi(api_client)
    include = "messages,memberships,users"  # str | Conversation relationships to include (csv) (optional) if omitted the server will use the default value of "messages,memberships,users"
    fields_conversation = "name"  # str | Conversation fields to include (csv) (optional) if omitted the server will use the default value of "name"
    page_offset = 0  # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10  # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "name,id"  # str | Sort order (optional) if omitted the server will use the default value of "name,id"
    filter_name = "filter[name]_example"  # str | name attribute filter (csv) (optional)
    filter_id = "filter[id]_example"  # str | id attribute filter (csv) (optional)
    filter = "filter_example"  # str | Custom Conversation filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a collection of Conversation objects
        api_response = api_instance.get_conversations()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieveacollectionof_conversationobjects0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a collection of Conversation objects
        api_response = api_instance.get_conversations(include=include, fields_conversation=fields_conversation,
                                                      page_offset=page_offset, page_limit=page_limit, sort=sort,
                                                      filter_name=filter_name, filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ConversationsApi->retrieveacollectionof_conversationobjects0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| Conversation relationships to include (csv) | [optional] if omitted the server will use the default value of "messages,memberships,users"
 **fields_conversation** | **str**| Conversation fields to include (csv) | [optional] if omitted the server will use the default value of "name"
 **page_offset** | **int**| Page offset | [optional] if omitted the server will use the default value of 0
 **page_limit** | **int**| Max number of items | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "name,id"
 **filter_name** | **str**| name attribute filter (csv) | [optional]
 **filter_id** | **str**| id attribute filter (csv) | [optional]
 **filter** | **str**| Custom Conversation filter | [optional]

### Return type

[**ConversationColl1**](ConversationColl1.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

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

