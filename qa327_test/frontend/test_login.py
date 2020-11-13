
import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.models import db, User
from werkzeug.security import generate_password_hash

"""
This file defines all unit tests for the login page
"""

# Mock a sample user
test_user = User(
    email='testFrontend@test.com',
    name='testFrontend',
    password=generate_password_hash('testFrontend'),
    balance=200
)

class FrontEndLoginPageTest(BaseCase):
    """
    A class that contains the unit tests for the login page
    """

    def test_login_success(self, *_):
        """
         R1.1: if the user hasn’t logged in, show the login page
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # since the user is logged out, they should be redirected to the log-in page
        self.assert_element("#log-in")
