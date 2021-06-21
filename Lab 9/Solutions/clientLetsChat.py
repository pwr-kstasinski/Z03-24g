from openapi_client import Configuration, ApiClient
from openapi_client.api.messages_api import MessagesApi
from openapi_client.api.users_api import UsersApi
from tkinter import *
import threading
from tkinter import scrolledtext
config = Configuration(host="http://127.0.0.1:5000")
messObj = MessagesApi(ApiClient(config))
usrObj = UsersApi(ApiClient(config))
global flag


def checkForMessages():
    if flag:
        threading.Timer(2.0, checkForMessages).start()
        getMessage(False)
    else:
        pass


def sendMessage():
    sender = username
    receiver = toWhoEntry.get()
    message_text = sendingField.get("1.0", END)
    messObj.post_send_sender_username_receiver_username_message_post(sender, receiver, message_text)
    messagesField.insert(END, "To " + receiver + ": " + message_text, 'send')
    sendingField.delete('1.0', 'end')

def sendMessageAll():
    sender = username
    message_text = sendingField.get("1.0", END)
    messObj.post_send_all_post(sender, "all", message_text)
    messagesField.insert(END, "To " + "all" + ": " + message_text, 'send')
    sendingField.delete('1.0', 'end')

def getMessage(flag):
    client = username

    mess = messObj.get_get_name_get(client)

    if mess == {"Information" : "No new messages"}:
        if flag:
            messagesField.insert(END, "No new messages\n", 'system')
        else:
            pass
    else:
        for m in mess:
            sender = m['senderUsername']
            messageText = m['message']
            messagesField.insert(END, sender + ": " + messageText, 'received')


def clearMessage():
    messagesField.delete('1.0', 'end')


def logOut(newWindow):
    newWindow.destroy()
    global flag
    flag = False

    usrObj.logout_logout_post({"login": f"{username}", "password": f"{password}"})



def chatView(root,who):
    global LuserEntryLogin
    global LuserEntryPassword
    global userEntryLogin
    global userEntryPassword

    global messagesField

    global toWhoEntry
    global username
    global password
    global sendingField
    global userEntry
    if who:
       username = userEntryLogin.get()
       password = userEntryPassword.get()
    else:
        username = LuserEntryLogin.get()
        password = LuserEntryPassword.get()

    for elem in root.winfo_children():
        elem.destroy()


    root.geometry("500x375")
    root['background'] = "gray32"


    loginLabel = Label(root, text="Logged in as : " + username, bg="gray32", fg="snow")
    loginLabel.grid(row=0, column=0)

    messagesField = scrolledtext.ScrolledText(root, height=10, width=60)
    messagesField.grid(row=1, columnspan=8)
    messagesField.tag_config('received',  foreground="green")
    messagesField.tag_config('send', foreground="blue")
    messagesField.tag_config('system', foreground="grey")

    messagesField.insert(END, "System :" + "Welcome to LetsChat: " + f"{username}"+ "\n", 'system')
    getMessages = Button(root, text="Refresh", command=lambda: getMessage(True), bg="navy", fg="snow")
    getMessages.grid(row=5, column=7)
    sendMessages = Button(root, text="Send", command=sendMessage, bg="navy", fg="snow", height=2 , width=7)
    sendMessages.grid(row=8, column=1)
    clearMessages = Button(root, text="Clear", command=clearMessage, bg="navy", fg="snow", height=2 , width=7 )
    clearMessages.grid(row=8, column=6)
    logOutButton = Button(root, text="Log out", command=lambda: logOut(root), bg="navy", fg="snow", activebackground="red")
    logOutButton.grid(row=0, column=7)
    showActiveUsers = Button(root, text="ActiveUsers", command=lambda: activeUsers(root), bg="navy", fg="snow", height=2, width=9)
    showActiveUsers.grid(row=5, column=5)
    sendMessagesAll = Button(root, text="SendAll", command=sendMessageAll, bg="navy", fg="snow", height=2, width=7)
    sendMessagesAll.grid(row=8, column=4)
    toWhoEntry = Entry(root, width=20)
    toWhoEntry.grid(row=5, column=1)
    dest_lbl = Label(root, text="Write to: ", bg="gray32", fg="snow", anchor="e", width=8)
    dest_lbl.grid(row=5, column=0)

    sendingField = Text(root, height=6, width=60)
    sendingField.grid(row=6, columnspan=8)
    global flag
    flag = True
    checkForMessages()


def activeUsers(root):
    res = usrObj.active_users_active_users_get()
    active = Toplevel(root)
    active.geometry("250x200")
    active['background'] = "white"
    welcome = Label(active, text="Currently active users: ", bg="snow", fg="black")
    welcome.pack()
    t = Text(active)
    for x in res:
        t.insert(END, x['login'] + '\n')
    t.pack()
def loggingIn(root):
    global LuserEntryLogin
    global LuserEntryPassword

    for elem in root.winfo_children():
        elem.destroy()

    root.geometry("300x180")
    root['background'] = "black"
    loggingLabel = Label(root, text="Welcome to logging panel!", fg="snow", bg="black")
    loggingLabel.pack()
    usernameLabel = Label(root, text='Enter your login:', bg="black", fg="snow")
    usernameLabel.pack()
    LuserEntryLogin = Entry(root, bg="snow", width=20)
    LuserEntryLogin.pack()
    passwordLabel = Label(root, text='Enter your password:', bg="black", fg="snow")
    passwordLabel.pack()
    LuserEntryPassword = Entry(root,show="*",  bg="snow", width=20)
    LuserEntryPassword.pack()
    loginButton = Button(root , text="LogIn", command=lambda: verifyLogin(root), bg="black",
                            activebackground="green", height=2, width=6, fg="snow")
    loginButton.config(font=("Arial", 12))
    loginButton.pack()

def registeringIn(root):
    global userEntryLogin
    global userEntryPassword

    for elem in root.winfo_children():
        elem.destroy()

    root.geometry("300x180")
    root['background'] = "black"
    registeringLabel = Label(root, text="Welcome to registering panel!", fg="snow", bg="black")
    registeringLabel.pack()
    usernameLabel = Label(root, text='Enter your login:', bg="black", fg="snow")
    usernameLabel.pack()
    userEntryLogin = Entry(root, bg="snow", width=20)
    userEntryLogin.pack()
    passwordLabel = Label(root, text='Enter your password:', bg="black", fg="snow")
    passwordLabel.pack()
    userEntryPassword = Entry(root,show="*" , bg="snow", width=20)
    userEntryPassword.pack()
    registerButton = Button(root, text="Register", command=lambda: verifyRegister(root), bg="black",
                         activebackground="green", height=2, width=6, fg="snow")
    registerButton.config(font=("Arial", 12))
    registerButton.pack()


def loginWindow(root):

    helloLabel = Label(root, text="Welcome to Lets Chat!", fg="snow", bg="black")
    helloLabel.pack()
    usernameLabel = Label(root, text='Do you want to login or register?', bg="black", fg="snow")
    usernameLabel.pack()
    registerButton = Button(root, text="Register", command=lambda: registeringIn(root), bg="black",
                            activebackground="green", height=2, width=6, fg="snow")
    logInButton = Button(root, text="Log-in", command=lambda: loggingIn(root), bg="black",
                         activebackground="green", height=2, width=6, fg="snow")

    registerButton.config(font=("Arial", 12), padx=10)
    registerButton.pack()
    logInButton.config(font=("Arial", 12),padx=10)
    logInButton.pack()

def verifyRegister(root):
    login = userEntryLogin.get()
    password = userEntryPassword.get()

    res = usrObj.put_register_post({"login": f"{login}", "password": f"{password}"})

    if res == {"Information" : "Successfully created account"}:
        chatView(root, True)
    else:
        err = Toplevel(root)
        err.geometry("250x60")
        err['background'] = "black"
        errorLabel = Label(err, text="User with given login already exists!", fg="snow", bg="black")
        errorLabel.pack()

def verifyLogin(root):
    login = LuserEntryLogin.get()
    password = LuserEntryPassword.get()

    res = usrObj.put_login_post({"login": f"{login}", "password": f"{password}"})

    if res == {"Information": f"Welcome to the Lets App:  {login}"}:
        chatView(root, False)
    else:
        err = Toplevel(root)
        err.geometry("250x60")
        err['background'] = "black"
        errorLabel = Label(err, text=res, fg="snow", bg="black")
        errorLabel.pack()



if __name__ == "__main__":
    root = Tk()
    root.title("Lets Chat")
    root.geometry("300x180")
    root['background'] = "black"
    logIn = Button(root, text="LogIn", command=lambda: loginWindow(root), bg="black",
                         activebackground="green", height=1, width=5, fg="snow")

    loginWindow(root)
    root.mainloop()

