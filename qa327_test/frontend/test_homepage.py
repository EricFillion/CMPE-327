from unittest.mock import patch
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327_test.common import test_user, login

"""
This file defines all unit tests for the login page
"""

class FrontEndHomepageTest(BaseCase):
    """
    A class that contains the unit tests for the homepage
    """

    def test_3_1_not_logged_in(self):
        """
        R3.1: If the user is not logged in, redirect to login page
        """
        # - Open `/logout` (to invalidate any previous session)
        self.open(base_url + '/logout')
        # - Open `/`
        self.open(base_url + '/')
        # - Sleep 3 seconds, then validate that we're on the login page by checking for `#log-in`
        self.assert_element("#log-in")
    
    @login(test_user)
    def test_3_2_welcome_header(self, *_):
        """
        R3.2: This page shows a header 'Hi {}'.format(user.name)
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page shows element `#welcome` with text: `'Hi {}'.format(user.name)`
        self.assert_text("Hi {}!".format(test_user.name), "#welcome")
        # - Open `/logout` (cleanup)
        self.open(base_url + '/logout')

