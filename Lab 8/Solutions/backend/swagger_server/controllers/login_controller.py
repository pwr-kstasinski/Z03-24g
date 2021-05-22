import connexion
import six

from swagger_server import util


def login_post(login=None):  # noqa: E501
    """Login to system

    Logs the user to the system using login # noqa: E501

    :param login: User login
    :type login: str

    :rtype: float
    """
    return 'do some magic!'


def logout_post(token=None):  # noqa: E501
    """Logout from the system

     # noqa: E501

    :param token: Token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'
