# openapi_client.UsersApi

All URIs are relative to *http://127.0.0.1:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user0**](UsersApi.md#create_user0) | **POST** /Users/ | Create User
[**delete_userfrom_users0**](UsersApi.md#delete_userfrom_users0) | **DELETE** /Users/{UserId}/ | Delete User from Users
[**retrieve_messagefromincomingmessages0**](UsersApi.md#retrieve_messagefromincomingmessages0) | **GET** /Users/{UserId}/incoming_messages | Retrieve Message from incoming_messages
[**retrieve_userinstance0**](UsersApi.md#retrieve_userinstance0) | **GET** /Users/{UserId}/ | Retrieve User instance
[**retrieveacollectionof_userobjects0**](UsersApi.md#retrieveacollectionof_userobjects0) | **GET** /Users/ | Retrieve a collection of User objects


# **create_user0**
> UserInst1 create_user0(post_body)

Create User

### Example

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

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://127.0.0.1:5000"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    post_body = UserInst1(
        data="",
    )  # UserInst1 | User attributes

    # example passing only required values which don't have defaults set
    try:
        # Create User
        api_response = api_instance.create_user(post_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->create_user0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_body** | [**UserInst1**](UserInst1.md)| User attributes |
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**UserInst1**](UserInst1.md)

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

# **delete_userfrom_users0**
> UserInst1 delete_userfrom_users0()

Delete User from Users

### Example

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
# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
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
 **user_id** | **str**|  | defaults to "aa7aa833-dac6-40ba-8de7-28eb3b1dfc51"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**UserInst1**](UserInst1.md)

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

# **retrieve_messagefromincomingmessages0**
> UserIncomingMessagesRelColl retrieve_messagefromincomingmessages0()

Retrieve Message from incoming_messages

Retrieve Message items from the User incoming_messages \"to-many\" relationship

### Example

```python
import time
import openapi_client
from openapi_client.api import users_api
from openapi_client.model.user_incoming_messages_rel_coll import UserIncomingMessagesRelColl
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.jsonapi_error404 import JsonapiError404
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
    api_instance = users_api.UsersApi(api_client)
    include = "include_example"  # str | Message relationships to include (csv) (optional)
    fields_message = "content,from_user_id,to_user_id"  # str | Message fields to include (csv) (optional) if omitted the server will use the default value of "content,from_user_id,to_user_id"
    page_offset = 0  # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10  # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "content,from_user_id,to_user_id,id"  # str | Sort order (optional) if omitted the server will use the default value of "content,from_user_id,to_user_id,id"
    filter_content = "filter[content]_example"  # str | content attribute filter (csv) (optional)
    filter_from_user_id = "filter[from_user_id]_example"  # str | from_user_id attribute filter (csv) (optional)
    filter_to_user_id = "filter[to_user_id]_example"  # str | to_user_id attribute filter (csv) (optional)
    filter_id = "filter[id]_example"  # str | id attribute filter (csv) (optional)
    filter = "filter_example"  # str | Custom Message filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Message from incoming_messages
        api_response = api_instance.get_incoming_messages()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->retrieve_messagefromincomingmessages0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Message from incoming_messages
        api_response = api_instance.get_incoming_messages(include=include, fields_message=fields_message,
                                                          page_offset=page_offset, page_limit=page_limit, sort=sort,
                                                          filter_content=filter_content,
                                                          filter_from_user_id=filter_from_user_id,
                                                          filter_to_user_id=filter_to_user_id, filter_id=filter_id,
                                                          filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->retrieve_messagefromincomingmessages0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User item | defaults to "aa7aa833-dac6-40ba-8de7-28eb3b1dfc51"
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

[**UserIncomingMessagesRelColl**](UserIncomingMessagesRelColl.md)

### Authorization

No authorization required

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
# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://127.0.0.1:5000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    include = "incoming_messages" # str | User relationships to include (csv) (optional) if omitted the server will use the default value of "incoming_messages"
    fields_user = "name" # str | User fields to include (csv) (optional) if omitted the server will use the default value of "name"

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
 **user_id** | **str**|  | defaults to "aa7aa833-dac6-40ba-8de7-28eb3b1dfc51"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| User relationships to include (csv) | [optional] if omitted the server will use the default value of "incoming_messages"
 **fields_user** | **str**| User fields to include (csv) | [optional] if omitted the server will use the default value of "name"

### Return type

[**UserInst1**](UserInst1.md)

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

# **retrieveacollectionof_userobjects0**
> UserColl1 retrieveacollectionof_userobjects0()

Retrieve a collection of User objects

Retrieve User from Users

### Example

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

# Defining the host is optional and defaults to http://127.0.0.1:5000
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://127.0.0.1:5000"
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = users_api.UsersApi(api_client)
    include = "incoming_messages"  # str | User relationships to include (csv) (optional) if omitted the server will use the default value of "incoming_messages"
    fields_user = "name"  # str | User fields to include (csv) (optional) if omitted the server will use the default value of "name"
    page_offset = 0  # int | Page offset (optional) if omitted the server will use the default value of 0
    page_limit = 10  # int | Max number of items (optional) if omitted the server will use the default value of 10
    sort = "name,id"  # str | Sort order (optional) if omitted the server will use the default value of "name,id"
    filter_name = "filter[name]_example"  # str | name attribute filter (csv) (optional)
    filter_id = "filter[id]_example"  # str | id attribute filter (csv) (optional)
    filter = "filter_example"  # str | Custom User filter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a collection of User objects
        api_response = api_instance.get_all_users()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->retrieveacollectionof_userobjects0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a collection of User objects
        api_response = api_instance.get_all_users(include=include, fields_user=fields_user, page_offset=page_offset,
                                                  page_limit=page_limit, sort=sort, filter_name=filter_name,
                                                  filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersApi->retrieveacollectionof_userobjects0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| User relationships to include (csv) | [optional] if omitted the server will use the default value of "incoming_messages"
 **fields_user** | **str**| User fields to include (csv) | [optional] if omitted the server will use the default value of "name"
 **page_offset** | **int**| Page offset | [optional] if omitted the server will use the default value of 0
 **page_limit** | **int**| Max number of items | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "name,id"
 **filter_name** | **str**| name attribute filter (csv) | [optional]
 **filter_id** | **str**| id attribute filter (csv) | [optional]
 **filter** | **str**| Custom User filter | [optional]

### Return type

[**UserColl1**](UserColl1.md)

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

