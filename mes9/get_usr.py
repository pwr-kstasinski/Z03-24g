from __future__ import print_function
from re import T
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

def isCresteU(user_name,password):
    api_instance = swagger_client.UserApi()
    content_type = 'application/vnd.api+json' # str |  (default to application/vnd.api+json)
    
    
    
    api_response = str(api_instance.retrieveacollectionof_userobjects0(content_type))
    ver = "\'"+user_name+"\', \'password\': \'"+password+"\'"
    api_response = api_response.replace("\"","")
    api_response = api_response.replace("\n","")
    api_response = api_response.replace("         ","")

    if ver in api_response:
        return True
    else :
        return False
   
def getUsers():
    api_instance = swagger_client.UserApi()
    content_type = 'application/vnd.api+json' # str |  (default to application/vnd.api+json)
    
    try:
    
        api_response = api_instance.retrieveacollectionof_userobjects0(content_type)
        data = json.loads(str(api_response.data).replace("'","\""))
        i = 0
        users = []
        while i<len(data):
            u = data[i]['attributes']['name']
            users.append(u)
            i+=1
        return users
    except ApiException as e:
        print("Exception when calling UserApi->create_user0: %s\n" % e)
        return 0

getUsers()