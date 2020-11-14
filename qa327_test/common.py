"""
qa327_test/common.py:
A shared space for any common testing code/data.
"""
from unittest.mock import patch
from werkzeug.security import generate_password_hash

from qa327_test.conftest import base_url
from qa327.models import User

# Mock a sample user
TEST_USER = User(
    email='test_frontend@example.com',
    name='Test Frontend',
    balance=2000
)
TEST_USER.raw_password = 'q1w2e3Q!W@E#'
TEST_USER.password = generate_password_hash(TEST_USER.raw_password)

def auto_login(user):
    """
    Function decorator which will automatically log-in a given user.
    This includes patching the backend functions so that they will
    always use this specific user.
    """
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
        patched_1 = patch('qa327.backend.get_user', return_value=user)(wrapped)
        patched_2 = patch('qa327.backend.login_user', return_value=user)(patched_1)
        return patched_2
    return generate_wrapper
