from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from qa327_test.common import auto_login, TEST_USER as test_user

import requests


class RegisterTest(BaseCase):

    @auto_login(test_user)
    def test_register_logged_in_redirect(self, *_):
        """
        R2.1 If the user has logged in, redirect back to the user profile page /
        """
        # Login and user mocking is handled with the common login decorator
        # Open `/register`
        self.open(base_url + '/register')
        # Validate that the current page has been redirected to /
        self.assert_equal(self.get_current_url(), base_url + '/')
        # logout to clear session
        self.open(base_url + '/logout')

    def test_show_register_page(self):
        '''
        R2.2 R2.3
        show the user registration page the registration page shows a registration form requesting: email, user name, password, password2
        '''
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

    def test_if_email_empty(self):
        """
        R2.4.1 test email not empty validation
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # email empty
        self.type("#email", " ")
        # input name
        self.type("#name", "Joe")
        # input valid password
        self.type("#password", "J12345678a!")
        # input valid password2
        self.type("#password2", "J12345678a!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: email/password format is incorrect.
        self.assert_text("email/password format is incorrect.", "#message")

    def test_if_password_empty(self):
        """
        R2.4.2 test password not empty valdiation
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # input valid email
        self.type("#email", "joe1@qq.com")
        # input valid name
        self.type("#name", "Joe")
        # password empty
        self.type("#password", " ")
        # password2 empty
        self.type("#password2", " ")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: email/password format is incorrect.
        self.assert_text("email/password format is incorrect.", "#message")

    def test_if_email_not_follow_rule(self):
        """
        R2.4.3 Email has to follow addr-spec defined in RFC 5322
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # email not follow rule
        self.type("#email", "Abc.example.com")
        # input valid name
        self.type("#name", "Joe")
        # input valid password
        self.type("#password", "J12345678a!")
        # input valid password2
        self.type("#password2", "J12345678a!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: email/password format is incorrect.
        self.assert_text("email/password format is incorrect.", "#message")

    def test_password_have_enough_length(self):
        """
        R2.4.4.1 Password has a minimum length of 6
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # input valid email
        self.type("#email", "Abc@example.com")
        # input valid name
        self.type("#name", "Joe")
        # password not follow rule
        self.type("#password", "Ja12!")
        # password2 not follow rule
        self.type("#password2", "Ja12!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: email/password format is incorrect.
        self.assert_text("email/password format is incorrect.", "#message")

    def test_password_have_uppercase(self):
        """
        R2.4.4.2 Password has at least one upper case
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "Abc@example.com")
        self.type("#name", "Joe")
        # no uppercase password
        self.type("#password", "aa12!aaaa")
        # no uppercase password2
        self.type("#password2", "aa12!aaaa")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: email/password format is incorrect.
        self.assert_text("email/password format is incorrect.", "#message")

    def test_password_have_lowercase(self):
        """
        R2.4.4.3 Password has at least one lower case
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # input valid email
        self.type("#email", "Abc@example.com")
        self.type("#name", "Joe")
        # password should have lowercase
        self.type("#password", "JJJ12!1")
        # password2 same as password
        self.type("#password2", "JJJ12!1")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: email/password format is incorrect.
        self.assert_text("email/password format is incorrect.", "#message")

    def test_password_have_special_letter(self):
        """
        R2.4.4.4 Password has at least one special letter
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # input valid email
        self.type("#email", "Abc@example.com")
        self.type("#name", "Joe")
        # password need with special character
        self.type("#password", "JJJ12aa")
        # input same password2 as password
        self.type("#password2", "JJJ12aa")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: email/password format is incorrect.
        self.assert_text("email/password format is incorrect.", "#message")

    def test_if_username_empty(self):
        """
        R2.5.1 User name has to be non-empty
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # input valid email
        self.type("#email", "2754272@qq.com")
        # user name empty
        self.type("#name", " ")
        # input valid password
        self.type("#password", "test_frontend1T!")
        # input valid password2
        self.type("#password2", "test_frontend1T!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: username format is incorrect.
        self.assert_text("username format is incorrect.", "#message")

    def test_if_username_alphanumeric_only(self):
        """
        R2.5.2 User name has to be alphanumeric
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # input valid email
        self.type("#email", "2754272@qq.com")
        # name should be alphanumeric only
        self.type("#name", "!!!!!")
        # input valid password
        self.type("#password", "test_frontend1T!")
        # input valid password2
        self.type("#password2", "test_frontend1T!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: username format is incorrect.
        self.assert_text("username format is incorrect.", "#message")

    def test_username_trim(self):
        """
        R2.5.3 Allow spaces for the user name if the space is not the first or last character
        """
        # logout first ensure not in login state
        self.open(base_url+'/logout')
        # goto register page
        self.open(base_url+'/register')
        # input valid email
        self.type("#email", "2754272@qq.com")
        # username contain space in the end
        self.type("#name", "Jaa2   ")
        # input valid password
        self.type("#password", "test_frontend1T!")
        # input valid password2
        self.type("#password2", "test_frontend1T!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: username format is incorrect.
        self.assert_text("username format is incorrect.", "#message")

    @patch('qa327.backend.get_user', return_value=test_user)
    def test_registered_before(self, *_):
        """
        R2.6 If the email already exists, show message 'this email has been ALREADY used'
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # input valid password
        self.type("#email", test_user.email)
        self.type("#name", "test_frontend")
        # input valid password
        self.type("#password", "test_frontend1T!")
        # input valid password2
        self.type("#password2", "test_frontend1T!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: this email has been ALREADY used
        self.assert_text("this email has been ALREADY used", "#message")

    def test_username_length_least_length(self):
        """
        R2.7.1 User name has to be longer than 2 characters
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # type a correct email
        self.type("#email", "test_frontend1@test.com")
        # username length less than 2
        self.type("#name", "t")
        # input valid password
        self.type("#password", "test_frontend1T!")
        # input valid password2
        self.type("#password2", "test_frontend1T!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: username format is incorrect.
        self.assert_text("username format is incorrect.", "#message")

    def test_username_max_length(self):
        """
        R2.7.2 User name has to be less than 20 characters
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "test_frontend1@test.com")
        # name over 20 characters
        self.type("#name", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        # input valid password
        self.type("#password", "test_frontend1T!")
        # input valid password2
        self.type("#password2", "test_frontend1T!")
        # send POST request
        self.click('input[type="submit"]')
        # should have message: username format is incorrect.
        self.assert_text("username format is incorrect.", "#message")

    def test_password_repeat(self):
        """
        R2.8 The two inputted passwords must match
        """
        # open logout to ensure user is logout
        self.open(base_url+'/logout')
        # open register page
        self.open(base_url+'/register')
        # if R2.2 R2.3 not fail, then type all the fields in register page
        self.type("#email", "test_frontend1@test.com")
        # input valid name
        self.type("#name", "aaaa")
        # input valid password
        self.type("#password", "test_frontend1T!")
        # input different password2
        self.type("#password2", "eeeeee")
        # send POST request
        self.click('input[type="submit"]')
        # should find error message
        self.assert_element("#message")
        # should have message:The passwords do not match
        self.assert_text("The passwords do not match", "#message")

    @patch('qa327.backend.get_user', return_value=None)
    @patch('qa327.backend.register_user', return_value=test_user)
    def test_register_post_request(self, *_):
            """
            R2.9 The registration form can be submitted as a POST request to the current URL (/register)
            """
            # Open /logout to ensure user is logout
            self.open(base_url+'/logout')
            # Open `/register`
            self.open(base_url+'/register')
            # Validate the existence of a form with attribute method equal to 'post'
            element = self.find_element("form")

            # assert that the above element method attribute is equal to "post"
            assert element.get_attribute("method") == "post"

            # assert that the above element action attribute is equal to the bas_url plus "/register"
            assert element.get_attribute("action") == base_url + "/register"
            # previous made by @jolene, but not work on @joe side
            # self.assert_element("//form[@method='post']")
            # Validate the existence of a form with attribute action equal to '/register'
            # self.assert_element("//form[@action='/register']")
            # Test user's data that will be used for server request
            # data = {
            #             'email': test_user.email, 
            #             'name':test_user.name,
            #             'password': test_user.password
            #         }
            # Make a post request to \register
            # r = requests.post(self.get_current_url(), data)
            # Confirm that the server accepts the requests and with status code 200
            # self.assert_equal(r.status_code, 200)
 
    @patch('qa327.backend.get_user', return_value=None)
    @patch('qa327.backend.register_user', return_value=test_user)
    def test_register_success(self, *_):
        """
        R2. 10 If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page
        """
        # Open /logout to ensure user is logout
        self.open(base_url+'/logout')
        # Open register page
        self.open(base_url+'/register')
        # Enter testuser's email into element #email
        self.type("#email", test_user.email)
        # Enter testuser's name" into element #name
        self.type("#name", test_user.name)
        # Enter testuser's password into element #password
        self.type("#password", test_user.raw_password)
        # Enter testuser's password into element #password2
        self.type("#password2", test_user.raw_password)
        # Click element input[type = “submit”]
        self.click('input[type="submit"]')
        # Validate that the current page has been redirected to /login
        self.assert_equal(self.get_current_url(), base_url + '/login')
