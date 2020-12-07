"""
This file defines all unit tests for the login page
"""

from unittest.mock import patch
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327_test.common import TEST_USER, auto_login
from qa327.models import Ticket
from datetime import date, timedelta

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
    
    @auto_login(TEST_USER)
    def test_3_2_welcome_header(self, *_):
        """
        R3.2: This page shows a header 'Hi {}'.format(user.name)
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page shows element `#welcome` with text: `'Hi {}'.format(user.name)`
        self.assert_text("Hi {}!".format(TEST_USER.name), "#welcome")
    
    @auto_login(TEST_USER)
    def test_3_3_balance(self, *_):
        """
        R3.3: This page shows user balance
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page shows element `#balance` with text: `"Your balance is ${:.2f}".format(user.balance)`
        self.assert_text("Your balance is ${:.2f}".format(TEST_USER.balance / 100), "#balance")
    
    @auto_login(TEST_USER)
    def test_3_4_logout_link(self, *_):
        """
        R3.4: This page shows a logout link, pointing to /logout
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page shows element `a#logout` with text "Logout" and `href='/logout'`
        self.assert_text("Logout", "a#logout[href='/logout']")
    
    # - Mock backend.get_all_tickets to create a list of tickets
    #     - Ensure list of tickets is stored for later
    #     - There must be one or more tickets
    #     - All tickets should be valid (not expired)
    TEST_3_5_1_TICKETS=[
        Ticket(name='Test Ticket 1', quantity=3, owner=TEST_USER, price=1000, expiry=date.today()+timedelta(days=1)),
        Ticket(name='Test Ticket 2', quantity=1, owner=TEST_USER, price=1500, expiry=date.today()+timedelta(days=2)),
        Ticket(name='Test Ticket 3', quantity=4, owner=TEST_USER, price=2000, expiry=date.today()+timedelta(days=3)),
    ]
    @patch('qa327.backend.get_all_tickets', return_value=TEST_3_5_1_TICKETS)
    @auto_login(TEST_USER)
    def test_3_5_1_ticket_list_positive(self, *_):
        """
        R3.5.1: This page lists all available tickets.
        Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
        (positive, ensure tickets in database show properly)
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page shows element `table#tickettable`
        self.assert_element("table#tickettable")
        # - Validate that the number of ticket rows (as opposed to header rows) in the ticket table is equal to the number of tickets
        rows = self.find_elements("table#tickettable tbody tr")
        self.assert_equal(len(rows), len(self.TEST_3_5_1_TICKETS))
        # - For each ticket in the list of tickets from the mock backend:
        for ticket in self.TEST_3_5_1_TICKETS:
            # - Find `tr` of ticket by looking up ticket's name under the ticket table
            matching_trs = [row for row in rows if ticket.name in row.text]
            self.assert_equal(len(matching_trs), 1)
            tr = matching_trs[0]
            # - Validate name by looking under the ticket's `tr` and validating that the element `td.tt_name` has text: `"{}".format(ticket.name)`
            self.assert_equal(tr.find_element_by_class_name("tt_name").text, "{}".format(ticket.name))
            # - Validate quantity by looking under the ticket's `tr` and validating that the element `td.tt_quantity` has text: `"{}".format(ticket.quantity)`
            self.assert_equal(tr.find_element_by_class_name("tt_quantity").text, "{}".format(ticket.quantity))
            # - Validate owner's email by looking under the ticket's `tr` and validating that the element `td.tt_owner` has text: `"{}".format(ticket.owner.name)`
            self.assert_equal(tr.find_element_by_class_name("tt_owner").text, "{}".format(ticket.owner.name))
            # - Validate price by looking under the ticket's `tr` and validating that the element `td.tt_price` has text: `"${:.2f}".format(ticket.price / 100)`
            self.assert_equal(tr.find_element_by_class_name("tt_price").text, "${:.2f}".format(ticket.price / 100))

    # - Mock backend.get_all_tickets to create a list of tickets
    #     - Ensure list of tickets is stored for later
    #     - One or more tickets must be valid (not expired)
    #     - One or more tickets must be expired
    TEST_3_5_2_TICKETS=[
        Ticket(name='Test Ticket 1', quantity=3, owner=TEST_USER, price=1000, expiry=date.today()+timedelta(days=1)),
        Ticket(name='Test Ticket 2', quantity=1, owner=TEST_USER, price=1500, expiry=date.today()+timedelta(days=2)),
        Ticket(name='Test Ticket 3', quantity=4, owner=TEST_USER, price=2000, expiry=date.today()+timedelta(days=-3)),
        Ticket(name='Test Ticket 4', quantity=1, owner=TEST_USER, price=2500, expiry=date.today()+timedelta(days=-4)),
    ]
    TEST_3_5_2_INVALID_TICKETS=TEST_3_5_2_TICKETS[2:]
    @patch('qa327.backend.get_all_tickets', return_value=TEST_3_5_2_TICKETS)
    @auto_login(TEST_USER)
    def test_3_5_2_ticket_list_negative_some_tickets_expired(self, *_):
        """
        R3.5.2: This page lists all available tickets.
        Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
        (negative, ensure expired ticket is not displayed)
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page shows element `table#tickettable`
        self.assert_element("table#tickettable")
        # - Validate that the number of ticket rows (as opposed to header rows) in the ticket table is equal to the number of valid tickets
        rows = self.find_elements("table#tickettable tbody tr")
        self.assert_equal(len(rows), len(self.TEST_3_5_2_TICKETS) - len(self.TEST_3_5_2_INVALID_TICKETS))
        # - For each expired ticket in the list of tickets from the mock backend:
        for ticket in self.TEST_3_5_2_INVALID_TICKETS:
            # - Search for `tr` of ticket by looking up ticket's name under the ticket table, and ensure it can not be found
            matching_trs = [row for row in rows if ticket.name in row.text]
            self.assert_equal(len(matching_trs), 0)

    # - Mock backend.get_all_tickets to create a list of tickets
    #     - There must be one or more tickets
    #     - All tickets must be expired
    TEST_3_5_3_TICKETS=[
        Ticket(name='Test Ticket 1', quantity=3, owner=TEST_USER, price=1000, expiry=date.today()+timedelta(days=-2)),
        Ticket(name='Test Ticket 2', quantity=1, owner=TEST_USER, price=1500, expiry=date.today()+timedelta(days=-3)),
    ]
    @patch('qa327.backend.get_all_tickets', return_value=TEST_3_5_3_TICKETS)
    @auto_login(TEST_USER)
    def test_3_5_3_ticket_list_negative_all_tickets_expired(self, *_):
        """
        R3.5.3: This page lists all available tickets.
        Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
        (ensure table is not displayed if there are zero valid tickets)
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page does not show element `table#tickettable`
        self.assert_element_absent("table#tickettable")
        # - Validate that the page does show element `#no_tickets_available`
        self.assert_element("#no_tickets_available")

    # - Mock backend.get_all_tickets to create a list of tickets
    #     - There must be zero tickets
    TEST_3_5_4_TICKETS=[]
    @patch('qa327.backend.get_all_tickets', return_value=TEST_3_5_4_TICKETS)
    @auto_login(TEST_USER)
    def test_3_5_4_ticket_list_negative_no_tickets(self, *_):
        """
        R3.5.4: This page lists all available tickets.
        Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.
        (test case with zero total tickets)
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Validate that the page does not show element `table#tickettable`
        self.assert_element_absent("table#tickettable")
        # - Validate that the page does show element `#no_tickets_available`
        self.assert_element("#no_tickets_available")
    
    @auto_login(TEST_USER)
    def test_3_6_sell__ticket_form(self, *_):
        """
        R3.6: This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
        """
        # Login and user mocking is handled with the common login decorator
        # Open `/`
        self.open(base_url + '/')
        # Validate that the page shows element `#sellform` 
        self.assert_element("#sellform")
        #Validate that the page does show element `#sellform_label_name` with text "Ticket Name:"
        self.assert_text("Ticket Name:", "#sellform_label_name")
        # Validate that the page does show element `#sellform_input_name`
        self.assert_element("#sellform_input_name")
        # Validate that the page does show element `#sellform_label_quantity` with text "Quantity:"
        self.assert_text("Quantity:", "#sellform_label_quantity")
        # Validate that the page does show element `#sellform_input_quantity`
        self.assert_element("#sellform_input_quantity")
        # Validate that the page does show element `#sellform_label_price` with text "Price Per Ticket:"
        self.assert_text("Price Per Ticket:", "#sellform_label_price")
        # Validate that the page does show element `#sellform_input_price`
        self.assert_element("#sellform_input_price")
        # Validate that the page does show element `#sellform_label_expiry` with text "Expiry Date:"
        self.assert_text("Expiry Date (yyyymmdd):", "#sellform_label_expiry")
        # Validate that the page does show element `#sellform_input_expiry
        self.assert_element("#sellform_input_expiry")
        # Validate that the page does show element `input#sellform_submit[action=submit]`
        self.assert_element("#sellform_submit")
        # Open `/logout` (cleanup)
        self.open(base_url + '/logout')

    @auto_login(TEST_USER)
    def test_3_7_buy_ticket_form(self, *_):
        """
        R3.7: This page contains a form that a user can buy new tickets. Fields: name, quantity
        """
        # Login and user mocking is handled with the common login decorator
        # Open `/`
        self.open(base_url + '/')
        # Validate that the page shows element `#buyform` 
        self.assert_element("#buyform")
        #Validate that the page does show element `#buyform_label_name` with text "Ticket Name:"
        self.assert_text("Ticket Name:", "#buyform_label_name")
        # Validate that the page does show element `#buyform_input_name`
        self.assert_element("#buyform_input_name")
        # Validate that the page does show element `#buyform_label_quantity` with text "Quantity:"
        self.assert_text("Quantity:", "#buyform_label_quantity")
        # Validate that the page does show element `#buyform_input_quantity`
        self.assert_element("#buyform_input_quantity")
        # Validate that the page does show element `#input#buyform_submit[action=submit]`
        self.assert_element("#buyform_submit")
        # Open `/logout` (cleanup)
        self.open(base_url + '/logout')

    @auto_login(TEST_USER)
    def test_3_8_update_ticket_form(self, *_):
        """
         R3.8: This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date
        """
        # Login and user mocking is handled with the common login decorator
        # Open `/`
        self.open(base_url + '/')
        # Validate that the page shows element `#updateform` 
        self.assert_element("#updateform")
        #Validate that the page does show element `#updateform_label_name` with text "Ticket Name:"
        self.assert_text("Ticket Name:", "#updateform_label_name")
        # Validate that the page does show element `#updateform_input_name`
        self.assert_element("#updateform_input_name")
        # Validate that the page does show element `#updateform_label_quantity` with text "Quantity:"
        self.assert_text("Quantity:", "#updateform_label_quantity")
        # Validate that the page does show element `#updateform_input_quantity`
        self.assert_element("#updateform_input_quantity")
        # Validate that the page does show element `#updateform_label_price` with text "Price Per Ticket:"
        self.assert_text("Price Per Ticket:", "#updateform_label_price")
        # Validate that the page does show element `#updateform_input_price`
        self.assert_element("#updateform_input_price")
        # Validate that the page does show element `#updateform_label_expiry` with text "Expiry Date:"
        self.assert_text("Expiry Date (yyyymmdd):", "#updateform_label_expiry")
        # Validate that the page does show element `#updateform_input_expiry
        self.assert_element("#updateform_input_expiry")
        # Validate that the page does show element `input#updateform_submit[action=submit]`
        self.assert_element("#updateform_submit")
        # Open `/logout` (cleanup)
        self.open(base_url + '/logout')

    @auto_login(TEST_USER)
    def test_3_9_sell_form_post(self, *_):
        """
        R3.9: The ticket-selling form can be posted to /sell
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Find the form element `#sellform`
        form = self.find_element("#sellform")
        self.assert_true(form)
        # - Verify that the form's `method` attribute is `post`
        self.assert_equal(form.get_attribute('method'), 'post')
        # - Verify that the form's `action` attribute is `/sell`
        self.assert_equal(form.get_attribute('action'), base_url + '/sell')
        # Logout is handled with the common login decorator
        
    @auto_login(TEST_USER)
    def test_3_10_buy_form_post(self, *_):
        """
        R3.10: The ticket-buying form can be posted to /buy
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Find the form element `#buyform`
        form = self.find_element("#buyform")
        self.assert_true(form)
        # - Verify that the form's `method` attribute is `post`
        self.assert_equal(form.get_attribute('method'), 'post')
        # - Verify that the form's `action` attribute is `/sell`
        self.assert_equal(form.get_attribute('action'), base_url + '/buy')
        # Logout is handled with the common login decorator
        
    @auto_login(TEST_USER)
    def test_3_11_sell_form_post(self, *_):
        """
        R3.11: The ticket-update form can be posted to /update
        """
        # Login and user mocking is handled with the common login decorator
        # - Open `/`
        self.open(base_url + '/')
        # - Find the form element `#updateform`
        form = self.find_element("#updateform")
        self.assert_true(form)
        # - Verify that the form's `method` attribute is `post`
        self.assert_equal(form.get_attribute('method'), 'post')
        # - Verify that the form's `action` attribute is `/update`
        self.assert_equal(form.get_attribute('action'), base_url + '/update')
        # Logout is handled with the common login decorator
