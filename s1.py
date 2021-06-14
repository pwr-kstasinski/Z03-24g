
import datetime
from openapi_client.api.message_api import MessageApi
from openapi_client.api.user_api import UserApi
from openapi_client.api_client import ApiClient, Configuration
from tkinter import *
import socketio
import json
import requests
configuration = Configuration(
    host="http://127.0.0.1:5000/api"
)
sio = socketio.Client()

def signUp(login, password):
    api_instance = UserApi(ApiClient())
    include = 'include_example'  
    fields_user = 'name' 
    varargs = login + " " + password  
    api_response = api_instance.invoke_usersign_up0(include=include, fields_user=fields_user, varargs=varargs)

    if api_response == 'success':
        return True
    return False

def logIn(login, password):
    api_instance = UserApi(ApiClient())
    include = 'include_example'  
    fields_user = 'name' 
    varargs = login + " " + password  
    
    api_response = api_instance.invoke_userlog_in0(include=include, fields_user=fields_user, varargs=varargs)
    
    if api_response == 'success':
        return True
    return False


def logOut(login):
    api_instance = UserApi(ApiClient())
    include = 'include_example'  
    fields_user = 'name' 
    varargs = login 
    api_response = api_instance.invoke_userlog_out0(include=include, fields_user=fields_user, varargs=varargs)

    if api_response == 'success':
        return True
    return False

def sendMessage(sender, receiver, text):
    apiInstance = UserApi(ApiClient())
    include = 'include_example'  # str | Message relationships to include (csv) (optional)
    fields_user = 'name'  # str | User fields to include (csv) (optional) (default to 'name')
    varargs = sender + " " + receiver + " " + text  # str | GetMessagesByUserName arguments (optional)
    UserSendMessages = apiInstance.invoke_usersend_messages0(include=include, fields_user=fields_user, varargs=varargs)
    if UserSendMessages == 'success':
        return True
    return False

def getChat(receiver,sender):
    # Create an instance of the API class
    apiMessageInstance = MessageApi(ApiClient())
    include = 'include_example'  # str | Message relationships to include (csv) (optional)
    fields_message = 'text,receiver,sender,send_time,is_read'  # str | Message fields to include (csv) (optional) (default to 'writer_user,recipient_user,text,send_time')
    varargs = receiver + " " + sender  # str | GetAuthenticationStatus arguments (optional)
    messages = apiMessageInstance.invoke_messageget_messages0(include=include, fields_message=fields_message, varargs=varargs)
    mes = []
    
    for i in range(len(messages['meta']['result'])):
        
            mes.append(messages['meta']['result'][i])
            mes.sort(key=lambda x: x["send_time"])
        
    return mes


def readMes(receiver,sender):
    # Create an instance of the API class
    apiMessageInstance = MessageApi(ApiClient())
    include = 'include_example'  # str | Message relationships to include (csv) (optional)
    fields_message = 'text,receiver,sender,send_time,is_read'  # str | Message fields to include (csv) (optional) (default to 'writer_user,recipient_user,text,send_time')
    varargs = receiver + " " + sender  # str | GetAuthenticationStatus arguments (optional)
    messages = apiMessageInstance.invoke_messageread_message0(include=include, fields_message=fields_message, varargs=varargs)
    mes = []
    
    for i in range(len(messages['meta']['result'])):
        
            mes.append(messages['meta']['result'][i])
            mes.sort(key=lambda x: x["send_time"])
        
    return mes
def GetOnlineUsers():
    api_instance = UserApi(ApiClient())
    content_type="application/vnd.api+json" 
    include = 'include_example'  
    fields_user = 'name' 
    api_response = api_instance.retrieveacollectionof_userobjects0(content_type=content_type, fields_user='name')
    online=[]
    for i in range(len(api_response['data'])):
        id = api_response['data'][i]['id']
        user = api_instance.retrieve_userinstance0(user_id = id, content_type=content_type)
        on = user['data']['attributes']['online']
        name = user['data']['attributes']['name']
        online.append([name,on])

    return online

def getUsers():
    api_instance = UserApi(ApiClient())
    content_type="application/vnd.api+json" 
    include = 'include_example'  
    fields_user = 'name' 
    api_response = api_instance.retrieveacollectionof_userobjects0(content_type=content_type, fields_user='name')
    users=[]
    for i in range(len(api_response['data'])):
        id = api_response['data'][i]['id']
        user = api_instance.retrieve_userinstance0(user_id = id, content_type=content_type)
        password = user['data']['attributes']['password']
        name = user['data']['attributes']['name']
        users.append([name,password])

    return(users)

def getUsersName():
    api_instance = UserApi(ApiClient())
    content_type="application/vnd.api+json" 
    include = 'include_example'  
    fields_user = 'name' 
    api_response = api_instance.retrieveacollectionof_userobjects0(content_type=content_type, fields_user='name')
    users=[]
    for i in range(len(api_response['data'])):
        id = api_response['data'][i]['id']
        user = api_instance.retrieve_userinstance0(user_id = id, content_type=content_type)
        name = user['data']['attributes']['name']
        users.append(name)

    return(users)

def getUnreadMes(receiver,sender):
    # Create an instance of the API class
    apiMessageInstance = MessageApi(ApiClient())
    include = 'include_example'  # str | Message relationships to include (csv) (optional)
    fields_message = 'text,receiver,sender,send_time,is_read'  # str | Message fields to include (csv) (optional) (default to 'writer_user,recipient_user,text,send_time')
    varargs = receiver + " " + sender  # str | GetAuthenticationStatus arguments (optional)
    messages = apiMessageInstance.invoke_messageget_messages0(include=include, fields_message=fields_message, varargs=varargs)
    messages = messages['meta']['result']
    k = 0
    for i in range(len(messages)):
            if messages[i]['sender']== sender:
                if messages[i]['is_read'] == False:
                    k = k+1
    
    
        
    return k

#print(getChat("1","2"))
#GetOnlineUsers()
#signUp("8","888")
#getMes()

#print(getUnreadMes("2","1"))
#print(readMes("5","1"))
sendMessage("3","1","oooooo")