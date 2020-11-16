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
            self.assert_element("//form[@method='post']")
            # Validate the existence of a form with attribute action equal to '/register'
            self.assert_element("//form[@action='/register']")
            # Test user's data that will be used for server request
            data = {
                        'email': test_user.email, 
                        'name':test_user.name,
                        'password': test_user.password
                    }
            # Make a post request to \register
            r = requests.post(self.get_current_url(), data)
            # Confirm that the server accepts the requests and with status code 200
            self.assert_equal(r.status_code, 200)
 
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
   