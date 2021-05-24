# openapi_client.MembershipsApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership0**](MembershipsApi.md#create_membership0) | **POST** /Memberships/ | Create Membership
[**delete_membershipfrom_memberships0**](MembershipsApi.md#delete_membershipfrom_memberships0) | **DELETE** /Memberships/{MembershipId}/ | Delete Membership from Memberships
[**retrieve_membershipinstance0**](MembershipsApi.md#retrieve_membershipinstance0) | **GET** /Memberships/{MembershipId}/ | Retrieve Membership instance
[**retrieveacollectionof_membershipobjects0**](MembershipsApi.md#retrieveacollectionof_membershipobjects0) | **GET** /Memberships/ | Retrieve a collection of Membership objects


# **create_membership0**
> MembershipInst1 create_membership0(post_body)

Create Membership

### Example

* Basic Authentication (BasicAuth):

```python
import time
import openapi_client
from openapi_client.api import memberships_api
from openapi_client.model.jsonapi_error409 import JsonapiError409
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.membership_inst1 import MembershipInst1
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
    api_instance = memberships_api.MembershipsApi(api_client)
    post_body = MembershipInst1(
        data="",
    )  # MembershipInst1 | Membership attributes

    # example passing only required values which don't have defaults set
    try:
        # Create Membership
        api_response = api_instance.create_membership(post_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MembershipsApi->create_membership0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_body** | [**MembershipInst1**](MembershipInst1.md)| Membership attributes |
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**MembershipInst1**](MembershipInst1.md)

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

# **delete_membershipfrom_memberships0**
> MembershipInst1 delete_membershipfrom_memberships0()

Delete Membership from Memberships

### Example

* Basic Authentication (BasicAuth):
```python
import time
import openapi_client
from openapi_client.api import memberships_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.membership_inst1 import MembershipInst1
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
    api_instance = memberships_api.MembershipsApi(api_client)

    # example passing only required values which don't have defaults set
    try:
        # Delete Membership from Memberships
        api_response = api_instance.delete_membershipfrom_memberships0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MembershipsApi->delete_membershipfrom_memberships0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **str**|  | defaults to "jsonapi_id_string"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"

### Return type

[**MembershipInst1**](MembershipInst1.md)

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

# **retrieve_membershipinstance0**
> MembershipInst1 retrieve_membershipinstance0()

Retrieve Membership instance

Retrieve Membership from Memberships

### Example

* Basic Authentication (BasicAuth):
```python
import time
import openapi_client
from openapi_client.api import memberships_api
from openapi_client.model.jsonapi_error500 import JsonapiError500
from openapi_client.model.jsonapi_error405 import JsonapiError405
from openapi_client.model.membership_inst1 import MembershipInst1
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
    api_instance = memberships_api.MembershipsApi(api_client)
    include = "include_example" # str | Membership relationships to include (csv) (optional)
    fields_membership = "user_id,conversation_id,last_download,last_read" # str | Membership fields to include (csv) (optional) if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read"

    # example passing only required values which don't have defaults set
    try:
        # Retrieve Membership instance
        api_response = api_instance.retrieve_membershipinstance0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MembershipsApi->retrieve_membershipinstance0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve Membership instance
        api_response = api_instance.retrieve_membershipinstance0(include=include, fields_membership=fields_membership)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MembershipsApi->retrieve_membershipinstance0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **membership_id** | **str**|  | defaults to "jsonapi_id_string"
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
 **include** | **str**| Membership relationships to include (csv) | [optional]
 **fields_membership** | **str**| Membership fields to include (csv) | [optional] if omitted the server will use the default value of "user_id,conversation_id,last_download,last_read"

### Return type

[**MembershipInst1**](MembershipInst1.md)

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

# **retrieveacollectionof_membershipobjects0**
> MembershipColl1 retrieveacollectionof_membershipobjects0()

Retrieve a collection of Membership objects

Retrieve Membership from Memberships

### Example

* Basic Authentication (BasicAuth):
```python
import time
import openapi_client
from openapi_client.api import memberships_api
from openapi_client.model.membership_coll1 import MembershipColl1
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
    api_instance = memberships_api.MembershipsApi(api_client)
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
        # Retrieve a collection of Membership objects
        api_response = api_instance.retrieveacollectionof_membershipobjects0()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MembershipsApi->retrieveacollectionof_membershipobjects0: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a collection of Membership objects
        api_response = api_instance.retrieveacollectionof_membershipobjects0(include=include, fields_membership=fields_membership, page_offset=page_offset, page_limit=page_limit, sort=sort, filter_user_id=filter_user_id, filter_conversation_id=filter_conversation_id, filter_last_download=filter_last_download, filter_last_read=filter_last_read, filter_id=filter_id, filter=filter)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MembershipsApi->retrieveacollectionof_membershipobjects0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | defaults to "application/vnd.api+json"
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

[**MembershipColl1**](MembershipColl1.md)

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

