import connexion
import six

from swagger_server.models.object import Object  # noqa: E501
from swagger_server import util


def receive_get(token=None, nadawca=None):  # noqa: E501
    """Receives messages

    Receivies all messages from server # noqa: E501

    :param token: User token
    :type token: float
    :param nadawca: Message sender, optional
    :type nadawca: str

    :rtype: Object
    """
    return 'do some magic!'


def receivers_get():  # noqa: E501
    """List all receivers

    Lists all messages receivers in the system # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def send_post(token=None, receiver=None, message=None):  # noqa: E501
    """Sends message

    Sends message to the server # noqa: E501

    :param token: User token
    :type token: float
    :param receiver: Message receiver login
    :type receiver: str
    :param message: Message to send
    :type message: str

    :rtype: None
    """
    return 'do some magic!'
