"""
    ChatApp Server API

    This is a simple API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.message_api import MessageApi  # noqa: E501


class TestMessageApi(unittest.TestCase):
    """MessageApi unit test stubs"""

    def setUp(self):
        self.api = MessageApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_username_get(self):
        """Test case for get_username_get

        receiving messages for a specific user  # noqa: E501
        """
        pass

    def test_send_receiver_username_message_post(self):
        """Test case for send_receiver_username_message_post

        sending a message to a specific user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
