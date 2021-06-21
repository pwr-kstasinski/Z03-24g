import threading
import time
from tkinter import *
from tkinter import font
from tkinter import ttk
from openapi_client.api.messages_api import MessagesApi
from openapi_client.api.user_api import UserApi
from openapi_client.api.default_api import DefaultApi
from openapi_client.model.message import Message


msgapi = MessagesApi()
userapi = UserApi()
defapi = DefaultApi()
messages = []
USER_REFRESH_DELAY = 3

def createMessage(fr,to,msg):
    return Message(fr=fr,to=to,msg=msg)

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        
        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width = False, 
                             height = False)
        self.login.configure(width = 400,
                             height = 300)
        
        self.pls = Label(self.login, 
                       text = "Please login to continue",
                       justify = CENTER, 
                       font = "Helvetica 14 bold")
        self.pls.place(relheight = 0.15,
                       relx = 0.2, 
                       rely = 0.07)
        
        self.labelName = Label(self.login,
                               text = "Name: ",
                               font = "Helvetica 12")
        self.labelName.place(relheight = 0.2,
                             relx = 0.1, 
                             rely = 0.2)
        
        self.entryName = Entry(self.login, 
                             font = "Helvetica 14")
        self.entryName.place(relwidth = 0.4, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.2)
        self.entryPassword = Entry(self.login, 
                             font = "Helvetica 14")
        self.entryPassword.place(relwidth = 0.4, 
                             relheight = 0.12,
                             relx = 0.35,
                             rely = 0.35)
          
        self.loginButton = Button(self.login,
                         text = "LOGIN", 
                         font = "Helvetica 14 bold", 
                         command = lambda: self.logIn(self.entryName.get(),self.entryPassword.get()))
        self.loginButton.place(relx = 0.3,
                         rely = 0.55)
        
        self.registerButton = Button(self.login,
                         text = "REGISTER", 
                         font = "Helvetica 14 bold", 
                         command = lambda: self.registerIn(self.entryName.get(),self.entryPassword.get()))
        self.registerButton.place(relx = 0.5,
                      rely = 0.55)
        
        self.Window.mainloop()
  
    def registerIn(self, name, passw):
        userapi.register(id=name,_pass=passw)
    
    def logIn(self, name, passw):
        userapi.login(id=name,_pass=passw)

        self.me = name
        self.login.destroy()
        self.layout(name)
          
        rcv = threading.Thread(target=self.receive)
        rcv.start()
  
    def layout(self,name):
        self.Window.deiconify()
        self.Window.title("CHATROOM")
        self.Window.resizable(width = False,
                              height = False)
        self.Window.configure(width = 720,
                              height = 550,
                              bg = "#17202A")
        
        self.labelHead = Label(self.Window,
                             bg = "#17202A", 
                              fg = "#EAECEE",
                              text = self.me ,
                               font = "Helvetica 13 bold",
                               pady = 5)
        self.labelHead.place(relwidth = 1)

        self.line = Label(self.Window,
                          width = 450,
                          bg = "#ABB2B9")
        self.line.place(relwidth = 1,
                        rely = 0.07,
                        relheight = 0.012)
          
        self.textCons = Text(self.Window,
                             width = 20, 
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 14", 
                             padx = 5,
                             pady = 5)
        self.textCons.place(relheight = 0.745,
                            relwidth = 0.7, 
                            rely = 0.08)
        self.userCons = Text(self.Window,
                             width = 20, 
                             height = 2,
                             bg = "#17202A",
                             fg = "#EAECEE",
                             font = "Helvetica 14", 
                             padx = 5,
                             pady = 5)
        self.userCons.place(relheight = 0.745,
                            relwidth = 0.3,
                            relx = 0.7,
                            rely = 0.08)
        
        self.labelBottom = Label(self.Window,
                                 bg = "#ABB2B9",
                                 height = 80)
        self.labelBottom.place(relwidth = 1,
                               rely = 0.825)
          
        self.entryMsg = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
        self.entryMsg.place(relwidth = 0.68,
                            relheight = 0.04,
                            rely = 0.008,
                            relx = 0.08)
        self.entryMsg.focus()

        self.entryTarget = Entry(self.labelBottom,
                              bg = "#2C3E50",
                              fg = "#EAECEE",
                              font = "Helvetica 13")
        self.entryTarget.place(relwidth = 0.56,
                            relheight = 0.025,
                            rely = 0.05,
                            relx = 0.18)

        self.labelTo = Label(self.labelBottom,
                               bg = "#17202A", 
                               fg = "#EAECEE",
                               text = "TO:" ,
                               font = "Helvetica 13 bold",
                               pady = 5)
        self.labelTo.place(relwidth = 0.10,
                            relheight = 0.025,
                            rely = 0.05,
                            relx = 0.04)
        
        self.buttonMsg = Button(self.labelBottom,
                                text = "Send",
                                font = "Helvetica 10 bold", 
                                width = 20,
                                bg = "#ABB2B9",
                                command = lambda : self.sendButton(self.entryMsg.get()))
        self.buttonMsg.place(relx = 0.77,
                             rely = 0.008,
                             relheight = 0.06, 
                             relwidth = 0.22)
          
        self.textCons.config(cursor = "arrow")
        scrollbar = Scrollbar(self.textCons)
        scrollbar.place(relheight = 1,
                        relx = 0.974)
          
        scrollbar.config(command = self.textCons.yview)
          
        self.textCons.config(state = DISABLED)
  
    def addMSG(self,msg):
        self.textCons.config(state = NORMAL)
        self.textCons.insert(END,
                                msg.fr+": "+msg.msg+"\n\n")
            
        self.textCons.config(state = DISABLED)
        self.textCons.see(END)
    
    def sendButton(self, msg):
        self.textCons.config(state = DISABLED)
        target=self.entryTarget.get()
        newmsg=createMessage(self.me,target,msg)
        msgapi.send(newmsg)
        self.addMSG(newmsg)
        self.entryMsg.delete(0, END)
  
    def receive(self):
        ct=0
        while(True):
            #received = defapi.receive(id=self.me)
            received = defapi.receive_get(id=self.me)
            messages.extend(received)
            for x in received:
                self.addMSG(x)
            time.sleep(2)
            ct-=1
            if ct<=0:
                usrs = defapi.logged_get()
                self.textCons.config(state = NORMAL)
                self.userCons.delete('1.0', END)
                for u in usrs:
                    self.userCons.insert(END,u+"\n")
                    self.textCons.config(state = DISABLED)
                    self.textCons.see(END)
                ct = USER_REFRESH_DELAY
                
if __name__ == "__main__":
    g = GUI()