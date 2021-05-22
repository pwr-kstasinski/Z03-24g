import connexion
import six
from random import randint
from swagger_server import util
from swagger_server.global_server import *


def login_post(login=None):
    """Login to system

    Logs the user to the system using login

    :param login: User login
    :type login: str

    :rtype: Integer
    """
    if login is None:
        return 'invalid_login', 404
    user: Client = GLOBAL_SERVER.get_client(login)
    if user is None:
        return 'invalid_login', 404
    else:
        return user.login_to_system()


def logout_post(token=None):  # noqa: E501
    """Logout from the system

     # noqa: E501

    :param token: Token
    :type token: str

    :rtype: None
    """
    if token is None or not token.isdigit():
        return 'not_found', 404
    user: Client = GLOBAL_SERVER.get_client_token(int(token))
    if user is None:
        return 'not_found', 404
    user.logout()
    return 'logged_out'
