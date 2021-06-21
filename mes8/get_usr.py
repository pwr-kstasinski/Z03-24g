from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import swagger_client.models.user_inst1
import create_usr
import create_msg
import ast
import json


def getUser(user_id):
    api_instance = swagger_client.UserApi()
    content_type = 'application/vnd.api+json' # str |  (default to application/vnd.api+json)
    
    try:
    
        api_response = api_instance.retrieve_userinstance0(user_id,content_type)
        text = api_response.data
        d = ast.literal_eval(text)
        name = d['attributes']['name']
        id = d['id']
        return id,name
    except ApiException as e:
        print("Exception when calling UserApi->create_user0: %s\n" % e)
        return 0

def isCresteU(user_name):
    api_instance = swagger_client.UserApi()
    content_type = 'application/vnd.api+json' # str |  (default to application/vnd.api+json)
    
    
    
    api_response = str(api_instance.retrieveacollectionof_userobjects0(content_type))
    name = "\'"+user_name+"\'"

    if name in api_response:
        return user_name
    else :
        return False
   
