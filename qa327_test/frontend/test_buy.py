import pytest
from unittest.mock import patch
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from qa327_test.common import auto_login, TEST_TICKET, TEST_USER
from qa327.models import Ticket
from datetime import date, timedelta


class FrontendBuyTest(BaseCase):
    """
    A class test buy section
    """
    @auto_login(TEST_USER)
    def test_name_alphanumeric(self, *_):
        """
        Test Case R6.1.1: The name of the ticket has to be alphanumeric-only - Negative.
        """
        # open home page
        self.open(base_url + '/')

        # input name
        self.type("#buyform_input_name", "t!cket_1")

        # input quantity
        self.type("#buyform_input_quantity", str(1))

        # submit buy form
        self.click("#buyform_submit")

        # redirect to home page
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have error message
        self.assert_text(
            "The name of the ticket has to be alphanumeric only", selector='.message_error')

    @auto_login(TEST_USER)
    def test_name_space_position(self, *_):
        """
        Test Case 6.1.2 The name is only allowed spaces if it is not the first or the last character
        """
        # open home page
        self.open(base_url + '/')

        # input name with space first and end of word
        self.type("#buyform_input_name", " "+TEST_TICKET.name+" ")

        # input quantity
        self.type("#buyform_input_quantity", str(1))

        # submit bu form
        self.click("#buyform_submit")

        # redirect to home page
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have error message: The name of the ticket is only allowed spaces if it is not the first or last character
        self.assert_text(
            "The name of the ticket is only allowed spaces if it is not the first or last character", selector='.message_error')

    @auto_login(TEST_USER)
    def test_name_length(self, *_):
        """
        Test Case R6.2: The name of the ticket is no longer than 60 characters - Negative.
        """

        # open home page
        self.open(base_url + '/')

        # input oversized name of ticket
        self.type("#buyform_input_name", "a"*61)

        # input valid quantity
        self.type("#buyform_input_quantity", str(1))

        # submit form
        self.click("#buyform_submit")

        # redirect to home page
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have error message :The name of the ticket should be no longer than 60 characters
        self.assert_text(
            "The name of the ticket should be no longer than 60 characters", selector='.message_error')

    @auto_login(TEST_USER)
    def test_quantity_number_too_long(self, *_):
        """
        R5.3.1.1: The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative.
        """

        # open home page
        self.open(base_url + '/')

        # input valid name
        self.type("#buyform_input_name", TEST_TICKET.name)

        # input invalid quantity
        self.type("#buyform_input_quantity", str(1000))

        # submit buy form
        self.click("#buyform_submit")

        # redirect to home page
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have error message: The quantity of the ticket must be between 1 and 100
        self.assert_text(
            "The quantity of the ticket must be between 1 and 100", selector='.message_error')

    @auto_login(TEST_USER)
    def test_quantity_number_too_short(self, *_):
        """
        R5.3.1.2: The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative.
        """
        # open home page
        self.open(base_url + '/')

        # input valid ticket name
        self.type("#buyform_input_name", TEST_TICKET.name)

        # input invalid quantity
        self.type("#buyform_input_quantity", str(0))

        # submit buy form
        self.click("#buyform_submit")

        # redirect to home page
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have error message: The quantity of the ticket must be between 1 and 100
        self.assert_text(
            "The quantity of the ticket must be between 1 and 100", selector='.message_error')

    @patch('qa327.backend.get_ticket_by_name', return_value=None)
    @auto_login(TEST_USER)
    def test_ticket_name_existence(self, *_):
        """
        R6.4.1: /buy[post] The ticket name not exists in the database 
        """
        # open home page
        self.open(base_url + '/')

        # input invalid ticket name
        self.type("#buyform_input_name", "testTicketNonexisted")

        # input valid quantity
        self.type("#buyform_input_quantity", str(1))

        # submit form
        self.click("#buyform_submit")

        # redirect to home page
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have error message: The ticket does not exist.
        self.assert_text("The ticket does not exist.", selector='.message_error')

    @patch('qa327.backend.get_ticket_by_name', return_value=TEST_TICKET)
    @auto_login(TEST_USER)
    def test_ticket_quantity_enough(self, *_):
        """
        R6.4.3: /buy[post] The quantity is more than the quantity requested to buy
        """
        # open home page
        self.open(base_url + '/')
        # input valid name
        self.type("#buyform_input_name", TEST_TICKET.name)
        # input invalid quantity
        self.type("#buyform_input_quantity", str(TEST_TICKET.quantity+1))
        # submit form
        self.click("#buyform_submit")
        # redirect to home page
        self.assert_equal(self.get_current_url(), base_url + '/')
        # should have error message
        self.assert_text("The ticket quantity is less than the quantity requested.", selector='.message_error')


    @patch('qa327.backend.get_ticket_by_name', return_value=TEST_TICKET)
    @auto_login(TEST_USER)
    def test_user_balance_enough(self, *_):
        """
        R6.5.1: /buy[post] The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) -Negative
        """
        # open home page
        self.open(base_url + '/')

        # input valid name
        self.type("#buyform_input_name", TEST_TICKET.name)

        # input a valid quantity
        self.type("#buyform_input_quantity", str(TEST_TICKET.quantity))

        # submit form
        self.click("#buyform_submit")

        # redirect home page
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have error message
        self.assert_text("Must have more balance than the ticket price.", selector='.message_error')



    @auto_login(TEST_USER)
    @patch('qa327.backend.buy_ticket', return_value=None)
    @patch('qa327.backend.get_ticket_by_name', return_value=TEST_TICKET)
    def test_user_buy_success(self, *_):
        """
        R6.6: /buy[post] No error, return home page 
        """

        # open home page
        self.open(base_url + '/')

        # input valid name
        self.type("#buyform_input_name", TEST_TICKET.name)

        # input a valid quantity
        self.type("#buyform_input_quantity", str(1))

        # submit form
        self.click("#buyform_submit")

        # redirect home page and there should be no error
        self.assert_equal(self.get_current_url(), base_url + '/')

        # should have info message:
        self.assert_text("Ticket was purchased successfully", selector='.message_info')

