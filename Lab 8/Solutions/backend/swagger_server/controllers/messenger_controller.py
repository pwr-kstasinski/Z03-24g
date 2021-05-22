import connexion
import six

from swagger_server import util
from json import dumps

from swagger_server.global_server import *


def receive_get(token=None, sender=None):
    """Receives messages

    Receivies all messages from server

    :param token: User token
    :type token: int
    :param sender: Message sender, optional
    :type sender: str

    :rtype: Object
    """
    if token is None:
        return "invalid_token", 404
    response = GLOBAL_SERVER.get_all_messages(token, sender)
    if response == 1:
        return "invalid_token", 404
    elif response == 0:
        return "empty", 201
    return dumps(list(map(lambda d: {"sender":d.sender, "receiver":d.receiver, "message": d.message, "send_time": str(d.send_date)}, response)))


def receivers_get():
    """List all receivers

    Lists all messages receivers in the system


    :rtype: str
    """
    return ";".join(GLOBAL_SERVER.list_clients())


def send_post(token=None, receiver=None, message=None):  # noqa: E501
    """Sends message

    Sends message to the server # noqa: E501

    :param token: User token
    :type token: int
    :param receiver: Message receiver login
    :type receiver: str
    :param message: Message to send
    :type message: str

    :rtype: None
    """
    if message is None or receiver is None or token is None:
        return "invalid_arguments", 400
    response = GLOBAL_SERVER.send_message(int(token), receiver, message)
    if response == 2:
        return "target_not_found", 404
    elif response != 0:
        return "invalid_arguments", 400
    else:
        return "sent"
