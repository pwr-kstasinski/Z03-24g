from get_usr import isCresteU
import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage, Frame
import create_usr
import create_msg
import get_msg
import get_usr

app = tk.Tk()
app.title('Chat')
app.geometry('500x300')



def Open(user_name):
    user = user_name.get()
    name_lbl.destroy()
    LogIn_btn.destroy()
    user_entry.destroy()
    password_entry.destroy()
    name1_lbl.destroy()
    error_lbl.destroy()
    SignIn_btn.destroy()
    user_lbl = Label(app, text="Hello, "+ user )
    user_lbl.grid(row=0, column=0)
    
    receiver_name = tk.StringVar()
    receiver_entry = Entry(app, textvariable=receiver_name)
    receiver_entry.grid(row=1, column=1)

    message = tk.StringVar()
    message_entry = Entry(app, textvariable=message)
    message_entry.grid(row=2, column=1)

   

    
    
    def GetMessage():
        list_of_mes = get_msg.getMes(user)
        show = ''
        
        for mes in list_of_mes:
            show+= "from "+mes['sender']+" : "+mes['text']+"\n"
        
        m3_lbl = Label(app, text="Your messages:" )
        m3_lbl.grid(row=5, column=0)

        
        m4_lbl.config(text=show)
        

    def SendMessage():
        receiver = receiver_name.get()
        mess = message.get()
        create_msg.createMes(user,receiver,mess)

        

    m1_lbl = Label(app, text="Enter receiver name:" )
    m1_lbl.grid(row=1, column=0)

    m2_lbl = Label(app, text="Enter message:" )
    m2_lbl.grid(row=2, column=0)

    m5_lbl = Label(app, text="Users:" )
    m5_lbl.grid(row=0, column=4)
    
    users = sorted(get_usr.getUsers())
    list_users = ""
    for us in users:
        list_users = list_users + us +"\n"
    m6_lbl = Label(app, text=list_users )
    m6_lbl.grid(row=4,column=5)

    getM_btn = Button(app, text="Get message",
                    width=12, command= GetMessage )
    getM_btn.grid(row=3, column=2)

    
    sendM_btn = Button(app, text="Send message",
                    width=12, command=SendMessage )
    sendM_btn.grid(row=2, column=2)

  

def logIn(userName,passwordTxt):
    
    user=userName.get()
    password=passwordTxt.get()
    if get_usr.isCresteU(user,password)==False:
        error_lbl.config( text="Your username or password is incorrect" )
        
    else:
        Open(userName)

def signIn(userName,passwordTxt):
    
    user=userName.get()
    password=passwordTxt.get()
    
    if  create_usr.createUser(user,password) == True:
        Open(userName)
        
    else:
        error_lbl.config( text="User with this login already exists" )

name_lbl = Label(app, text="Enter user name", )
name_lbl.grid(row=0, column=0)

name1_lbl = Label(app, text="Enter password", )
name1_lbl.grid(row=1, column=0)

error_lbl = Label(app, text="" )
error_lbl.grid(row=1, column=3)

m4_lbl = Label(app, text="" )
m4_lbl.grid(row=6, column=0)

password_txt = tk.StringVar()
password_entry = Entry(app, textvariable=password_txt)
password_entry.grid(row=1, column=1)

user_name = tk.StringVar()
user_entry = Entry(app, textvariable=user_name)
user_entry.grid(row=0, column=1)

LogIn_btn = Button(app, text="Log In",
                    width=12, command= lambda : [ logIn(user_name,password_txt)] )
LogIn_btn.grid(row=2, column=1)
SignIn_btn = Button(app, text="Sign In",
                    width=12, command= lambda : [ signIn(user_name,password_txt)] )
SignIn_btn.grid(row=2, column=0)





app.mainloop()