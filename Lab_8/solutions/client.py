from tkinter import END
import eel
import openapi_client.api_client as openapi_client
import openapi_client.api.message_api as openapi_clientM
import tkinter as tk
from pprint import pprint




eel.init("web")

configuration = openapi_client.Configuration(
    host="http://localhost:5000"
)

username = ""
message_text = ""


def getMessages():
    with openapi_client.ApiClient(configuration) as api_client:
        api_instance = openapi_clientM.MessageApi(api_client)
        try:
            listmsg=[]
            api_response = api_instance.get_username_get(username)
            response = api_response.to_dict()
            pprint(api_response)
            for message in response['messages']:
               listmsg.append( message)
            return(listmsg)
        except openapi_client.ApiException as e:
            print("Exception when calling MessageApi->get_username_get: %s\n" % e)


def sendMessage():
    with openapi_client.ApiClient() as api_client:
        api_instance = openapi_clientM.MessageApi(api_client)
        receiver_username = send_to_user
        message_text = message_sent_to
        print(message_text)
        try:
            api_instance.send_receiver_username_message_post(receiver_username, message_text)
            print(receiver_username)
            print(message_text)
        except openapi_client.ApiException as e:
            print("Exception when calling MessageApi->send_receiver_username_message_post: %s\n" % e)

@eel.expose
def send_mail_to_serwer(username_send, adresat ,message_send):
    global username
    username=username_send
    global send_to_user
    send_to_user=adresat
    global message_sent_to
    message_sent_to=message_send
    sendMessage()

@eel.expose
def get_mail_from_serwer(username_get):
    global username
    username=username_get
    global message_get
    message_get=[]
    message_get=getMessages()
    return message_get

eel.start("main.html",size=(770,500))

