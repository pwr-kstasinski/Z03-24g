from __future__ import print_function
from swagger_client import api_client
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

def createMes(sender,receiver,text):
    # create an instance of the API class
    api_instance = swagger_client.MessageApi()
    content_type = 'application/vnd.api+json' # str |  (default to application/vnd.api+json)
    post_body = swagger_client.MessageInst1(
        data={"attributes": {"text": text, "sender": sender, "receiver": receiver}, "type": "Message"}
    ) # MessageInst1 | Message attributes
    try:
        # Create Message
        api_response = api_instance.create_message0(content_type, post_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MessageApi->create_message0: %s\n" % e)
    