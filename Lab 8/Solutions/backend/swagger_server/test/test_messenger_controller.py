# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.object import Object  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMessengerController(BaseTestCase):
    """MessengerController integration test stubs"""

    def test_receive_get(self):
        """Test case for receive_get

        Receives messages
        """
        query_string = [('token', 56),
                        ('nadawca', 'nadawca_example')]
        response = self.client.open(
            '//receive',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_receivers_get(self):
        """Test case for receivers_get

        List all receivers
        """
        response = self.client.open(
            '//receivers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_post(self):
        """Test case for send_post

        Sends message
        """
        query_string = [('token', 56),
                        ('receiver', 'receiver_example'),
                        ('message', 'message_example')]
        response = self.client.open(
            '//send',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
