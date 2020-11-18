
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

        # logout to clear session
        self.open(base_url + '/logout')


    @patch('qa327.backend.login_user', return_value=TEST_USER)
    def test_login_page_success(self, *_):
        """
         R1.3: If the user has logged in, redirect to the user profile page
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

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # logout to clear session
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

        # logout to clear session
        self.open(base_url + '/logout')


    def test_login_page_submit_as_post(self):
        """
        R1.5 The login form can be submitted as a post request to the current URL (/login)
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # find element with id = "form"
        element = self.find_element("form")

        # assert that the above element method attribute is equal to "post"
        assert(element.get_attribute("method") == "post")

        # assert that the above element action attribute is equal to the bas_url plus "/login"
        assert(element.get_attribute("action") == base_url + "/login")

        # logout to clear session
        self.open(base_url + '/logout')


    def test_login_page_email_not_empty(self):
        """
        R1.6.1 : Email cannot be empty:
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # Enter a blank string into element #email

        self.type("#email", " ")

        # Enter test_user’s password into element #password
        self.type("#password",  TEST_USER.raw_password)

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")

        # logout to clear session
        self.open(base_url + '/logout')


    def test_login_page_password_not_empty(self):
        """
        R1.6.2 : Password cannot be empty:
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # Enter test_user’s email
        self.type("#email", "test_frontend@test.com")

        self.type("#password",
                  " ")

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")

        # logout to clear session
        self.open(base_url + '/logout')



    def test_login_page_email_format_n_1(self):
        """
        R1.7.1 : Password cannot start with a period:
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # Enter a blank string into element #email
        self.type("#email", ".test@gmail.com")

        # Enter test_user’s password into element #password
        self.type("#password",
                   TEST_USER.raw_password)

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")

        # logout to clear session
        self.open(base_url + '/logout')


    def test_login_page_email_format_n_2(self):
        """
        R1.7.2 : Email must have an @ symbol
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # Enter a blank string into element #email
        self.type("#email", "testgmail.com")

        # Enter test_user’s password into element #password
        self.type("#password",
                   TEST_USER.raw_password)

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")

        # logout to clear session
        self.open(base_url + '/logout')


    def test_login_page_email_format_n_3(self):
        """
        R1.7.3 : Email cannot have an "!" symbol
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # Enter a blank string into element #email
        self.type("#email", "tes!tgmail.com")

        # Enter test_user’s password into element #password
        self.type("#password",
                  TEST_USER.raw_password)

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")

        self.open(base_url + '/logout')


    def test_login_page_email_format_n_4(self):
        """
        R1.7.4 : Email must send with a domain name
        """
        # open /logout to ensure that the user is logged out
        self.open(base_url + '/logout')

        # open login page
        self.open(base_url + '/login')

        # Enter a blank string into element #email
        self.type("#email", "test@gmail")

        # Enter test_user’s password into element #password
        self.type("#password",
                  TEST_USER.raw_password)

        # Press submit button
        self.click('input[type="submit"]')

        # Assert that the proper warning message is displayed
        self.assert_text("email/password format is incorrect.", "#message")

        self.open(base_url + '/logout')


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
