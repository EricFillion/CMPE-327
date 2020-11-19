"""
This file defines all unit tests for the 404 page
"""
from seleniumbase import BaseCase
from qa327_test.conftest import base_url

class Error404PageTest(BaseCase):
    """
    A class that contains the unit tests for the 404 page
    """
    def test_8_1_1_get_nonexistent(self):
        """
        R8.1.1 - For any requests except those in the specification's routes table,
        the system should return a 404 error
        (GET, non-existent page)
        """
        # - Open `/logout` (to invalidate any previous session)
        self.open(base_url + '/logout')
        # - Open `/nonexistent-page`
        self.open(base_url + '/nonexistent-page')
        # - Validate that the resulting page contains the text '404'
        self.assert_text('404')
        # - Validate that the resulting page contains the text 'error'
        self.assert_text('error')

    def test_8_1_2_get_on_post_only(self):
        """
        R8.1.2 - For any requests except those in the specification's routes table,
        the system should return a 404 error
        (GET on POST-only pages)
        """
        # - Open `/logout` (to invalidate any previous session)
        self.open(base_url + '/logout')
        # - Open `/sell`
        self.open(base_url + '/sell')
        # - Validate that the resulting page contains the text '404'
        self.assert_text('404')
        # - Validate that the resulting page contains the text 'error'
        self.assert_text('error')
        # - Open `/update`
        self.open(base_url + '/update')
        # - Validate that the resulting page contains the text '404'
        self.assert_text('404')
        # - Validate that the resulting page contains the text 'error'
        self.assert_text('error')
        # - Open `/buy`
        self.open(base_url + '/buy')
        # - Validate that the resulting page contains the text '404'
        self.assert_text('404')
        # - Validate that the resulting page contains the text 'error'
        self.assert_text('error')
