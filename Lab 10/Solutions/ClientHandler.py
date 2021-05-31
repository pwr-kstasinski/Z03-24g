import socket
import threading
import time
import json


host="127.0.0.1"
port=5000

class ClientHandler(threading.Thread):
    def __init__(self, gui,tLock):
        threading.Thread.__init__(self)
        self.gui=gui
        self.tLock=tLock
        self.sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sc.connect((host,port))
        self.active=True

    def run(self):
        while self.active:
            msg = self.sc.recv(1024)
            msg=msg.decode()
            print("recieved:",msg)
            self.tLock.acquire()

            self.msgHandler(msg)

            self.tLock.release()
        self.sc.close()

    def msgHandler(self,data):
        data=json.loads(data)
        #print(data)
        action=data["action"]
        data=data["data"]

        if(action=="login"):
            self.gui.loginUser(data)
        if(action=="logout"):
            self.gui.logoutUser(data)
        if(action=="register"):
            self.gui.registerUser(data)
        if(action=="getUsers"):
            self.gui.updateUserList(data)
        if(action=="recieve"):
            self.gui.recieveMessage(data)
        """if(action=="send"):
            self.gui.api_send(self,data)
        if(action=="sendEveryone"):
            self.gui.api_send_everyone(self,data)"""
    
    def send(self,data):
        data=bytes(json.dumps(data),"utf-8")
        print("sending:",data)
        self.sc.sendall(data)

    def kill(self):
        lock=threading.Lock()
        lock.acquire()
        self.active=False
        lock.release()
