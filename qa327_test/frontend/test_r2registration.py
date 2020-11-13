import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
# should not use this test_user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
# this mock user should be OK
test_user2 = User(
    email='1820@qq.com',
    name='kkkkk',
    password=generate_password_hash('Koj1230!')
)


class RegisterTest(BaseCase):

    """
    R2.2 R2.3 otherwise, 
    show the user registration page the registration page shows a registration form requesting: email, user name, password, password2
    """

    def test_show_register_page(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # check current url
        self.assertEqual(self.get_current_url(), base_url+'/register')
        # check the existence of element email
        self.assert_element("#email")
        # check the existence of element name
        self.assert_element("#name")
        # check the existence of element password
        self.assert_element("#password")
        # check the existence of element password2
        self.assert_element("#password2")

    """
    R2.4.1 test email not empty validation
    """

    def test_if_email_empty(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        # email empty
        self.type("#email", " ")
        self.type("#name", "Joe")
        self.type("#password", "J12345678a!")
        self.type("#password2", "J12345678a!")
        # send POST request
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.4.2 test password not empty valdiation
    """

    def test_if_password_empty(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "joe1@qq.com")
        self.type("#name", "Joe")
        # password empty
        self.type("#password", " ")
        self.type("#password2", " ")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.4.3.1 Email has to follow addr-spec defined in RFC 5322
    """

    def test_if_email_not_follow_rule(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        # email not follow rule
        self.type("#email", "Abc.example.com")
        self.type("#name", "Joe")
        self.type("#password", "J12345678a!")
        self.type("#password2", "J12345678a!")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")
    """
    R2.4.4.1 Password has minimum length 6
    """

    def test_password_have_enough_length(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "Abc.@example.com")
        self.type("#name", "Joe")
        # password not follow rule
        self.type("#password", "Ja12!")
        self.type("#password2", "Ja12!")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.4.4.2 Password has at least one upper case
    """

    def test_password_have_uppercase(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "Abc.@example.com")
        self.type("#name", "Joe")
        # no uppercase password
        self.type("#password", "aa12!aaaa")
        self.type("#password2", "aa12!aaaa")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.4.4.3 Password has at least one lower case
    """

    def test_password_have_lowercase(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "Abc.@example.com")
        self.type("#name", "Joe")
        # password should have lowercase
        self.type("#password", "JJJ12!1")
        self.type("#password2", "JJJ12!1")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.4.4.4 Password has at least one special letter
    """

    def test_password_have_special_letter(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "Abc.@example.com")
        self.type("#name", "Joe")
        # password need with special character
        self.type("#password", "JJJ12aa")
        self.type("#password2", "JJJ12aa")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.5.1 User name has to be non-empty
    """

    def test_if_username_empty(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "2754272@qq.com")
        # user name empty
        self.type("#name", " ")
        self.type("#password", "test_frontend1T!")
        self.type("#password2", "test_frontend1T!")
        self.click('input[type="submit"]')
       # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.5.2 User name has to be alphanumeric-only
    """

    def test_if_username_alphanumeric_only(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "2754272@qq.com")
        # name should be alphanumeric only
        self.type("#name", "!!!!!")
        self.type("#password", "test_frontend1T!")
        self.type("#password2", "test_frontend1T!")
        self.click('input[type="submit"]')
       # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.5.3 User name has to be space allowed only if it is not the first or the last character
    """

    def test_username_trim(self, *_):
        self.open(base_url+'/logout')
        self.open(base_url+'/register')
        self.type("#email", "2754272@qq.com")
        self.type("#name", "Jaa2   ")
        self.type("#password", "test_frontend1T!")
        self.type("#password2", "test_frontend1T!")
        self.click('input[type="submit"]')
       # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.6 If the email already exists, show message 'this email has been ALREADY used'
    """
    @patch('qa327.backend.get_user', return_value=test_user)
    def test_registered_before(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "test_frontend@test.com")
        self.type("#name", "test_frontend")
        self.type("#password", "test_frontend1T!")
        self.type("#password2", "test_frontend1T!")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: this email has been ALREADY used
        self.assert_text("this email has been ALREADY used", "#message")

    """
    R2.7.1 User name has to be longer than 2 characters
    """

    def test_username_length_least_length(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "test_frontend1@test.com")
        # username length
        self.type("#name", "t")
        self.type("#password", "test_frontend1T!")
        self.type("#password2", "test_frontend1T!")
        self.click('input[type="submit"]')
       # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.7.2 User name has to be less than 20 characters
    """

    def test_username_max_length(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "test_frontend1@test.com")
        # name over 20 characters
        self.type("#name", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        self.type("#password", "test_frontend1T!")
        self.type("#password2", "test_frontend1T!")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message: email/password format incorrect
        self.assert_text("email/password format incorrect", "#message")

    """
    R2.8 test password repeat validation
    """

    def test_password_repeat(self, *_):
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "test_frontend1@test.com")
        self.type("#name", "aaaaa")
        self.type("#password", "test_frontend1T!")
        self.type("#password2", "eeeeee")
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message:The passwords do not match
        self.assert_text("The passwords do not match", "#message")
