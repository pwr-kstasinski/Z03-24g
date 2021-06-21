"""
    Messages server

    SAFRSAPI  # noqa: E501

    The version of the OpenAPI document: 0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.users_api import UsersApi  # noqa: E501


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user0(self):
        """Test case for create_user0

        Create User  # noqa: E501
        """
        pass

    def test_delete_userfrom_users0(self):
        """Test case for delete_userfrom_users0

        Delete User from Users  # noqa: E501
        """
        pass

    def test_retrieve_messagefromincomingmessages0(self):
        """Test case for retrieve_messagefromincomingmessages0

        Retrieve Message from incoming_messages  # noqa: E501
        """
        pass

    def test_retrieve_userinstance0(self):
        """Test case for retrieve_userinstance0

        Retrieve User instance  # noqa: E501
        """
        pass

    def test_retrieveacollectionof_userobjects0(self):
        """Test case for retrieveacollectionof_userobjects0

        Retrieve a collection of User objects  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
