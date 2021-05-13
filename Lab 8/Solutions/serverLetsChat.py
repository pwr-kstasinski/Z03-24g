
from collections import defaultdict
from fastapi import FastAPI
import uvicorn

tags_metadata = [
    {
        "name": "messages",
        "description": "Operations with sending and receiving messages"

    },
    {
        "name": "users",
        "description": "Operations with logging and future registering"
    }

]
app = FastAPI(debug=True, title = "Lets Chat", description= "Simple Api created to communicate between users", openapi_tags=tags_metadata)

messages = defaultdict(list)
users = []


def checkExistingMessages(name):
    if name not in messages:
        return False
    else:
        return True


@app.get("/get/{name}", tags=["messages"], summary="Receive messages")
def get(name: str):
    flag = checkExistingMessages(name)
    if flag:
        return{"messages": messages.pop(str(name))}
    else:
        return {"Information": "There are no new messages"}


@app.post("/send/{sender_username}/{receiver_username}/{message}", tags=["messages"], status_code=201, summary="Send message")
def post(sender_username: str, receiver_username: str, message: str):
    messages[str(receiver_username)].append((sender_username, message))
    return {"sending": "done"}


def checkIfExistingUser(loginId):
    flag = False
    if len(users) != 0:
        for user in users:
            if user == loginId:
                flag = True
    return flag


@app.put("/login/{loginId}", tags=["users"], status_code=201, summary="Enter your login")
def put(loginId: str):
    flag = checkIfExistingUser(loginId)
    if not flag:
        users.append(loginId)
        return {"Verification": f"Successfully registered, welcome {loginId}"}

    else:
        return {"Verification": f"Successfully logged in, welcome {loginId}"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
