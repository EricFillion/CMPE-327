from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from qa327_test.common import auto_login, test_user
class FrontEndAutoLoginTest(BaseCase):
    @auto_login(test_user)
    def test_auto_login(self, *_):
        self.open(base_url + '/')
        # Wait up to 3 seconds for page to be ready
        self.wait_for_ready_state_complete(timeout=3)
        # After waiting, ensure we are still at homepage (not redirected to login)
        self.assert_equal(self.get_current_url(), base_url + '/')
