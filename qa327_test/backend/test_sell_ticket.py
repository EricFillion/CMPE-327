"""
Whitebox tests for the `sell_ticket` backend function.
"""

from datetime import date
from seleniumbase import BaseCase
from sqlalchemy.orm.session import make_transient

from qa327.backend import sell_ticket
from qa327.models import db, User, Ticket
from qa327_test.common import TEST_USER

class BackEndSellTicketTest(BaseCase):
    """
    Testing backend function `sell_ticket` using data interface coverage.
    """
    def test_sell_ticket_valid_no_fraction(self):
        """
        All inputs valid, price with no fractional part | user=&lt;user in DB> name="Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | No error
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = new_user
        name = "Unique"
        quantity = 1
        price = 10.00
        expiryDate = date(2030, 1, 1)
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == False
    def test_sell_ticket_valid_with_fraction(self):
        """
        All inputs valid, price with fractional part | user=&lt;user in DB> name="Unique" quantity=1 price=12.34 expiryDate=date(2030, 1, 1) | No error
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = new_user
        name = "Unique"
        quantity = 1
        price = 12.34
        expiryDate = date(2030, 1, 1)
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == False
    def test_sell_ticket_user_not_in_db(self):
        """
        User object that doesn't exist in database | user=&lt;user not in DB> name="Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: user does not exist in database
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        # Skip adding new_user to DB
        # Set up parameters
        user = new_user
        name = "Unique"
        quantity = 1
        price = 10.00
        expiryDate = date(2030, 1, 1)
        # Call function
        print(User.query.all())
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        print(User.query.all())
        assert ret_value == "Internal Error: user does not exist in database"
    def test_sell_ticket_user_bad_type(self):
        """
        Non-User type user parameter | user=None name="Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: 'user' must be of type 'User'
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = None
        name = "Unique"
        quantity = 1
        price = 10.00
        expiryDate = date(2030, 1, 1)
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == "Internal Error: 'user' must be of type 'User'"
    def test_sell_ticket_duplicate_name(self):
        """
        Duplicate name | user=&lt;user in DB> name="Not Unique" quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Error: "A ticket with that name already exists."
        """
        # The most straightforward way to have a ticket with a duplicate name
        # is to just insert the same ticket into the DB twice.
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = new_user
        name = "Not Unique"
        quantity = 1
        price = 10.00
        expiryDate = date(2030, 1, 1)
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == False
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == "A ticket with that name already exists."
    def test_sell_ticket_name_bad_type(self):
        """
        Non-str type name parameter | user=&lt;user in DB> name=None quantity=1 price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: 'name' must be of type 'str'
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = new_user
        name = None
        quantity = 1
        price = 10.00
        expiryDate = date(2030, 1, 1)
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == "Internal Error: 'name' must be of type 'str'"
    def test_sell_ticket_quantity_bad_type(self):
        """
        Non-int type quantity parameter | user=&lt;user in DB> name="Unique" quantity=None price=10.00 expiryDate=date(2030, 1, 1) | Internal Error: 'quantity' must be of type 'int'
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = new_user
        name = "Unique"
        quantity = None
        price = 10.00
        expiryDate = date(2030, 1, 1)
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == "Internal Error: 'quantity' must be of type 'int'"
    def test_sell_ticket_price_bad_type(self):
        """
        Non-float type price parameter | user=&lt;user in DB> name="Unique" quantity=1 price=None expiryDate=date(2030, 1, 1) | Internal Error: 'price' must be of type 'float'
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = new_user
        name = "Unique"
        quantity = 1
        price = None
        expiryDate = date(2030, 1, 1)
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == "Internal Error: 'price' must be of type 'float'"
    def test_sell_ticket_expiryDate_bad_type(self):
        """
        Non-date type expiryDate parameter | user=&lt;user in DB> name="Unique" quantity=1 price=10.00 expiryDate=None | Internal Error: 'expiryDate' must be of type 'date'
        """
        # Prepare DB
        new_user = User()
        new_user.name = TEST_USER.name
        new_user.email = TEST_USER.email
        new_user.password = TEST_USER.password
        new_user.balance = TEST_USER.balance
        db.session.add(new_user)
        db.session.commit()
        # Set up parameters
        user = new_user
        name = "Unique"
        quantity = 1
        price = 10.00
        expiryDate = None
        # Call function
        ret_value = sell_ticket(user, name, quantity, price, expiryDate)
        # Check return value
        assert ret_value == "Internal Error: 'expiryDate' must be of type 'date'"
