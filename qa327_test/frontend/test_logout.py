import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327_test.common import TEST_USER
class FrontEndLogoutTest(BaseCase):
    @patch('qa327.backend.get_user', return_value=TEST_USER)
    @patch('qa327.backend.login_user', return_value=TEST_USER)
    def test_logout(self,*_):
        '''
        R7.1 Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.
        '''
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
        
        # since the user is logged out, they should be redirected to the log-in page
        self.assert_element("#log-in")