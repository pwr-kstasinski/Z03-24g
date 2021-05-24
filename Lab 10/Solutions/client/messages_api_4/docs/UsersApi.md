# openapi_client.UsersApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user0**](UsersApi.md#create_user0) | **POST** /Users/ | Create User
[**delete_userfrom_users0**](UsersApi.md#delete_userfrom_users0) | **DELETE** /Users/{UserId}/ | Delete User from Users
[**retrieve_conversationfromconversations0**](UsersApi.md#retrieve_conversationfromconversations0) | **GET** /Users/{UserId}/conversations | Retrieve Conversation from conversations
[**retrieve_membershipfrommemberships0**](UsersApi.md#retrieve_membershipfrommemberships0) | **GET** /Users/{UserId}/memberships | Retrieve Membership from memberships
[**retrieve_userinstance0**](UsersApi.md#retrieve_userinstance0) | **GET** /Users/{UserId}/ | Retrieve User instance
[**retrieveacollectionof_userobjects0**](UsersApi.md#retrieveacollectionof_userobjects0) | **GET** /Users/ | Retrieve a collection of User objects


# **create_user0**
> UserInst1 create_user0(post_body)

Create User

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import users_api
from openapi_client.model.jsonapi_error409 import JsonapiError409
from openapi_client.model.user_inst1 import UserInst1
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
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
    api_instance = users_api.UsersApi(api_client)
    post_body = UserInst1(
        data="",
    )  # UserInst | User attributes

    # example passing only required values which don't have defaults set
    try:
        # Create User
        api_response = api_instance.create_user(post_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_body** | [**UserInst1**](UserInst1.md)| User attributes |
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**UserInst1**](UserInst1.md)

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

# **delete_userfrom_users0**
> UserInst1 delete_userfrom_users0()

Delete User from Users

### Example

* Basic Authentication (BasicAuth):
```python
import time
import openapi_client
from openapi_client.api import users_api
from openapi_client.model.user_inst1 import UserInst1
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
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
    api_instance = users_api.UsersApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete User from Users
        api_response = api_instance.delete_userfrom_users0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->delete_userfrom_users0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | defaults to "e9868444-83a6-4013-bb5e-241bb3ad5e39"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**UserInst1**](UserInst1.md)

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

# **retrieve_conversationfromconversations0**
> UserConversationsRelColl retrieve_conversationfromconversations0()

Retrieve Conversation from conversations

Retrieve Conversation items from the User conversations \"to-many\" relationship

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import users_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.user_conversations_rel_coll import UserConversationsRelColl
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
    api_instance = users_api.UsersApi(api_client)
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
        # Retrieve Conversation from conversations
        api_response = api_instance.get_conversations()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_conversations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Conversation from conversations
        api_response = api_instance.get_conversations(include=include, fields_conversation=fields_conversation,
                                                      page_offset=page_offset, page_limit=page_limit, sort=sort,
                                                      filter_name=filter_name, filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_conversations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User item | defaults to "e9868444-83a6-4013-bb5e-241bb3ad5e39"
 **include** | **str**| Conversation relationships to include (csv) | [optional] if omitted the server will use the default value of "messages,memberships,users"
 **fields_conversation** | **str**| Conversation fields to include (csv) | [optional] if omitted the server will use the default value of "name"
 **page_offset** | **int**| Page offset | [optional] if omitted the server will use the default value of 0
 **page_limit** | **int**| Max number of items | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "name,id"
 **filter_name** | **str**| name attribute filter (csv) | [optional]
 **filter_id** | **str**| id attribute filter (csv) | [optional]
 **filter** | **str**| Custom Conversation filter | [optional]

### Return type

[**UserConversationsRelColl**](UserConversationsRelColl.md)

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

# **retrieve_membershipfrommemberships0**
> UserMembershipsRelColl retrieve_membershipfrommemberships0()

Retrieve Membership from memberships

Retrieve Membership items from the User memberships \"to-many\" relationship

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import users_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.user_memberships_rel_coll import UserMembershipsRelColl
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
    api_instance = users_api.UsersApi(api_client)
    include = "include_example"  # str | Membership relationships to include (csv) (optional)
    fields_membership = "user_id,conversation_id,last_download,last_read"  # str | Membership fields to include (csv) (optional) if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read"
    page_offset = 0  # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10  # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "user_id,conversation_id,last_download,last_read,id"  # str | Sort order (optional) if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read,id"
    filter_user_id = "filter[user_id]_example"  # str | user_id attribute filter (csv) (optional)
    filter_conversation_id = "filter[conversation_id]_example"  # str | conversation_id attribute filter (csv) (optional)
    filter_last_download = "filter[last_download]_example"  # str | last_download attribute filter (csv) (optional)
    filter_last_read = "filter[last_read]_example"  # str | last_read attribute filter (csv) (optional)
    filter_id = "filter[id]_example"  # str | id attribute filter (csv) (optional)
    filter = "filter_example"  # str | Custom Membership filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Membership from memberships
        api_response = api_instance.get_memberships()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_memberships: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Membership from memberships
        api_response = api_instance.get_memberships(include=include, fields_membership=fields_membership,
                                                    page_offset=page_offset, page_limit=page_limit, sort=sort,
                                                    filter_user_id=filter_user_id,
                                                    filter_conversation_id=filter_conversation_id,
                                                    filter_last_download=filter_last_download,
                                                    filter_last_read=filter_last_read, filter_id=filter_id,
                                                    filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_memberships: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User item | defaults to "e9868444-83a6-4013-bb5e-241bb3ad5e39"
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

[**UserMembershipsRelColl**](UserMembershipsRelColl.md)

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

# **retrieve_userinstance0**
> UserInst1 retrieve_userinstance0()

Retrieve User instance

Retrieve User from Users

### Example

* Basic Authentication (BasicAuth):
```python
import time
import openapi_client
from openapi_client.api import users_api
from openapi_client.model.user_inst1 import UserInst1
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
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
    api_instance = users_api.UsersApi(api_client)
    include = "memberships,conversations" # str | User relationships to include (csv) (optional) if omitted the server will use the default value of "memberships,conversations"
    fields_user = "last_active,name,password" # str | User fields to include (csv) (optional) if omitted the server will use the default value of "last_active,name,password"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve User instance
        api_response = api_instance.retrieve_userinstance0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->retrieve_userinstance0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve User instance
        api_response = api_instance.retrieve_userinstance0(include=include, fields_user=fields_user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->retrieve_userinstance0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | defaults to "e9868444-83a6-4013-bb5e-241bb3ad5e39"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| User relationships to include (csv) | [optional] if omitted the server will use the default value of "memberships,conversations"
 **fields_user** | **str**| User fields to include (csv) | [optional] if omitted the server will use the default value of "last_active,name,password"

### Return type

[**UserInst1**](UserInst1.md)

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

# **retrieveacollectionof_userobjects0**
> UserColl1 retrieveacollectionof_userobjects0()

Retrieve a collection of User objects

Retrieve User from Users

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import users_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.user_coll1 import UserColl1
from openapi_client.model.jsonapi_error404 import JsonapiError404
from openapi_client.model.jsonapi_error403 import JsonapiError403
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
    api_instance = users_api.UsersApi(api_client)
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
        # Retrieve a collection of User objects
        api_response = api_instance.get_users()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a collection of User objects
        api_response = api_instance.get_users(include=include, fields_user=fields_user, page_offset=page_offset,
                                              page_limit=page_limit, sort=sort, filter_last_active=filter_last_active,
                                              filter_name=filter_name, filter_password=filter_password,
                                              filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
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

[**UserColl1**](UserColl1.md)

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

