import asyncio
import json

import websockets
from sqlalchemy import and_, or_

from database import db_session, User, Message

connected = set()


async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        async for message in websocket:
            message = json.loads(message)

            # try to log in
            if message['action'] == 'try_login':
                user = User.query.filter(
                    and_(User.login == message['login'],
                         User.password == message['password']
                         )).first()
                if user:
                    await websocket.send(json.dumps({
                        'action': 'confirm_login',
                        'login': user.login,
                        'id': user.id,
                    }))
                    websocket.user_id = user.id
                else:
                    await websocket.send(
                        json.dumps({'action': 'failed_login'}))

            # try to register
            if message['action'] == 'try_register':
                user = User(message['login'], message['password'])
                try:
                    db_session.add(user)
                    db_session.commit()
                    await websocket.send(json.dumps({
                        'action': 'confirm_register',
                        'login': user.login,
                        'id': user.id,
                    }))
                except Exception:
                    await websocket.send(
                        json.dumps({'action': 'failed_register'}))

            # set user active
            if message['action'] == 'set_active':
                user = User.query.filter(User.id == message['user_id']).first()
                try:
                    db_session.add(user)
                    db_session.commit()
                    await websocket.send(json.dumps({
                        'action': 'confirm_register',
                        'login': user.login,
                        'id': user.id,
                    }))
                except Exception:
                    await websocket.send(
                        json.dumps({'action': 'failed_register'}))

            # get all users
            if message['action'] == 'get_users':
                users = []
                for user in User.query.all():
                    users.append({'login': user.login, 'id': user.id})
                await websocket.send(
                    json.dumps({'action': 'list_users', 'users': users}))

            # send message
            if message['action'] == 'send_message':
                message = Message(message['sender'], message['recipient'],
                                  message['content'])
                db_session.add(message)
                db_session.commit()

                # invoke
                for conn in connected:
                    await conn.send(
                        json.dumps({'action': 'list_messages', 'sender': message.sender_id,
                            'recipient': message.recipient_id, 'messages': [{
                            'id': message.id,
                            'sender_id': message.sender_id,
                            'recipient_id': message.recipient_id,
                            'content': message.content,
                            'read': message.read,
                            'sent': str(message.sent)
                        }]}))

            # get messages
            # if message['action'] == 'get_messages':
            #     messages = Message.query.filter(
            #         or_(and_(Message.recipient_id == message['recipient'],
            #                  Message.sender_id == message['sender']),
            #             and_(Message.recipient_id == message['sender'],
            #                  Message.sender_id == message['recipient']))).all()
                # output = []
                # for message in messages:
                #     output.append({
                #         'id': message.id,
                #         'sender_id': message.sender_id,
                #         'recipient_id': message.recipient_id,
                #         'content': message.content,
                #         'read': message.read,
                #         'sent': str(message.sent)
                #     })
                #
                # # invoke
                # for conn in connected:
                #     await conn.send(
                #         json.dumps(
                #             {'action': 'list_messages', 'messages': output}))
    finally:
        # Unregister.
        connected.remove(websocket)


start_server = websockets.serve(server, "localhost", 5000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
