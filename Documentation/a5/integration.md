# Integration Tests
### Notes
Each of these tests has been broken up into "major steps", showing what functionality will be exercised. Each major step mostly duplicates the actions done in a frontend test case. The closest matching frontend testcase has been put in parentheses beside the heading since it may be useful to refer to the Markdown description or the actual code. Each major step includes a check that the action it intended to take was completed successfully.


## Integration Test I1: Create posting
### Overview of major steps
1. User registers
2. User logs in
3. User sells ticket
4. User logs out
### Notes
- The test_user and test_ticket defined in `qa327_test/common.py` will be used throughout this test
### Initialization
- Clear all contents from database (done by pytest fixture)
- Open `/logout` to ensure there is no previous session
### 1. User registers (R2.10)
- Open `/`
- Validate redirection to `/login`
- Click "Register" link (element `a[href="/register"]`)
- Enter test_user's name into element `#name`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Enter test_user's password into element `#password2`
- Click "Register" button (element `input[type="submit"]`)
- Validate redirection to `/login`
### 2. User logs in (R1.9)
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click "Login" button (element `input[type="submit"]`)
- Validate redirection to `/`
### 3. User sells ticket (R4.7 + R3.5.1 for validation)
- Enter test_ticket’s name in the element `#sellform_input_name`
- Enter test_ticket’s quantity into the element `#sellform_input_quantity`
- Enter test_ticket’s raw expiry date into the element `#sellform_input_date`
- Enter test_ticket’s price into the element `#sellform_input_price`
- Click element `#sellform_submit`
- Validate that an element matching `.message_info` shows text `Ticket was posted for sale successfully.`
- Find `tr` of ticket by looking up ticket's name under the ticket table
- Validate name by looking under the ticket's `tr` and validating that the element `td.tt_name` has text: `"{}".format(ticket.name)`
- Validate owner's email by looking under the ticket's `tr` and validating that the element `td.tt_owner` has text: `"{}".format(user.name)`
    - This is to verify the link between ticket and its owner was properly created
### 4. User logs out (R7.1)
- Click element `#logout`
- Validate redirection to `/login`


## Integration Test I2: Purchase ticket
### Overview of major steps
1. User registers
2. User logs in
3. User buys ticket
4. User logs out
### Notes
- The test_user defined in `qa327_test/common.py` will be used throughout this test
- An additional test user `test_seller` will be manually added to the database to serve as the user who posted the ticket
    - Email: "test_seller@test.com"
    - Name: "Test Seller"
    - Password: None (we will not login as this user, so it is not necessary to set their password)
    - Balance: 0 (they will not need to spend any balance)
- An additional test ticket "test_selling_ticket" will be manually added to the database
    - It will be based on the test_ticket provided in common.py, but with the following information changed:
    - Owner: `test_seller`
    - Owner ID: [corresponding value for test_seller, set automatically from code]
### Initialization
- Clear all contents from database (done by pytest fixture)
- Add "test_seller" to database
- Open `/logout` to ensure there is no previous session
### 1. User registers (R2.10)
- Open `/`
- Validate redirection to `/login`
- Click "Register" link (element `a[href="/register"]`)
- Enter test_user's name into element `#name`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Enter test_user's password into element `#password2`
- Click "Register" button (element `input[type="submit"]`)
- Validate redirection to `/login`
### 2. User logs in (R1.9 + R3.3 for balance validation)
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click "Login" button (element `input[type="submit"]`)
- Validate redirection to `/`
- Validate that an element `#balance` shows text `Your balance is $50.00`
### 3. User buys ticket (R6.5.1 + R3.5.1 for quantity validation + R3.3 for balance validation)
- Enter test_ticket’s name in the element `#buyform_input_name`
- Enter a quantity of 5 into the element `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that an element `.message_info` shows text `Ticket was purchased successfully.`
- Find `tr` of ticket by looking up ticket's name under the ticket table
- Validate name by looking under the ticket's `tr` and validating that the element `td.tt_quantity` has text: `85`
- Validate that an element `#balance` shows text `Your balance is $43.00`
### 4. User logs out (R7.1)
- Click element `#logout`
- Validate redirection to `/login`