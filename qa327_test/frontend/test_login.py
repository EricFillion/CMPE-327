
import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.models import db, User
from werkzeug.security import generate_password_hash
from unittest.mock import patch
from qa327_test.common import auto_login, TEST_USER

"""
This file defines all unit tests for the login page
"""

class FrontEndLoginPageTest(BaseCase):
    """
    A class that contains the unit tests for the login page
    """

    def test_login_success(self):
        """
         R1.1: if the user hasn’t logged in, show the login page
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # since the user is logged out, they should be redirected to the log-in page
        self.assert_element("#log-in")


    def test_login_page_password_too_short(self):
        """
         R1.8.1 Password must be at least 6 characters
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # fill email and password 
        self.type("#email", TEST_USER.email)
        self.type("#password", "A#cde")

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")
       
        # logout to clear session
        self.open(base_url + '/logout')

    def test_login_page_password_contain_lowercase(self):
        """
         R1.8.2 Password must contains one lower case
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # fill email and password 
        self.type("#email", TEST_USER.email)
        self.type("#password", "A#CDEF")

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")
        
        # logout to clear session
        self.open(base_url + '/logout')

    def test_login_page_password_contain_special_char(self):
        """
         R1.8.3 Password must contains one special character
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')

        # fill email and password and click submit
        self.type("#email", TEST_USER.email)
        self.type("#password", "Abcdef")

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")

         # logout to clear session
        self.open(base_url + '/logout')

    def test_login_page_password_contain_uppercase(self):
        """
         R1.8.4 Password must contains one upper case
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')

        # fill email and password and click submit
        self.type("#email", TEST_USER.email)
        self.type("#password", "a#cdef")

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")
        
        # logout to clear session
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.login_user', return_value=TEST_USER)
    def test_login_correct_email_and_password(self, *_):
        """
         R1.9: If email/password are correct, redirect to /
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # fill email and password and click submit
        self.type("#email", TEST_USER.email)
        self.type("#password", TEST_USER.raw_password)

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the welcome header is displayed
        self.assert_element("#welcome")
        
        # logout to clear session
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_user', return_value=TEST_USER)
    def test_login_redirect(self, *_):
        """
         R1.10: If email/password are not correct, redirect to /login 
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # fill email and password and click submit
        self.type("#email", TEST_USER.email)
        self.type("#password", "W$ongpassword")

        # Press submit button
        self.click('input[type="submit"]')
        
        # Assert that the proper warning message is displayed
        self.assert_text("email/password combination incorrect", "#message")
        
        # Validate that current page is “/login”
        self.assert_equal(self.get_current_url(), base_url + '/login')

        # logout to clear session
        self.open(base_url + '/logout')


