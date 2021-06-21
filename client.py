import tkinter as tk
from tkinter import *
import s1
import socketio
import asyncio

app = tk.Tk()
app.title('Chat')
app.geometry('550x300')
sio = socketio.Client()



sio.connect('http://127.0.0.1:5000')

def destr(roott):
    roott.destroy()

    
    

def Chat(user1,user2):
    

    root = tk.Tk()
    root.title(user2)
    root.geometry('500x500')
    s1.readMes(user1,user2)
    messages =  s1.readMes(user1,user2)
    cr = 1
    cs = 0
    r = 0
    for i in range(len(messages)):
        if messages[i]['receiver'] == user1:
            if messages[i]['is_read'] == True:
                bg = "white"
            else:
                bg = "cyan"
            user_lbl = Label(root, bg = bg, text = messages[i]['text']+ " : " + messages[i]['send_time'])
            user_lbl.grid(row=r, column=cr)
            r= r+1
            
        else:
            if messages[i]['is_read'] == True:
                bg = "white"
            else:
                bg = "cyan"
            user_lbl = Label(root,bg = bg, text = messages[i]['text']+ " : " + messages[i]['send_time'])
            user_lbl.grid(row=r, column=cs)
            r= r+1
    
    
    
    message_txt = tk.StringVar()
    message_entry = Entry(root, textvariable=message_txt)
    message_entry.grid(row=r, column=0)
    
    # message_entry.delete(0, END)
    # message_entry.insert(0, "")
    Send_btn = Button(root, text="Send", 
                    width=8 , command= lambda : [s1.sendMessage(user1,user2 , message_txt.get())])
    Send_btn.grid(row=r, column=1)

   


    
def printUsers(userr):
        
        i = 1
        users = s1.GetOnlineUsers()
        users.remove([userr,True])
        for user in users:
            if user[1] == True:
            
                Userr_btn = Button(app, text=user[0], background = 'green',
                    width=8 , command = lambda : [ Chat(userr,Userr_btn.cget('text'))])
                Userr_btn.grid(row=i, column=0)
                
                user_lbl = Label(app, text=s1.getUnreadMes(userr,user[0]), justify=LEFT)
                user_lbl.grid(row=i, column=1)
                

                # use_lbl = Label(app, text=user[0])
                # use_lbl.grid(row=i, column=2)

            else:
                
                User_btn = Button(app, text=user[0], 
                    width=8 , command = lambda : [Chat(userr,User_btn.cget('text'))] )
                User_btn.grid(row=i, column=0)
                user_lbl = Label(app, text=s1.getUnreadMes(userr,user[0]) , justify=LEFT)
                user_lbl.grid(row=i, column=1)
                
                # use_lbl = Label(app, text=user[0])
                # use_lbl.grid(row=i, column=2)

                
            i=i+1
        

        


def Open(user):
    
    name_lbl.destroy()
    LogIn_btn.destroy()
    user_entry.destroy()
    password_entry.destroy()
    name1_lbl.destroy()
    error_lbl.destroy()
    SignIn_btn.destroy()
    
    user_lbl = Label(app, text="Hello, "+ user )
    user_lbl.grid(row=0, column=0)
    
    
    for i in range(1,5):
        l0 = tk.Label(app, text='                                ')
        l0.grid(column=i, row=0)
        #l0.columnconfigure(i, minw)
    LogOut_btn = Button(app, text="LogOut",
                    width=12, command= lambda : [ s1.logOut(user),app.destroy()] )
    LogOut_btn.grid(row=0, column = 5)
    printUsers(user)

    i = 1
    users = s1.GetOnlineUsers()
    users.remove([user,True])
    for userr in users:
        user_lbl = Label(app, text=s1.getUnreadMes(user,userr[0]), justify=LEFT)
        user_lbl.grid(row=i, column=1)
    
    
    






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

def logIn(user,password):
    
    
    if  [user,password] in s1.getUsers():

        s1.logIn(user,password)
        Open(user)
    else:
        error_lbl.config( text="Your username or password is incorrect" )
def signUp(user,password):
    
    if  user in s1.getUsersName():
        error_lbl.config( text="User with this login already exists" )

    else:
        s1.signUp(user,password)
        s1.logIn(user,password)
        Open(user)
        
        
LogIn_btn = Button(app, text="LogIn",
                    width=12, command= lambda : [ logIn(user_name.get(),password_txt.get())] )
LogIn_btn.grid(row=2, column=1)
SignIn_btn = Button(app, text="SignUp",
                    width=12, command= lambda : [ signUp(user_name.get(),password_txt.get())] )
SignIn_btn.grid(row=2, column=0)


    
@sio.event
def update_list():
    Open(user_name.get())

@sio.event
def update_mes():
    
    Open(user_name.get())




app.mainloop()