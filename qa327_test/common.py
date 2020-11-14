from unittest.mock import patch

from qa327_test.conftest import base_url
from qa327.models import db, User
from werkzeug.security import generate_password_hash

# Mock a sample user
test_user = User(
    email='test_frontend@example.com',
    name='Test Frontend',
    balance=2000
)
test_user.raw_password = 'q1w2e3Q!W@E#'
test_user.password = generate_password_hash(test_user.raw_password)

def auto_login(user):
    def generate_wrapper(fn):
        def wrapped(self, *args, **kwargs):
            # - Open `/logout` (to invalidate any previous session)
            self.open(base_url + '/logout')
            # - Open `/login`
            self.open(base_url + '/login')
            # - Enter test_user's email into element `#email`
            self.type("#email", user.email)
            # - Enter test_user's password into element `#password`
            self.type("#password", user.raw_password)
            # - Click element `input[type='submit']`
            self.click('input[type="submit"]')

            # Call user testing function, preserving any return value
            return_value = fn(self, *args, **kwargs)

            # - Open `/logout` (cleanup)
            self.open(base_url + '/logout')

            return return_value
        p1 = patch('qa327.backend.get_user', return_value=user)(wrapped)
        p2 = patch('qa327.backend.login_user', return_value=user)(p1)
        return p2
    return generate_wrapper
