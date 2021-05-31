import socket
import threading
import time
import json


host="127.0.0.1"
port=5000

class ServerConnection(threading.Thread):
    def __init__(self, server, client, tLock):
        threading.Thread.__init__(self)
        self.server=server
        self.client=client
        self.tLock=tLock
        
    def run(self):
        while True:
            msg = self.client.recv(1024)
            msg=msg.decode()
            print("recieved:",msg)
            self.tLock.acquire()

            self.msgHandler(msg)
            
            self.tLock.release()
        self.client.close()

    def msgHandler(self,data):
        data=json.loads(data)
        #print(data)
        action=data["action"]
        data=data["data"]

        if(action=="login"):
            self.server.api_login_user(self,data)
        if(action=="logout"):
            self.server.api_logout_user(self,data)
        if(action=="register"):
            self.server.api_register_user(self,data)
        if(action=="getUsers"):
            self.server.api_get_users(self,data)
        if(action=="messageHistory"):
            self.server.api_message_history(self,data)
        if(action=="recieve"):
            self.server.api_recieve(self,data)
        if(action=="markRed"):
            self.server.api_mark_red(self,data)
        if(action=="send"):
            self.server.api_send(self,data)
        if(action=="sendEveryone"):
            self.server.api_send_everyone(self,data)
        

    def send(self,data):
        data=bytes(json.dumps(data),"utf-8")
        print("sending:",data)
        self.client.sendall(data)
