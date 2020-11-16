from unittest.mock import patch
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327_test.common import TEST_USER, auto_login

"""
This file defines all unit tests for the login page
"""

class FrontEndHomepageTest(BaseCase):
    """
    A class that contains the unit tests for the homepage
    """
    
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
        self.assert_text("Expiry Date:", "#sellform_label_expiry")
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
        self.assert_text("Expiry Date:", "#updateform_label_expiry")
        # Validate that the page does show element `#updateform_input_expiry
        self.assert_element("#updateform_input_expiry")
        # Validate that the page does show element `input#updateform_submit[action=submit]`
        self.assert_element("#updateform_submit")
        # Open `/logout` (cleanup)
        self.open(base_url + '/logout')