import requests as req
import tkinter as tk
import time

class Gui(tk.Frame):
    def __init__(self, master=tk.Tk()):
        super().__init__(master)
        master.title("message server client")
        self.pack()
        self.createWidgets()
    
    def createWidgets(self):
        self.registrationFrame=tk.Frame()
        self.registrationFrame.pack(side="top")

        idLabel=tk.Label(self.registrationFrame,text="User Id:")
        idLabel.grid(row=0,column=0)
        self.idInput=tk.Entry(self.registrationFrame)
        self.idInput.grid(row=0,column=1)
        
        passLabel=tk.Label(self.registrationFrame,text="Password:")
        passLabel.grid(row=1,column=0)
        self.passInput=tk.Entry(self.registrationFrame)
        self.passInput.grid(row=1,column=1)

        self.loginButton=tk.Button(self.registrationFrame,text="login",command=self.loginUser)
        self.loginButton.grid(row=2,column=0)
        self.registerButton=tk.Button(self.registrationFrame,text="register",command=self.registerUser)
        self.registerButton.grid(row=2,column=1)
        
        self.loginResult=tk.Label(self.registrationFrame,text="")
        self.loginResult.grid(row=3,column=0)
        
    def createChatroomLayout(self):
        self.registrationFrame.pack_forget()
        self.pack()
        self.chatFrame=tk.Frame(self)
        self.chatFrame.pack(side="top")

        self.chatInfoFrame=tk.Frame(self.chatFrame)
        self.chatInfoFrame.grid(row=0)
        userIdLabel=tk.Label(self.chatInfoFrame,text="User Id: "+self.userId)
        userIdLabel.grid(row=0,column=0)

        self.messagesFrame=tk.Frame(self.chatFrame)
        self.messagesFrame.grid(row=1)
        self.messageLabels=[]
        for i in range(1,10):
            self.messageLabels.append(tk.Label(self.messagesFrame,text=""))
            self.messageLabels[-1].grid(row=i-1,column=0)
        
        self.messagingFrame=tk.Frame(self.chatFrame)
        self.messagingFrame.grid(row=2)
        self.messageEntry=tk.Entry(self.messagingFrame)
        self.messageEntry.grid(row=0,column=0)
        self.messageEntry.bind("<Return>",self.sendMessage)
        self.messageEntryButton=tk.Button(self.messagingFrame,text="Send",command=self.sendMessage)
        self.messageEntryButton.grid(row=0,column=1)

        self.waitForMessages()


    def registerUser(self):
        if((self.idInput.get()=="")or(self.passInput.get()=="")):
            self.loginResult["text"]="no id or password provided"
            self.update()
            return
        res=req.post("http://127.0.0.1:5000/api/users/register"
            ,data={"userId":self.idInput.get(),"password":self.passInput.get()})
        if(res.text=="Registered successfully"):
            self.userId=self.idInput.get()
            self.userPass=self.passInput.get()
            return self.createChatroomLayout()
        else:
            self.loginResult["text"]="Id alredy taken"
            self.update()
            return
            """self.userId=self.idInput.get()
            return self.createChatroomLayout()"""

    def loginUser(self):
        if((self.idInput.get()=="")or(self.passInput.get()=="")):
            self.loginResult["text"]="no id or password provided"
            self.update()
            return
        res=req.post("http://127.0.0.1:5000/api/users/login"
            ,data={"userId":self.idInput.get(),"password":self.passInput.get()})
        if(res.text=="Login successfull"):
            self.userId=self.idInput.get()
            self.userPass=self.passInput.get()
            return self.createChatroomLayout()
        else:
            self.loginResult["text"]="wrong id or password"
            self.update()
            return
        

    def waitForMessages(self):
        while(True):
            res_raw=req.get("http://127.0.0.1:5000/api/users"
                ,data={"userId":self.userId,"password":self.userPass})
            print(res_raw.text)
            res=res_raw.json()
            res.reverse()
            res.append(None)
            j=0
            while(res[j]!=None):
                i=0
                while(i+1<len(self.messageLabels)):
                    self.messageLabels[i]["text"]=self.messageLabels[i+1]["text"]
                    i+=1
                self.messageLabels[-1]["text"]=res[j]["srcId"]+":\n"+res[j]["msg"]
                j+=1
            self.messagesFrame.update()
            time.sleep(1)
    
    def sendMessage(self,event=None):
        res=req.post("http://127.0.0.1:5000/api/send/all"
            ,{"userId":self.userId,"password":self.userPass,"msg":self.messageEntry.get()})
        self.messageEntry.delete(0,1000)
        self.messagesFrame.update()

Gui().mainloop()



"""
data={"recieverId":"qwe","msg":"hihi"}
res=req.post("http://127.0.0.1:5000/api/send?id=asd",data)
print(res.text)
data2={"msg":"nooooo"}
res=req.post("http://127.0.0.1:5000/api/send/all?id=asd",data2)
print(res.text)
"""