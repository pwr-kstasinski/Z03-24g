# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestLoginController(BaseTestCase):
    """LoginController integration test stubs"""

    def test_login_post(self):
        """Test case for login_post

        Login to system
        """
        query_string = [('login', 'login_example')]
        response = self.client.open(
            '//login',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_post(self):
        """Test case for logout_post

        Logout from the system
        """
        query_string = [('token', 'token_example')]
        response = self.client.open(
            '//logout',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
