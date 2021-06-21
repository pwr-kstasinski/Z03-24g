from tkinter import scrolledtext

from openapi_client.api.messages_api import MessagesApi
from openapi_client.api.users_api import UsersApi
from openapi_client.configuration import Configuration
from openapi_client import ApiClient
from tkinter import *
import threading

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


def getMessage(flag):
    client = username

    mess = messObj.get_get_name_get(client)

    if mess == {"Information": "There are no new messages"}:
        if flag:
            messagesField.insert(END, "No new messages\n", 'system')
        else:
            pass
    else:
        for m in mess['messages']:
            sender = m[0]
            messageText = m[1]
            messagesField.insert(END, sender + ": " + messageText, 'received')


def clearMessage():
    messagesField.delete('1.0', 'end')


def logIn(username):
    response = usrObj.put_login_login_id_put(username)

    return response['Verification']


def logOut(newWindow):
    newWindow.destroy()
    global flag
    flag = False


def chatView(root):
    global username

    global messagesField

    global toWhoEntry

    global sendingField

    username = userEntry.get()
    newWindow = Toplevel(root)

    newWindow.geometry("500x375")
    newWindow['background'] = "gray32"

    welcomeMessage = logIn(username)

    loginLabel = Label(newWindow, text="Logged in as : " + username, bg="gray32", fg="snow")
    loginLabel.grid(row=0, column=0)

    messagesField = scrolledtext.ScrolledText(newWindow, height=10, width=60)
    messagesField.grid(row=1, columnspan=8)
    messagesField.tag_config('received',  foreground="green")
    messagesField.tag_config('send', foreground="blue")
    messagesField.tag_config('system', foreground="grey")

    messagesField.insert(END, "System :" + welcomeMessage + "\n", 'system')
    getMessages = Button(newWindow, text="Refresh", command=lambda: getMessage(True), bg="navy", fg="snow")
    getMessages.grid(row=5, column=7)
    sendMessages = Button(newWindow, text="Send", command=sendMessage, bg="navy", fg="snow", height=2 , width=7)
    sendMessages.grid(row=8, column=1)
    clearMessages = Button(newWindow, text="Clear", command=clearMessage, bg="navy", fg="snow", height=2 , width=7 )
    clearMessages.grid(row=8, column=3)
    logOutButton = Button(newWindow, text="Log out", command=lambda: logOut(newWindow), bg="navy", fg="snow", activebackground="red")
    logOutButton.grid(row=0, column=7)

    toWhoEntry = Entry(newWindow, width=20)
    toWhoEntry.grid(row=5, column=1)
    dest_lbl = Label(newWindow, text="Write to: ", bg="gray32", fg="snow", anchor="e", width=8)
    dest_lbl.grid(row=5, column=0)

    sendingField = Text(newWindow, height=6, width=60)
    sendingField.grid(row=6, columnspan=8)
    global flag
    flag = True
    checkForMessages()


def login(root):
    global userEntry

    helloLabel = Label(root, text="Welcome to Lets Chat!", fg="snow", bg="black")
    helloLabel.pack()
    usernameLabel = Label(root, text='Enter your login:', bg="black", fg="snow")
    usernameLabel.pack()
    userEntry = Entry(root, bg="snow", width=20)
    userEntry.pack()
    logInButton = Button(root, text="Log-in", command=lambda: chatView(root), bg="black",
                         activebackground="green", height=1, width=5, fg="snow")
    logInButton.config(font=("Arial", 12))
    logInButton.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("Lets Chat")
    root.geometry("260x120")
    root['background'] = "black"
    login(root)
    root.mainloop()
