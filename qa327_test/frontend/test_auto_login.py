"""
qa327_test/frontend/test_auto_login.py:
A single test verifying the correct operation of the common auto_login function.
"""
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from qa327_test.common import auto_login, TEST_USER
class FrontEndAutoLoginTest(BaseCase):
    """
    Class containing test cases for the auto_login function.
    """
    @auto_login(TEST_USER)
    def test_auto_login(self, *_):
        """
        Test the auto_login function decorator.
        This doesn't follow any specific requirement, although it may duplicate
        some of the login testing.
        """
        self.open(base_url + '/')
        # Wait up to 3 seconds for page to be ready
        self.wait_for_ready_state_complete(timeout=3)
        # After waiting, ensure we are still at homepage (not redirected to login)
        self.assert_equal(self.get_current_url(), base_url + '/')
