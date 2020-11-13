
import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.models import db, User
from werkzeug.security import generate_password_hash
from unittest.mock import patch

"""
This file defines all unit tests for the login page
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend'),
    balance=200
)

class FrontEndLoginPageTest(BaseCase):
    """
    A class that contains the unit tests for the login page
    """

    def test_no_login(self):
        """
         R1.1: if the user hasn’t logged in, show the login page
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # since the user is logged out, they should be redirected to the log-in page
        self.assert_element("#log-in")

    def test_login_page_message(self):
        """
         R1.2: The login page has a message that by default says ‘please login’

        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # message element must say "please login"
        self.assert_text("Please login", "#message")

        # reset
        self.open(base_url + '/logout')

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_login_page_success(self, *_):
        """
         R1.3: If the user has logged in, redirect to the user profile page

        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # Enter test_user’s email into element #email
        self.type("#email", "test_frontend@test.com")

        # Enter test_user’s password into element #password
        self.type("#password", generate_password_hash('test_frontend'))

        # Click element input[type = “submit”]
        self.click('input[type="submit"]')

        self.assert_element("#welcome")

        # reset
        self.open(base_url + '/logout')


    def test_login_page_contains_email_and_password(self):
        """
        R1.4 The login page provides a login form which requests two field: email and password

        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # validate that the login contains an email field
        self.assert_element("#email")

        # validate that the login contains an password field

        self.assert_element("#password")

        # reset
        self.open(base_url + '/logout')

