"""
This file defines integration test I2
"""

from unittest.mock import patch
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327_test.common import TEST_USER, TEST_TICKET
from qa327.models import User, Ticket, db
from datetime import date, timedelta

class IntegrationPurchaseTicketTest(BaseCase):
    """
    A class that contains the integration test which purchases a ticket
    through the app
    """

    def test_integration_purchase_ticket(self):
        """
        This testcase follows a complete userflow through ticket purchase
        """
        # ### Overview of major steps
        # 1. User registers
        # 2. User logs in
        # 3. User buys ticket
        # 4. User logs out
        # ### Notes
        # - The TEST_USER defined in `qa327_test/common.py` will be used throughout this test
        # - An additional test user `TEST_SELLER` will be manually added to the database to serve as the user who posted the ticket
        #     - Email: "test_seller@test.com"
        #     - Name: "Test Seller"
        #     - Password: None (we will not login as this user, so it is not necessary to set their password)
        #     - Balance: 0 (they will not need to spend any balance)
        TEST_SELLER = User(
            email="test_seller@test.com",
            name="Test Seller",
            password="",
            balance=0
        )
        # - An additional test ticket "TEST_SELLING_TICKET" will be manually added to the database
        #     - It will be based on the TEST_TICKET provided in common.py, but with the following information changed:
        #     - Owner: `TEST_SELLER`
        #     - Owner ID: [corresponding value for TEST_SELLER, set automatically from code]
        TEST_SELLING_TICKET = Ticket(
            name=TEST_TICKET.name,
            quantity=TEST_TICKET.quantity,
            price=TEST_TICKET.price,
            expiry=TEST_TICKET.expiry,
            owner=TEST_SELLER
        )
        # ### Initialization
        # - Clear all contents from database (done by pytest fixture)
        # - Add "TEST_SELLER" and "TEST_SELLING_TICKET" to database
        db.session.add(TEST_SELLER)
        db.session.add(TEST_SELLING_TICKET)
        db.session.commit()
        # - Open `/logout` to ensure there is no previous session
        self.open(base_url + '/logout')
        # ### 1. User registers (R2.10)
        # - Open `/`
        self.open(base_url + '/')
        # - Validate redirection to `/login`
        self.assert_equal(self.get_current_url(), base_url + '/login')
        # - Click "Register" link (element `a[href="/register"]`)
        self.click('a[href="/register"]')
        # - Enter TEST_USER's name into element `#name`
        self.type("#name", TEST_USER.name)
        # - Enter TEST_USER's email into element `#email`
        self.type("#email", TEST_USER.email)
        # - Enter TEST_USER's password into element `#password`
        self.type("#password", TEST_USER.raw_password)
        # - Enter TEST_USER's password into element `#password2`
        self.type("#password2", TEST_USER.raw_password)
        # - Click "Register" button (element `input[type="submit"]`)
        self.click('input[type="submit"]')
        # - Validate redirection to `/login`
        self.assert_equal(self.get_current_url(), base_url + '/login')
        # ### 2. User logs in (R1.9 + R3.3 for balance validation)
        # - Enter TEST_USER's email into element `#email`
        self.type("#email", TEST_USER.email)
        # - Enter TEST_USER's password into element `#password`
        self.type("#password", TEST_USER.raw_password)
        # - Click "Login" button (element `input[type="submit"]`)
        self.click('input[type="submit"]')
        # - Validate redirection to `/`
        self.assert_equal(self.get_current_url(), base_url + '/')
        # - Validate that an element `#balance` shows text `Your balance is $50.00`
        self.assert_text('Your balance is $50.00', selector='#balance')
        # ### 3. User buys ticket (R6.5.1 + R3.5.1 for quantity validation + R3.3 for balance validation)
        # - Enter TEST_SELLING_TICKET's name in the element `#buyform_input_name`
        self.type("#buyform_input_name", TEST_SELLING_TICKET.name)
        # - Enter a quantity of 2 into the element `#buyform_input_quantity`
        self.type("#buyform_input_quantity", str(2))
        # - Click element `#buyform_submit`
        self.click('#buyform_submit')
        # - Validate that an element `.message_info` shows text `Ticket was purchased successfully.`
        self.assert_text('Ticket was purchased successfully.', selector='.message_info')
        # - Find `tr` of ticket by looking up ticket's name under the ticket table
        rows = self.find_elements("table#tickettable tbody tr")
        matching_trs = [row for row in rows if TEST_SELLING_TICKET.name in row.text]
        self.assert_equal(len(matching_trs), 1)
        tr = matching_trs[0]
        # - Validate quantity by looking under the ticket's `tr` and validating that the element `td.tt_quantity` has text: `88`
        self.assert_equal(tr.find_element_by_class_name("tt_quantity").text, "{}".format(88))
        # - Validate that an element `#balance` shows text `Your balance is $8.00`
        self.assert_text('Your balance is $8.00', selector='#balance')
        # ### 4. User logs out (R7.1)
        # - Click element `#logout`
        self.open(base_url + '/logout')
        # - Validate redirection to `/login`
        self.assert_equal(self.get_current_url(), base_url + '/login')
