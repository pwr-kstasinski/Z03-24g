from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException


def createUser(name,password):
# create an instance of the API class
    api_instance = swagger_client.UserApi()
    content_type = 'application/vnd.api+json' # str |  (default to application/vnd.api+json)
    post_body = swagger_client.UserInst1(
        data={"attributes": {"name": name, 'password': password}, "type": "User"}
    ) # UserInst1 | User attributes
    try:
    # Create Message
        api_response = api_instance.create_user0(content_type, post_body)
        print(api_response)
        return True
    except ApiException as e:
        print("Exception when calling UserApi->create_user0: %s\n" % e)
        
