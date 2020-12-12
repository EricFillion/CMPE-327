"""
This file defines integration test I1
"""

from unittest.mock import patch
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327_test.common import TEST_USER, TEST_TICKET
from qa327.models import Ticket
from datetime import date, timedelta

class IntegrationCreatePostingTest(BaseCase):
    """
    A class that contains the integration test which posts a new ticket
    for sale in the app
    """

    def test_integration_create_posting(self):
        """
        This testcase follows a complete userflow through ticket posting
        """
        # ### Overview of major steps
        # 1. User registers
        # 2. User logs in
        # 3. User sells ticket
        # 4. User logs out
        # ### Notes
        # - The TEST_USER and TEST_TICKET defined in `qa327_test/common.py` will be used throughout this test
        # ### Initialization
        # - Clear all contents from database (done by pytest fixture)
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
        # ### 2. User logs in (R1.9)
        # - Enter TEST_USER's email into element `#email`
        self.type("#email", TEST_USER.email)
        # - Enter TEST_USER's password into element `#password`
        self.type("#password", TEST_USER.raw_password)
        # - Click "Login" button (element `input[type="submit"]`)
        self.click('input[type="submit"]')
        # - Validate redirection to `/`
        self.assert_equal(self.get_current_url(), base_url + '/')
        # ### 3. User sells ticket (R4.7 + R3.5.1 for validation)
        # - Enter TEST_TICKET's name in the element `#sellform_input_name`
        self.type("#sellform_input_name", TEST_TICKET.name)
        # - Enter TEST_TICKET's quantity into the element `#sellform_input_quantity`
        self.type("#sellform_input_quantity", str(TEST_TICKET.quantity))
        # - Enter TEST_TICKET's raw expiry date into the element `#sellform_input_date`
        self.type("#sellform_input_expiry", TEST_TICKET.raw_expiry)
        # - Enter TEST_TICKET's price into the element `#sellform_input_price`
        self.type("#sellform_input_price", str(TEST_TICKET.price))
        # - Click element `#sellform_submit`
        self.click('#sellform_submit')
        # - Validate that an element matching `.message_info` shows text `Successfully sold the ticket`
        self.assert_text('Successfully sold the ticket', selector='.message_info')
        # - Find `tr` of ticket by looking up ticket's name under the ticket table
        rows = self.find_elements("table#tickettable tbody tr")
        matching_trs = [row for row in rows if TEST_TICKET.name in row.text]
        self.assert_equal(len(matching_trs), 1)
        tr = matching_trs[0]
        # - Validate name by looking under the ticket's `tr` and validating that the element `td.tt_name` has text: `"{}".format(ticket.name)`
        self.assert_equal(tr.find_element_by_class_name("tt_name").text, "{}".format(TEST_TICKET.name))
        # - Validate owner's email by looking under the ticket's `tr` and validating that the element `td.tt_owner` has text: `"{}".format(user.name)`
        self.assert_equal(tr.find_element_by_class_name("tt_owner").text, "{}".format(TEST_USER.name))
        # ### 4. User logs out (R7.1)
        # - Click element `#logout`
        self.open(base_url + '/logout')
        # - Validate redirection to `/login`
        self.assert_equal(self.get_current_url(), base_url + '/login')
