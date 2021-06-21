import socketio
import asyncio
import time
import openapi_client
from pprint import pprint
from openapi_client.api import default_api
from openapi_client.model.inline_response200 import InlineResponse200
import tkinter as tk
import requests
import json
sio = socketio.Client()
configuration = openapi_client.Configuration(
    host = "http://localhost:5000"
)
user_ID = 0
chat_text = ""
USERS = []
other_user = 0
USERNAME = ""

class User:
    Id = -1
    Name = 'None'
    Status = 'ND'
    Unread = 0

    def __init__(self,Id,Name,Status,Unread):
        self.Id = Id
        self.Name = Name
        self.Status = Status
        self.Unread = Unread

def InitialDraw(root):
    Clear()
    widg = tk.Label(root,text="Wpisz login i hasło")
    widg.configure(bg="deep sky blue")
    widg.pack()
    login_text = tk.Entry(root)
    login_text.configure(bg="sky blue")
    login_text.pack()
    password_text = tk.Entry(root)
    password_text.configure(bg="sky blue")
    password_text.pack()
    widg = tk.Button(root,text="Zaloguj/Zarejestruj",command=lambda: Login(login_text,password_text))
    widg.configure(bg="steel blue")
    widg.pack()

def Login(login,password):
    log = str(login.get())
    psw = str(password.get())
    global USERNAME
    USERNAME = log
    global user_ID
    response = requests.get(f'http://localhost:5000/login/{log}/{psw}')
    data = json.loads(response.text)
    if data["status"] == 1:
        user_ID = data["id"]
        connect_websocket()
        root.title(f"[{USERNAME}]")
        MainDraw(root)
    else:
        user_ID = 0
        InitialDraw(root)  
def connect_websocket():
    sio.connect('http://localhost:5000')
def Clear():
    print("Updating UI")
    for widget in all_children(root):
        widget.destroy()
def all_children(window):
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
def MainDraw(root):
    Clear()
    DrawChat()

    input_field = tk.Entry(root)
    input_field.configure(bg="sky blue")
    input_field.grid(row=11,sticky="WS")
    send_button = tk.Button(root,text="Wyślij",command=lambda: send_message(input_field.get()))
    send_button.configure(bg="steel blue")
    send_button.grid(row=11,sticky="S")
    
    DrawUsers()
def DrawChat():
    if len(USERS) <= 0:
        return
    response = requests.get(f'http://localhost:5000/get_messages/{user_ID}/{USERS[other_user].Id}')
    data = json.loads(response.text)
    x = 0
    for msg in data:
        if user_ID != msg["From"]:
            text = tk.Label(root,text=f'{msg["SendDate"]}:{msg["Content"]}',bg="light steel blue")
            text.grid(row=x,sticky="W")
        else:
            text = tk.Label(root,text=f'{msg["Content"]} :{msg["Displayed"]} {msg["SendDate"]}',bg="light sky blue")
            text.grid(row=x,sticky="E")
        x = x+1
def DrawUsers():
    response = requests.get(f'http://localhost:5000/get_user_list/{user_ID}')
    data = json.loads(response.text)
    UserButton.Count = 0
    USERS.clear()
    for x in data:
        print(x)
    data = sorted(data,key=lambda item:item["Status"],reverse=True)
    for x in data:
        print(x)
    for user in data:
        u = User(user["Id"],user["Name"],user["Status"],user["Unread"])
        USERS.append(u)
        print(f"{len(USERS)} users found")
        UserButton(user["Name"],user["Status"],user["Unread"])
class UserButton:
    Count = 0
    def __init__(self,name,status,unread):
        self.id = UserButton.Count
        self.name = name
        if status==True:
            komunikat="W sieci"
        else:
            komunikat="Poza siecą"
        user_button = tk.Button(root,text=f'{name} {komunikat} {unread}',command=lambda:self.change_focus(self.id))
        user_button.grid(row=self.id,column=2,sticky="e")
        UserButton.Count=UserButton.Count+1
    def change_focus(self,focus):
        global other_user
        other_user = focus
        root.title(f"[{USERNAME}] rozmawia z: {self.name}")
        MainDraw(root)
def send_message(msg):
    requests.get(f'http://localhost:5000/send_message/{user_ID}/{USERS[other_user].Id}/{msg}')
    MainDraw(root)
@sio.event
def update_list():
    MainDraw(root)

def main():
    global root
    root = tk.Tk()
    root["bg"] = "deep sky blue"
    root.geometry("500x300")
    for i in range(2):
        root.columnconfigure(i, weight=1)
    InitialDraw(root)
    root.mainloop()
if __name__ == "__main__":
    main()
    pass

