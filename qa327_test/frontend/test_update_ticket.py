import pytest
from seleniumbase import BaseCase
from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327_test.common import TEST_USER, TEST_TICKET, auto_login
from qa327.models import Ticket
from datetime import datetime
from qa327_test.conftest import base_url

"""
This file defines all unit tests for the login page
"""

class FrontEndUpdateTicketTest(BaseCase):
    """
    A class that contains the unit tests for the login page
    """
    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_name_alphanumeric_negative(self, *_):
        """
         R5.1.1: The name of the ticket has to be alphanumeric-only - Negative. 
        """
        # Login and user mocking is handled with the common login decorator
        # Enter a string containing symbols (ex. "t!cket_1") into the element `#updateform_input_name`
        self.type("#updateform_input_name", "t!cket_1")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating “Unable to update ticket: The name of the ticket has to be alphanumeric only”.
        self.assert_text("Unable to update ticket: The name of the ticket has to be alphanumeric only", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_name_space_first_char(self, *_):
        """
          R5.1.2:  The name is only allowed spaces if it is not the first or the last character - Negative. Testing the first character.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter a string, that is less than 60 characters, containing only alphanumeric symbols that has a space for the first character  (ex. " t1")in the element `#updateform_input_name`
        self.type("#updateform_input_name", " t1")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        print(datetime.now().strftime("%Y%m%d"))

        # Validate that the `#message_error` element shows an error message stating “Unable to update ticket: The name of the ticket has to be alphanumeric only”.
        self.assert_text("Unable to update ticket: The name of the ticket is only allowed spaces if it is not the first or last character", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_name_space_last_char(self, *_):
        """
         R5.1.3:  The name is only allowed spaces if it is not the first or the last character - Negative. Testing the last character.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter a string, that is less than 60 characters, containing only alphanumeric symbols that
        # has a space for the last character  (ex. " t1")in the element `#updateform_input_name`
        self.type("#updateform_input_name", "t1 ")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating “Unable to update ticket: The name of the ticket has to be alphanumeric only”.
        self.assert_text("Unable to update ticket: The name of the ticket is only allowed spaces if it is not the first or last character", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_name_space_in_middle(self, *_):
        """
        R5.1.4:  The name is only allowed spaces if it is not the first or the last character - Positive.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter a string that is less than 60 characters, containing only alphanumeric symbols that
        # contains spaces that are not the first and last character (ex. "ticket 1") in the element `#updateform_input_name`
        self.type("#updateform_input_name", "ticket 1")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_info` element shows "Ticket was updated successfully"
        self.assert_text("Ticket was updated successfully", selector = '.message_info')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_valid_name(self, *_):
        """
         R5.1.5: Updating to a valid name - Positive. 
        """
        # Login and user mocking is handled with the common login decorator
        # Enter test ticket's name into the element `#updateform_input_name`
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_info` element shows "Ticket was updated successfully"
        self.assert_text("Ticket was updated successfully", selector = '.message_info')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)  
    def test_update_ticket_long_name(self, *_):
        """
         R5.2:  The name of the ticket is no longer than 60 characters - Negative.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter “aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa”
        # (61 chars) in the element element `#updateform_input_name`
        self.type("#updateform_input_name", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        # Enter the test_ticket's quantity in element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating  
        # “Unable to update ticket: The name of the ticket should be no longer than 60 characters”.
        self.assert_text("Unable to update ticket: The name of the ticket should be no longer than 60 characters", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)  
    def test_update_ticket_low_quantity(self, *_):
        """
        R5.3.1:  The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative. Testing quantity below range.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter the test_ticket's name in element `#updateform_input_name` 
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter a number less than or equal to 0 into the element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", "0")

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: 
        # The quantity of the ticket must be between 1 and 100”.
        self.assert_text("Unable to update ticket: The quantity of the ticket must be between 1 and 100", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)  
    def test_update_ticket_high_quantity(self, *_):
        """
        R5.3.2: The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative. Testing quantity above range.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter the test_ticket's name in element `#updateform_input_name` 
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter a number greater than 100 (ex. 101) into the element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", "101")

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: 
        # The quantity of the ticket must be between 1 and 100”.
        self.assert_text("Unable to update ticket: The quantity of the ticket must be between 1 and 100", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_valid_quantity(self, *_):
        """
         R5.3.3:  The quantity of the tickets has to be more than 0, and less than or equal to 100 - Positive.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter test ticket's name into the element `#updateform_input_name`
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter the number 50 into the element `#updateform_input_quantity`
        self.type("#updateform_input_quantity", "50")

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_info` element shows "Ticket was updated successfully"
        self.assert_text("Ticket was updated successfully", selector = '.message_info')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)  
    def test_update_ticket_low_price(self, *_):
        """
        R5.4.1:  Price has to be of range [10, 100] - Negative. Testing price below the range. 
        """
        # Login and user mocking is handled with the common login decorator
        # Enter the test_ticket's name in element `#updateform_input_name` 
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter a number below 10 (ex. 9) into the element `#updateform_input_price`
        self.type("#updateform_input_price", "9")
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating
        # “Unable to update ticket: The price of the ticket must be between 10 and 100”.
        self.assert_text("Unable to update ticket: The price of the ticket must be between 10 and 100", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)  
    def test_update_ticket_high_price(self, *_):
        """
        R5.4.2:  Price has to be of range [10, 100] - Negative. Testing price above the range.
        """
        # Login and user mocking is handled with the common login decorator
        # Enter the test_ticket's name in element `#updateform_input_name` 
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter a number above 100 (ex. 101) into the element `#updateform_input_price`
        self.type("#updateform_input_price", "101")
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating
        # “Unable to update ticket: The price of the ticket must be between 10 and 100”.
        self.assert_text("Unable to update ticket: The price of the ticket must be between 10 and 100", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_valid_price(self, *_):
        """
        R5.4.3: Price has to be of range [10, 100] - Positive.  
        """
        # Login and user mocking is handled with the common login decorator
        # Enter test ticket's name into the element `#updateform_input_name`
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the number 50 into the element `#updateform_input_price`
        self.type("#updateform_input_price", "50")
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_info` element shows "Ticket was updated successfully"
        self.assert_text("Ticket was updated successfully", selector = '.message_info')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)  
    def test_update_ticket_incorrect_date_format(self, *_):
        """
         R5.5.1:  Date must be given in the format YYYYMMDD (e.g. 20200901) - Negative
        """
        # Login and user mocking is handled with the common login decorator
        # Enter the test_ticket's name in element `#updateform_input_name` 
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter a date in an invalid format (ex. 20201331) into the element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", "20201331")

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating 
        # “Unable to update ticket: Date must be given in the format YYYYMMDD (e.g. 20200901)”.
        self.assert_text("Unable to update ticket: Date must be given in the format YYYYMMDD (e.g. 20200901)", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')

    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)
    def test_update_ticket_valid_date(self, *_):
        """
        R5.5.2:  Date must be given in the format YYYYMMDD (e.g. 20200901) - Positive.   
        """
        # Login and user mocking is handled with the common login decorator
        # Enter test ticket's name into the element `#updateform_input_name`
        self.type("#updateform_input_name", TEST_TICKET.name)

        # Enter the test_ticket's quantity in element `updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Call function to get todays date and enter date into the element 
        # `#updateform_input_expiry`. Todays date is used so that the date is never in the past.
        self.type("#updateform_input_expiry", datetime.now().strftime("%Y%m%d"))

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_info` element shows "Ticket was updated successfully"
        self.assert_text("Ticket was updated successfully", selector = '.message_info')

        # Open /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @auto_login(TEST_USER)  
    def test_update_ticket_non_existent(self, *_):
        """
         R5.6.1:  The ticket of the given name must exist - Negative. 
        """
        # Login and user mocking is handled with the common login decorator
        # Enter "nonExistentTicket" in element `#updateform_input_name`
        self.type("#updateform_input_name", "nonExistentTicket")

        # Enter the test_ticket's quantity in element `updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # the welcome element is unique to the profile page
        self.assert_element("#welcome")

        # Validate that the `#message_error` element shows an error message stating 
        #  “Unable to update ticket: The ticket of the given name must exist."
        self.assert_text("Unable to update ticket: The ticket of the given name must exist.", selector = '.message_error')

        # Open /logout (clean up)
        self.open(base_url + '/logout')


    @patch('qa327.backend.get_all_tickets', return_value=[TEST_TICKET])
    @patch('qa327.backend.update_ticket', return_value=None)
    @auto_login(TEST_USER)  
    def test_update_ticket_error_redirect(self, *_):
        """
         R5.7.1:  For any errors, redirect back to / and show an error message. 
        """
        # Login and user mocking is handled with the common login decorator
        # Enter " no!tATicket " in element `#updateform_input_name`
        self.type("#updateform_input_name", " no!tATicket ")

        # Enter the test_ticket's quantity in element `updateform_input_quantity`
        self.type("#updateform_input_quantity", str(TEST_TICKET.quantity))

        # Enter the test_ticket's price in element `#updateform_input_price`
        self.type("#updateform_input_price", str(TEST_TICKET.price))
        
        # Enter the test_ticket's expiry date in element `#updateform_input_expiry`
        self.type("#updateform_input_expiry", TEST_TICKET.raw_expiry)

        # Click element `input#updateform_submit[action=submit]`
        self.click('#updateform_submit')

        # Validate that the page has been redirected to '/'
        self.assert_equal(self.get_current_url(), base_url + '/')

        #Validate that the `#message_error` element is shown."
        self.assert_element(".message_error")

        # Open /logout (clean up)
        self.open(base_url + '/logout')


