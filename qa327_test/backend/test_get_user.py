from seleniumbase import BaseCase
from qa327.backend import get_user 
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

class BackEndGetUserTest(BaseCase):
    """
    Testing backend function get_user using input partitioning
    """ 

    def test_get_user_empty_email(self):
        """
        Input Partion: empty email
        """
        user = get_user("")
        self.assert_equal(user,  None)

 
    def test_get_user_invalid_email(self):
        """
        Input Partion: invalid email
        """
        user = get_user("invalid_email")
        self.assert_equal(user,  None)

   
    def test_get_user_nonexistent_email(self):
        """
        Input Partion: nonexistent user email
        """
        # Test is started with clean table. No need to remove data

        #Get user by email and assert equal to the test user 
        user = get_user("nonexistant_user@example.com")
        self.assert_equal(user,  None)

    def test_get_user_valid_email(self):
        """
         Input Partion: valid email
        """
        # Test is started with clean table. No need to remove data
        
        #Add test user to database
        hashed_pw = generate_password_hash('q1w2e3Q!W@E#', method='sha256')
        test_user = User(email='test_backend@example.com', name='Test Email Input', password=hashed_pw, balance=5000)
        db.session.add(test_user)

        #Get user by email and assert equal to the test user 
        user = get_user("test_backend@example.com")
        self.assert_equal(user,  test_user)
        
        #Clean up by deleting test user
        db.session.delete(test_user)