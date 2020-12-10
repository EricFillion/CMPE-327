"""
This file defines all unit tests for the login page
"""

from unittest.mock import patch
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from qa327_test.common import TEST_USER, auto_login, TEST_TICKET

class FrontEndSellTest(BaseCase):
    """
    A class that contains the unit tests for the sell functionality
    """
    @auto_login(TEST_USER)
    def test_4_1_1_alphanumeric_negative(self, *_):
        """
        R4.1.1: The name of the ticket has to be alphanumeric-only
        """
        # Enters a name with a special character into the name text field
        self.type("#sellform_input_name", "abc1234#")

        # Enter  TEST_TICKET's quantity into the sellform_input_quantity element
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter  TEST_TICKET's expiry date into the sellform_input_expiry element
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter  TEST_TICKET's price into the sellform_input_price element
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # Press submit
        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The name of the ticket has to be alphanumeric only", selector='.message_error')

    @patch('qa327.backend.sell_ticket', return_value=False)
    @auto_login(TEST_USER)
    def test_4_1_2_space_positive(self, *_):
        """
        R4.1.2: Space allowed if not first or last character of the ticket's name
        """
        # Enters a valid name with a space in the middle
        self.type("#sellform_input_name", "abc 1234")

        # Enter valid information for other elements
        self.type("#sellform_input_quantity", str(str(TEST_TICKET.quantity)))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", str(TEST_TICKET.raw_expiry))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(str(TEST_TICKET.price)))

        # Press submit
        self.click('#sellform_submit')

        self.assert_text("Successfully sold the ticket", selector='.message_info')


    @auto_login(TEST_USER)
    def test_4_1_3_space_negative(self, *_):
        """
        R4.1.3: Space not allowed if it’s the first character
        """
        # Enters a name with a space as the first character
        self.type("#sellform_input_name", " abc1234")

        # Enter valid information for other elements
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # Press submit
        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The name of the ticket is only allowed spaces if it is not the first or last character", selector='.message_error')


    @auto_login(TEST_USER)
    def test_4_1_4_space_negative(self, *_):
        """
        R4.1.4: Space not allowed if it’s the last character
        """
        # Enters a name with with a space as the last character
        self.type("#sellform_input_name", "abc1234 ")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))


        # Press submit
        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The name of the ticket is only allowed spaces if it is not the first or last character", selector='.message_error')

    @auto_login(TEST_USER)
    def test_4_2_1_length_negative(self, *_):
        """
        4.2.1 The name of the ticket is no longer than 60 characters - Negative
        """
        # Enters a name with 61 characters
        self.type("#sellform_input_name", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))



        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The name of the ticket should be no longer than 60 characters", selector='.message_error')



    @patch('qa327.backend.sell_ticket', return_value=False)
    @auto_login(TEST_USER)
    def test_4_2_2_length_positive(self, *_):
        """
        4.2.2 The name of the ticket is no longer than 60 characters - Positive
        """
        # Enters a name with 60 chars
        self.type("#sellform_input_name", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))


        self.click('#sellform_submit')

        self.assert_text("Successfully sold the ticket", selector='.message_info')

    @auto_login(TEST_USER)
    def test_4_3_1_quantity_negative(self, *_):
        """
        R4.3.1 The quantity of tickets has to be more than 0 - Negative
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter quantity of 0, which is the lowest negative value
        self.type("#sellform_input_quantity", str(0))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))


        # submit
        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The quantity of the ticket must be between 1 and 100", selector='.message_error')


    @auto_login(TEST_USER)
    @patch('qa327.backend.sell_ticket', return_value=False)
    def test_4_3_2_quantity_positive(self, *_):
        """
        R4.3.2 The quantity of tickets has to be more than 0 - Positive

        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter quantity of 1, which is the lowest positive value
        self.type("#sellform_input_quantity", str(1))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(str(TEST_TICKET.price)))


        # submit
        self.click('#sellform_submit')

        self.assert_text("Successfully sold the ticket", selector='.message_info')

    @auto_login(TEST_USER)
    def test_4_3_3_quantity_negative(self, *_):
        """
        R4.3.2 The quantity of tickets has to be less than 101 - Negative
        """
        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter quantity of 101, which is the lowest negative value
        self.type("#sellform_input_quantity", str(101))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # submit
        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The quantity of the ticket must be between 1 and 100", selector='.message_error')


    @auto_login(TEST_USER)
    @patch('qa327.backend.sell_ticket', return_value=False)
    def test_4_3_4_quantity_positive(self, *_):
        """
         R4.3.4 The quantity of tickets has to be less than 101  - Positive
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter quantity of 100, which is the highest positive value
        self.type("#sellform_input_quantity", str(100))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # submit
        self.click('#sellform_submit')

        self.assert_text("Successfully sold the ticket", selector='.message_info')

    @auto_login(TEST_USER)
    @patch('qa327.backend.sell_ticket', return_value=False)
    def test_4_4_1_price_positive(self, *_):
        """
        R4.4.1 The price of tickets has to be more than 9 - Positive
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter price of 10, which is the lowest positive value
        self.type("#sellform_input_price", str(10))


        # submit
        self.click('#sellform_submit')

        self.assert_text("Successfully sold the ticket", selector='.message_info')


    @auto_login(TEST_USER)
    def test_4_4_2_price_negative(self, *_):
        """
        R4.4.2 The price of tickets has to be more than 9 - Negative
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter price of 9, which is the highest negative value
        self.type("#sellform_input_price", str(9))

        # submit
        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The price of the ticket must be between 10 and 100", selector='.message_error')


    @auto_login(TEST_USER)
    @patch('qa327.backend.sell_ticket', return_value=False)
    def test_4_4_3_price_positive(self, *_):
        """
        R4.4.3 The price of tickets has to be less than 101 - Positive
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter price of 100, which is the lowest positive value
        self.type("#sellform_input_price", str(100))

        # submit
        self.click('#sellform_submit')

        self.assert_text("Successfully sold the ticket", selector='.message_info')


    @auto_login(TEST_USER)
    def test_4_4_4_price_negative(self, *_):
        """
        R4.4.4 The price of tickets has to be less than 101 - Negative
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter price of 9, which is the highest negative value
        self.type("#sellform_input_price", str(101))

        # submit
        self.click('#sellform_submit')

        self.assert_text("Unable to sell ticket: The price of the ticket must be between 10 and 100", selector='.message_error')

    @auto_login(TEST_USER)
    def test_4_5_1_date_negative(self, *_):
        """
        R4.5.1 The date must given in the format YYYYMMDD - Negative
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter expiry in a long format with full words
        self.type("#sellform_input_expiry", "January 1st, 2021")

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # submit
        self.click('#sellform_submit')

        self.assert_text("Date must be given in the format YYYYMMDD (e.g. 20200901)", selector='.message_error')


    @auto_login(TEST_USER)
    @patch('qa327.backend.sell_ticket', return_value=False)
    def test_4_5_2_date_positive(self, *_):
        """
        R4.5.1 The date must given in the format YYYYMMDD - Positive
        """

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter a valid date
        self.type("#sellform_input_expiry", "20210101")

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # submit
        self.click('#sellform_submit')

        self.assert_text("Successfully sold the ticket", selector='.message_info')
    #

    @auto_login(TEST_USER)
    def test_4_6_redirect(self, *_):
        """
        R4.6 For any errors, redirect back to / and show an error message
        """
        # Enter an invalid name
        self.type("#sellform_input_name", " ")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # submit
        self.click('#sellform_submit')

        # Validate that the page has been redirected to '/'
        self.assert_equal(self.get_current_url(), base_url + '/')

        # assert that a message error is being shown
        self.assert_element(selector='.message_error')

    @patch('qa327.backend.sell_ticket', return_value=False)
    @auto_login(TEST_USER)
    def test_4_7_add_ticket_info(self, *_):
        """
        R4.7 The added new ticket information will be posted on the user profile page
        """

        # Enter valid information for all elements

        # Enter the test_ticket's name in element `#updateform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))

        # submit
        self.click('#sellform_submit')
        # todo assert