from __future__ import print_function
from swagger_client import api_client
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import json

def getMes(receiver):
   
    api_instance = swagger_client.MessageApi()
    content_type = 'application/vnd.api+json' # str |  (default to application/vnd.api+json)

    try:
        
        api_response = api_instance.retrieveacollectionof_messageobjects0(content_type)
        data = json.loads(str(api_response.data).replace("'","\""))
        i = 0
        messages = []
        while i<len(data):
            s = data[i]['attributes']['receiver']
            id = data[i]['id']
            if s==receiver:
                messages.append(data[i]['attributes'])
                api_response = api_instance.delete_messagefrom_message0(id,content_type)
            i+=1
        return messages
    except ApiException as e:
        print("Exception when calling MessageApi->create_message0: %s\n" % e)
