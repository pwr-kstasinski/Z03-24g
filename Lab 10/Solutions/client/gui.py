import sys
import asyncio
import socketio
import threading
import json
from datetime import datetime
from tkinter import *
from tkinter import font
from tkinter import ttk
from openapi_client.api.messages_api import MessagesApi
from openapi_client.api.default_api import DefaultApi
from openapi_client.model.message import Message
from scrollable import Scrollable

msgapi = MessagesApi()
defapi = DefaultApi()
sio = socketio.AsyncClient()
to_call_on_sio = None
el = asyncio.new_event_loop()
usrbuttons = {}

@sio.on('any')
async def on_message(data):
    await to_call_on_sio(data)
async def sio_dc():
    print('start dc')
    await sio.disconnect()

def createMessage(fr,to,msg):
    return Message(fr=fr,to=to,msg=msg)

class MessageBox(Frame):
    def __init__(self,parent,pos,msg,sent):
        super().__init__(parent)
        fromLabel = Label(self, 
            text = msg.fr+" @ "+msg.sent[:25]+" "+("\u2173" if msg.read else "..."),
            justify = LEFT if sent else RIGHT,
            fg = "#334411",
            font = "Helvetica 14 bold")
        fromLabel.pack(side=TOP,anchor='e' if sent else 'w')
        textLabel = Label(self, 
            text = msg.msg,
            justify = LEFT, 
            font = "Helvetica 14")
        textLabel.pack(side=BOTTOM,anchor='e' if sent else 'w')
        self.grid(row=pos,sticky=E if sent else W)

class UserButton(Button):
    def __init__(self,parent,pos,uid,active,call):
        super().__init__(parent,
                         text = uid if uid else "ALL", 
                         font = "Helvetica 14 bold" if active else "Helvetica 14 italic", 
                         command = lambda: call(self.uid))
        self.grid(row=pos,sticky=W+N)
        self.uid = uid
        self.active = active
        usrbuttons[uid]=self
    def setUnread(self,n):
        self['text'] = self.uid+" ("+str(n)+")"+("" if self.uid=="ALL" else ("-ACTIVE" if self.active else "-INACTIVE"))

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()
        def on_closing():
            print('closing')
            defapi.logout_get(id=self.me)
            asyncio.get_event_loop().stop()
            if self.me:
                self.Window.destroy()
            sys.exit(0)

        self.Window.protocol("WM_DELETE_WINDOW", on_closing)
        
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
        defapi.register_post(id=name,_pass=passw)
    
    def logIn(self, name, passw):
        defapi.login_get(id=name,_pass=passw)

        self.me = name
        self.login.destroy()
        self.layout(name)
  
    def layout(self,name):
        self.Window.deiconify()
        self.Window.title("CHATROOM")
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
          
        self.textCons = Frame(self.Window,
                             width = 20, 
                             height = 2,
                             #bg = "#17202A",
                             #fg = "#EAECEE",
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
        self.scrollable = Scrollable(self.textCons)
        self.scrollable.columnconfigure(0, weight=1)
        scrollbar = Scrollbar(self.userCons)
        scrollbar.place(relheight = 1,
                        relx = 0.974)
        scrollbar.config(command = self.userCons.yview)
          
        self.wsthread = threading.Thread(target = self.createWSConnection,daemon=True)
        self.wsthread.start()
        self.refreshUsers()
        for x in usrbuttons:
            self.refreshUnread(x)
    
    def sendButton(self, msg):
        newmsg=createMessage(self.me,self.other,msg)
        sendth=threading.Thread(target = lambda: self.sendMessage(newmsg), daemon=True)
        sendth.start()
        self.entryMsg.delete(0, END)
        
    def sendMessage(self,msg):
        msgapi.send(msg)
        self.refreshConversation()
    def switchToUser(self,uid):
        self.other=uid
        self.refreshConversation()
    
    def switchToAll(self,uid=None):
        self.other=""
        msgs=defapi.receive_get(id="",fr=self.me)
        for widget in self.scrollable.winfo_children():
            widget.destroy()
        pos=0
        for m in msgs:
            if m['fr']!=self.me and not m['read']:
                m['read']=True
                defapi.read_put(id=m['_id'])
            MessageBox(self.scrollable,pos,m,m['fr']==self.me)
            pos+=1
        self.scrollable.update()
        self.scrollable.seeEnd()
    def refreshConversation(self):
        msgs=defapi.receive_get(id=self.me,fr=self.other)
        for widget in self.scrollable.winfo_children():
            widget.destroy()
        pos=0
        for m in msgs:
            if m['to']==self.me and not m['read']:
                m['read']=True
                defapi.read_put(id=m['_id'])
            MessageBox(self.scrollable,pos,m,m['fr']==self.me)
            pos+=1
        self.scrollable.update()
        self.scrollable.seeEnd()

    def refreshUsers(self,msg=None):
        ct=1
        users = defapi.users_get(self.me)
        users = sorted(users,key=lambda x: (x.last,x.active),reverse=True)
        for widget in self.userCons.winfo_children():
            widget.destroy()
        UserButton(self.userCons,0,"ALL",True,self.switchToAll)
        self.refreshUnread("ALL")
        for u in users:
            if u.uid!=self.me:
                print(u.last)
                UserButton(self.userCons,ct,u.uid,u.active,self.switchToUser)
                self.refreshUnread(u.uid)
                ct+=1
    def refreshUnread(self,uid):
        if(uid=="ALL"):
            n = defapi.unread_get(id="",fr=self.me)
        else:
            n = defapi.unread_get(id=self.me,fr=uid)
        usrbuttons[uid].setUnread(n)
    
    def refreshChatOrUnread(self,msg):
        if msg["to"] == self.me:
            if msg["fr"] == self.other:
                self.refreshConversation()
            else:
                self.refreshUnread(msg["fr"])
        else:
            if msg["to"]=="":
                if self.other == "":
                    self.switchToAll()
                else:
                    self.refreshUnread("ALL")

        pass
    def refreshRead(self,msg):
        if msg["to"] == self.me and msg["fr"] == self.other or msg["to"]==""==self.other:
            self.refreshConversation()
        pass
    
    def createWSConnection(self):
        asyncio.set_event_loop(el)
        asyncio.get_event_loop().run_until_complete(self.listen())
        asyncio.get_event_loop().run_forever()

    async def listen(self):
        global to_call_on_sio
        to_call_on_sio = self.handle_sio
        await sio.connect('http://localhost:5000')
        await sio.wait()
    
    async def handle_sio(self,data):
        message = json.loads(data)
        code = message["code"]
        print(code)
        def codedict(val):
            return {
                "usrreg":self.refreshUsers,
                "usrlog":self.refreshUsers,
                "msgrec":self.refreshChatOrUnread,
                "msgrea":self.refreshRead
            }[val]
        codedict(code)(message)
    
    """def receive(self):
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
                self.scrollable.config(state = NORMAL)
                self.userCons.delete('1.0', END)
                for u in usrs:
                    self.userCons.insert(END,u+"\n")
                    self.scrollable.config(state = DISABLED)
                    self.scrollable.see(END)
                ct = USER_REFRESH_DELAY"""
                
if __name__ == "__main__":
    g = GUI()