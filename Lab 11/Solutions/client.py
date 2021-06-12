from openapi_client import Configuration, ApiClient
from openapi_client.api.messages_api import MessagesApi
from openapi_client.api.users_api import UsersApi
from tkinter import *
import threading
from tkinter import scrolledtext
import socket
import asyncio
import threading
from datetime import date, datetime
config = Configuration(host="127.0.0.1:5001")
messObj = MessagesApi(ApiClient(config))
usrObj = UsersApi(ApiClient(config))
global isOpen
global messagesFieldReceiver
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)
global white
global reSize
global sizeWindow
global root


def sendMessage(username, recv):
    sender = username
    receiver = recv
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    messagesField.tag_config('date', foreground="grey", font=("Courier", 7), justify="left")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message_text = sendingField.get("1.0", END)
    messObj.post_send_sender_username_receiver_username_message_post(sender, receiver, message_text)
    messagesField.insert(END, f"{sender}: {message_text}", "send")
    messagesField.insert(END, f"{d1},{current_time},Recv:No \n ",  'date')
    sendingField.delete('1.0', 'end')

def sendMessageAll():
    sender = username
    today = date.today()
    d1 = today.strftime("%Y/%m/%d")
    messagesField.tag_config('date', foreground="grey", font=("Courier", 7), justify="left")
    messagesField.tag_config('all', foreground="purple", font=("Courier", 10), justify="left")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message_text = sendingField.get("1.0", END)
    messObj.post_all_send_all_post(sender, "all", message_text)
    messagesField.insert(END, f"{sender} to All : {message_text}", "all")
    messagesField.insert(END, f"{d1},{current_time},Recv:No \n", 'date')
    sendingField.delete('1.0', 'end')

def getMessage(flag, recv):
    client = username
    anyNewMess = getNewMessages(username, recv)
    if anyNewMess > 0:
        res = messObj.marked_as_read_marked_as_read_name_sender_put(username, recv)

    mess = messObj.get_get_name_sender_get(client, recv)

    if mess == []:
        if flag:
            messagesField.insert(END, "No new messages\n", 'system')
        else:
            pass
    else:
        messagesField.delete('1.0', 'end')
        sortedMess = sorted(mess, key=lambda k: k['id'])
        for m in range(len(sortedMess)):
            sender = sortedMess[m]['senderUsername']
            messageText = sortedMess[m]['message']
            date = sortedMess[m]['date']
            time  = sortedMess[m]['time']
            isRead = sortedMess[m]['isRead']
            toAll = sortedMess[m]['toAll']

            if isRead == 1:
                receivedMessage = "Yes"
            else:
                receivedMessage = "No"
            if sender == client:

                if toAll == False:

                    messagesField.insert(END, f"{sender}: {messageText}", 'send')
                    messagesField.insert(END, f"{date},{time},Recv:{receivedMessage} \n", 'dateLeft')
                else:
                    messagesField.insert(END, f"{sender} to All: {messageText}", 'allLeft')
                    messagesField.insert(END, f"{date},{time},Recv:{receivedMessage} \n", 'dateLeft')
            else:

                if toAll == False:
                    messagesField.insert(END, f"{sender}: {messageText}", 'received')
                    messagesField.insert(END, f"{date},{time},Recv: {receivedMessage} \n",'dateRight')
                else:
                    messagesField.insert(END,f"{sender} to All: {messageText}",
                                         'allRight')
                    messagesField.insert(END, f"{date},{time},Recv: {receivedMessage} \n",'dateRight')


def getNewMessages(username, sender):
    (nim, count) = messObj.get_new_get_new_name_sender_get(username,sender)

    return count


def clearMessage():
    messagesField.delete('1.0', 'end')


def logOut(newWindow):
    newWindow.destroy()
    global flag
    flag = False

    usrObj.logout_logout_post({"login": f"{username}", "password": f"{password}"})


def goBack(convWindow):
    global isOpen
    global white
    isOpen = (False, "")
    res = usrObj.active_users_active_users_get()

    orderedUsers, messageTable = getOrder(res, username)
    createButtons(orderedUsers, white)
    convWindow.destroy()


def PeronalizedchatView(newWindow,recv):
    global username


    global messagesField
    global messagesFieldReceiver
    global toWhoEntry
    global password
    global sendingField
    global userEntry
    global isOpen

    convWindow = Toplevel(newWindow)

    convWindow.geometry("500x375")
    convWindow['background'] = "gray32"


    isOpen = (True, recv)

    loginLabel = Label(convWindow, text="Logged in as : " + username + " chatting with: " + recv, bg="gray32", fg="snow")
    loginLabel.grid(row=0, column=0)

    messagesField = scrolledtext.ScrolledText(convWindow, height=10, width=60)
    messagesField.grid(row=1, columnspan=8)

    messagesField.tag_config('received',  foreground="green", font=("Courier", 10),justify="right")
    messagesField.tag_config('send', foreground="blue", font=("Courier", 10))
    messagesField.tag_config('system', foreground="grey", font=("Courier", 8), justify="center")
    messagesField.tag_config('dateLeft', foreground="grey", font=("Courier", 7), justify="left")
    messagesField.tag_config('dateRight', foreground="grey", font=("Courier", 7), justify="right")
    messagesField.tag_config('allLeft', foreground="purple", font=("Courier", 10), justify="left")
    messagesField.tag_config('allRight', foreground="purple", font=("Courier", 10), justify="right")


    messagesField.insert(END, "System :" + "Welcome chat room: " + f"{username} with {recv}"+ "\n", 'system')

    getMessages = Button(convWindow, text="Refresh", command=lambda: getMessage(True, recv), bg="navy", fg="snow")
    getMessages.grid(row=5, column=7)
    sendMessages = Button(convWindow, text="Send", command=lambda : sendMessage(username, recv), bg="navy", fg="snow", height=2 , width=7)
    sendMessages.grid(row=8, column=0)
    clearMessages = Button(convWindow, text="Clear", command=clearMessage, bg="navy", fg="snow", height=2 , width=7 )
    clearMessages.grid(row=8, column=4)
    back = Button(convWindow, text="Back", command=lambda: goBack(convWindow), bg="navy", fg="snow", height=2, width=7)
    back.grid(row=8, column=6)

    getMessage(True, recv)

    sendMessagesAll = Button(convWindow, text="SendAll", command=sendMessageAll, bg="navy", fg="snow", height=2, width=7)
    sendMessagesAll.grid(row=8, column=2)


    sendingField = Text(convWindow, height=6, width=60)
    sendingField.grid(row=6, columnspan=8)



def getOrder(res, username):
    messageArray = []
    usersWithMessages = []
    usersWithoutMessages = []
    togetherArray = []

    for x in res[1]:
        if x['login'] != username:
            previousMessages = messObj.get_get_name_sender_get(username, x['login'])
            if previousMessages != []:
                sortedPreviousMessages = sorted(previousMessages, key=lambda k: k['id'])
                t = sortedPreviousMessages[len(sortedPreviousMessages)-1]['time']
                hours = int(t[0:2])
                minutes = int(t[3:5])
                seconds = int(t[6:8])
                sumTime = hours * 3600 + minutes * 60 + seconds
                numberOfNewMessage = getNewMessages(username, x['login'])
                usersWithMessages.append((x['login'], x['is_active'], numberOfNewMessage , sumTime))


            else:
                usersWithoutMessages.append((x['login'], x['is_active'], 0, 0))
    usersWithMessages.sort(key=lambda element: (element[3], element[1]))
    usersWithMessages.reverse()
    for y in usersWithMessages:
         togetherArray.append(y)
    usersWithoutMessages.sort(key=lambda tu: (-tu[1], tu[0]))

    for z in usersWithoutMessages:
        togetherArray.append(z)

    return togetherArray, messageArray

def createButtons(orderedUsers, white= False):
    global reSize
    global sizeWindow
    list = newWindow.grid_slaves()

    for l in list:
        l.destroy()
    index = 4
    count = 0
    if white == True:
        bgColor = "snow"
        fgColor = "black"
    else:
        fgColor = "snow"
        bgColor = "black"

    createOther(bgColor, fgColor)
    for x in orderedUsers:
        user = x[0]
        activeStatus = x[1]
        if activeStatus == 1:
            activeStatus = "Active"
            name = Button(newWindow, text=f"{user}, Status: {activeStatus} , New messages: {x[2]}",
                          command=lambda user=user: PeronalizedchatView(newWindow, user), bg=bgColor, fg="green")
        else:
            activeStatus = "Inactive"
            name = Button(newWindow, text=f"{user}, Status: {activeStatus} , New messages: {x[2]}",
                      command=lambda user=user: PeronalizedchatView(newWindow, user) , bg=bgColor , fg="red")

        name.grid(row=index, column=0)
        index += 1
        count += 1

    if count > reSize:
        sizeWindow = sizeWindow *2
        newWindow.geometry(f"390x{sizeWindow}")
        reSize = reSize + count

def changeMotiveF():
    global white
    global root
    if white == False:
        white = True

    else:
        white = False
    newWindow.destroy()
    chatView(root, True)


def createOther(bg, fg):
    loginLabel = Label(newWindow, text="Logged in as : " + username, bg=bg, fg=fg)
    loginLabel.grid(row=0, column=0)

    logOutButton = Button(newWindow, text="Log out", command=lambda: logOut(newWindow), bg="navy", fg="snow",
                          activebackground="red")
    logOutButton.grid(row=0, column=9)

    changeMotive = Button(newWindow, text="Change motive", command=changeMotiveF, bg="navy", fg="snow",
                          activebackground="red")
    changeMotive.grid(row=0, column=11)


def chatView(root,who, window = None):


    global messagesField
    global white
    global toWhoEntry
    global username
    global password
    global sendingField
    global userEntry
    global newWindow
    global isOpen
    global sizeWindow
    isOpen = (False, "")


    if white == True:
        back = "white"

    else:
        back = "black"
    if window !=None:
        window.destroy()

    newWindow = Toplevel(root)

    newWindow.geometry(f"390x{sizeWindow}")
    newWindow['background'] = back

    res = usrObj.active_users_active_users_get()


    orderedUsers, messageTable = getOrder(res, username)

    createButtons(orderedUsers, white)


def loggingIn(root):
    global LuserEntryLogin
    global LuserEntryPassword

    logWindow = Toplevel(root)

    logWindow.geometry("500x375")
    logWindow['background'] = "gray32"

    logWindow.geometry("300x180")
    logWindow['background'] = "black"
    loggingLabel = Label(logWindow, text="Welcome to logging panel!", fg="snow", bg="black")
    loggingLabel.pack()
    usernameLabel = Label(logWindow, text='Enter your login:', bg="black", fg="snow")
    usernameLabel.pack()
    LuserEntryLogin = Entry(logWindow, bg="snow", width=20)
    LuserEntryLogin.pack()
    passwordLabel = Label(logWindow, text='Enter your password:', bg="black", fg="snow")
    passwordLabel.pack()
    LuserEntryPassword = Entry(logWindow,show="*",  bg="snow", width=20)
    LuserEntryPassword.pack()
    loginButton = Button(logWindow, text="LogIn", command=lambda: verifyLogin(logWindow, root), bg="black",
                            activebackground="green", height=2, width=6, fg="snow")
    loginButton.config(font=("Arial", 12))
    loginButton.pack()

def registeringIn(root):
    global userEntryLogin
    global userEntryPassword

    regWindow = Toplevel(root)

    regWindow.geometry("300x180")
    regWindow['background'] = "black"
    registeringLabel = Label(regWindow, text="Welcome to registering panel!", fg="snow", bg="black")
    registeringLabel.pack()
    usernameLabel = Label(regWindow, text='Create your login:', bg="black", fg="snow")
    usernameLabel.pack()
    userEntryLogin = Entry(regWindow, bg="snow", width=20)
    userEntryLogin.pack()
    passwordLabel = Label(regWindow, text='Create your password:', bg="black", fg="snow")
    passwordLabel.pack()
    userEntryPassword = Entry(regWindow,show="*" , bg="snow", width=20)
    userEntryPassword.pack()
    registerButton = Button(regWindow, text="Register", command=lambda: verifyRegister(regWindow, root), bg="black",
                         activebackground="green", height=2, width=6, fg="snow")
    registerButton.config(font=("Arial", 12))
    registerButton.pack()


def loginWindow(root):
    global white
    global reSize
    global sizeWindow
    sizeWindow =200
    reSize = 5
    white = False
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

def verifyRegister(regWindow ,root):
    global username
    global password
    login = userEntryLogin.get()
    password = userEntryPassword.get()
    username = login
    password = password
    sock.send(login.encode(FORMAT))
    res = usrObj.put_register_post({"login": f"{login}", "password": f"{password}"})

    if res == {"Information" : "Successfully created account"}:
        chatView(root, True, regWindow )
    else:
        err = Toplevel(root)
        err.geometry("250x60")
        err['background'] = "black"
        errorLabel = Label(err, text="User with given login already exists!", fg="snow", bg="black")
        errorLabel.pack()

def verifyLogin(logWindow , root):

    global username
    global password
    password = LuserEntryPassword.get()
    login = LuserEntryLogin.get()
    username = login
    password = password

    res = usrObj.put_login_post({"login": f"{login}", "password": f"{password}"})

    if res == {"Information": f"Welcome to the Lets App:  {login}"}:

        chatView(root, False, logWindow)
    else:
        err = Toplevel(root)
        err.geometry("250x60")
        err['background'] = "black"
        errorLabel = Label(err, text=res, fg="snow", bg="black")
        errorLabel.pack()

def handleSockets():
    while True:
        try:
            global isOpen
            global newWindow

            message = sock.recv(1024).decode(FORMAT)
            if message == "0":

                res = usrObj.active_users_active_users_get()
                orderedUsers, messageTable = getOrder(res, username)
                createButtons(orderedUsers, white)
            elif len(message) > 1 and message[0] != "9":
                if isOpen[0] == False or isOpen[1] != message:
                    res = usrObj.active_users_active_users_get()

                    orderedUsers, messageTable = getOrder(res, username)
                    createButtons(orderedUsers, white)
                elif isOpen[0] == True and isOpen[1] == message:
                    getMessage(True, message)
            elif message[0] == "9":
                name = ""
                for mes in range(len(message)):
                    if mes == 0 :
                        continue
                    else:
                        name += message[mes]
                print(name)
                if isOpen[0] == True and isOpen[1] == name:
                    getMessage(True, name)

        except:
            continue


if __name__ == "__main__":
    root = Tk()
    root.title("Lets Chat")
    root.geometry("300x180")
    root['background'] = "black"
    logIn = Button(root, text="LogIn", command=lambda: loginWindow(root), bg="black",
                         activebackground="green", height=1, width=5, fg="snow")
    thread = threading.Thread(target=handleSockets)
    thread.start()
    loginWindow(root)
    root.mainloop()
