from get_usr import isCresteU
import tkinter as tk
from tkinter import Label, Entry, Button, PhotoImage, Frame
import create_usr
import create_msg
import get_msg
import get_usr

app = tk.Tk()
app.title('Chat')
app.geometry('400x300')



def Open(user_name):
    user = user_name.get()
    name_lbl.destroy()
    LogIn_btn.destroy()
    user_entry.destroy()
    user_lbl = Label(app, text="Hello, "+ user )
    user_lbl.grid(row=0, column=0)
    
    receiver_name = tk.StringVar()
    receiver_entry = Entry(app, textvariable=receiver_name)
    receiver_entry.grid(row=1, column=1)

    message = tk.StringVar()
    message_entry = Entry(app, textvariable=message)
    message_entry.grid(row=2, column=1)

   
    receiver = receiver_name.get()
    mess = message.get()

    
    
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

        

    m1_lbl = Label(app, text="Enter receiver name:", )
    m1_lbl.grid(row=1, column=0)

    m2_lbl = Label(app, text="Enter message:", )
    m2_lbl.grid(row=2, column=0)



    getM_btn = Button(app, text="Get message",
                    width=12, command= GetMessage )
    getM_btn.grid(row=3, column=2)

    
    sendM_btn = Button(app, text="Send message",
                    width=12, command=SendMessage )
    sendM_btn.grid(row=2, column=2)

  

def logIn(userName):
    
    user=userName.get()
    if get_usr.isCresteU(user)==False:
        create_usr.createUser(user)



name_lbl = Label(app, text="Enter user name", )
name_lbl.grid(row=0, column=0)


m4_lbl = Label(app, text="" )
m4_lbl.grid(row=6, column=0)



user_name = tk.StringVar()
user_entry = Entry(app, textvariable=user_name)
user_entry.grid(row=0, column=1)

LogIn_btn = Button(app, text="LogIn",
                    width=12, command= lambda : [ logIn(user_name),Open(user_name)] )
LogIn_btn.grid(row=1, column=1)





app.mainloop()