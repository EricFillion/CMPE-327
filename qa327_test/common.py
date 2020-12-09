"""
qa327_test/common.py:
A shared space for any common testing code/data.
"""
from datetime import date
from unittest.mock import patch
from werkzeug.security import generate_password_hash

from qa327_test.conftest import base_url
from qa327.models import User, Ticket

# Mock a sample user
TEST_USER = User(
    email='test_frontend@test.com',
    name='Test Frontend',
    balance=2000
)
TEST_USER.raw_password = 'q1w2e3Q!W@E#'
TEST_USER.password = generate_password_hash(TEST_USER.raw_password)

# Mock a sample ticket
TEST_TICKET = Ticket(
    name="t1",
    quantity=90,
    price=1500,
    expiry=date(2030, 1, 1),
    owner_id="test_owener_id",
    owner=TEST_USER,
)
TEST_TICKET.raw_expiry = "20301001"

def auto_login(user):
    """
    Function decorator which will automatically log-in a given user.
    This includes patching the backend functions so that they will
    always use this specific user.
    """
    # In order to make a function decorator taking a parameter, we need to
    # return a function that, when called with another function F as the
    # parameter, will return F but decorated with our special functionality.
    def generate_wrapper(func):
        def wrapped(self, *args, **kwargs):
            # Open `/logout` (to invalidate any previous session)
            self.open(base_url + '/logout')
            # Open `/login`
            self.open(base_url + '/login')
            # Enter given user's email into element `#email`
            self.type("#email", user.email)
            # Enter given user's password into element `#password`
            self.type("#password", user.raw_password)
            # Click element `input[type='submit']`
            self.click('input[type="submit"]')

            # Call user testing function, preserving any return value
            return_value = func(self, *args, **kwargs)

            # Open `/logout` (cleanup)
            self.open(base_url + '/logout')

            return return_value
        # We manually apply the patch function decorators to patch the
        # get_user and login_user objects. This means the caller can simply
        # decorate with:
        #   @auto_login(...)
        # instead of having to do:
        #   @auto_login(...)
        #   @patch(...)
        #   @patch(...)
        patched_1 = patch('qa327.backend.get_user', return_value=user)(wrapped)
        patched_2 = patch('qa327.backend.login_user', return_value=user)(patched_1)
        return patched_2
    return generate_wrapper
