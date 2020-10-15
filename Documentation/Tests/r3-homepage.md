# Requirement 3 - User's Home Page
## Notes:
When the testcases under R3 refer to the "test user", it refers to this user:
```python
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

## R3.1: If the user is not logged in, redirect to login page
Mocking:

N/A

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/`
- Sleep 3 seconds, then validate that current URL is `/login`

## R3.2: This page shows a header 'Hi {}'.format(user.name)
Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page shows element `#welcome` with text: `'Hi {}'.format(user.name)`
- Open `/logout` (cleanup)

## R3.3: This page shows user balance
Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page shows element `#balance` with text: `"Your balance is ${:.2f}".format(user.balance)`
- Open `/logout` (cleanup)

## R3.4: This page shows a logout link, pointing to /logout
Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page shows element `a#logout` with text "Logout" and `href='/logout'`
- Open `/logout` (cleanup)

## R3.5.1: This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. (positive, ensure tickets in database show properly)
Mocking:
- Mock backend.get_user to return the test user
- Mock backend.get_all_tickets to create a list of tickets
    - Ensure list of tickets is stored for later
    - There must be one or more tickets
    - All tickets should be valid (not expired)

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page shows element `table#tickettable`
- Validate that the number of ticket rows (as opposed to header rows) in the ticket table is equal to the number of tickets
- For each ticket in the list of tickets from the mock backend:
    - Find `tr` of ticket by looking up ticket's name under the ticket table
    - Validate name by looking under the ticket's `tr` and validating that the element `td.tt_name` has text: `"{}".format(ticket.name)`
    - Validate quantity by looking under the ticket's `tr` and validating that the element `td.tt_quantity` has text: `"{}".format(ticket.balance)`
    - Validate owner's email by looking under the ticket's `tr` and validating that the element `td.tt_owner` has text: `"{}".format(ticket.owner)`
    - Validate price by looking under the ticket's `tr` and validating that the element `td.tt_price` has text: `"${:.2f}".format(ticket.price)`
- Open `/logout` (cleanup)

## R3.5.2: This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. (negative, ensure expired ticket is not displayed)
Mocking:
- Mock backend.get_user to return the test user
- Mock backend.get_all_tickets to create a list of tickets
    - Ensure list of tickets is stored for later
    - One or more tickets must be valid (not expired)
    - One or more tickets must be expired

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page shows element `table#tickettable`
- Validate that the number of ticket rows (as opposed to header rows) in the ticket table is equal to the number of valid tickets
- For each expired ticket in the list of tickets from the mock backend:
    - Search for `tr` of ticket by looking up ticket's name under the ticket table, and ensure it can not be found
- Open `/logout` (cleanup)

## R3.5.3: This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. (ensure table is not displayed if there are zero valid tickets)
Mocking:
- Mock backend.get_user to return the test user
- Mock backend.get_all_tickets to create a list of tickets
    - There must be one or more tickets
    - All tickets must be expired

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page does not show element `table#tickettable`
- Validate that the page does show element `#no_tickets_available`
- Open `/logout` (cleanup)

## R3.5.4: This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. (test case with zero total tickets)
Mocking:
- Mock backend.get_user to return the test user
- Mock backend.get_all_tickets to create a list of tickets
    - There must be zero tickets

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page does not show element `table#tickettable`
- Validate that the page does show element `#no_tickets_available`
- Open `/logout` (cleanup)

## R3.6: This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page does show element `#sellform`
- Validate that the page does show element `#sellform_label_name` with text "Ticket Name:"
- Validate that the page does show element `#sellform_input_name`
- Validate that the page does show element `#sellform_label_quantity` with text "Quantity:"
- Validate that the page does show element `#sellform_input_quantity`
- Validate that the page does show element `#sellform_label_price` with text "Price Per Ticket:"
- Validate that the page does show element `#sellform_input_price`
- Validate that the page does show element `#sellform_label_expiry` with text "Expiry Date:"
- Validate that the page does show element `#sellform_input_expiry`
- Validate that the page does show element `input#sellform_submit[action=submit]`
- Open `/logout` (cleanup)

## R3.7: This page contains a form that a user can buy new tickets. Fields: name, quantity
Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page does show element `#buyform`
- Validate that the page does show element `#buyform_label_name` with text "Ticket Name:"
- Validate that the page does show element `#buyform_input_name`
- Validate that the page does show element `#buyform_label_quantity` with text "Quantity:"
- Validate that the page does show element `#buyform_input_quantity`
- Validate that the page does show element `input#buyform_submit[action=submit]`
- Open `/logout` (cleanup)

## R3.8: This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date
Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Validate that the page does show element `#updateform`
- Validate that the page does show element `#updateform_label_name` with text "Ticket Name:"
- Validate that the page does show element `#updateform_input_name`
- Validate that the page does show element `#updateform_label_quantity` with text "Quantity:"
- Validate that the page does show element `#updateform_input_quantity`
- Validate that the page does show element `#updateform_label_price` with text "Price Per Ticket:"
- Validate that the page does show element `#updateform_input_price`
- Validate that the page does show element `#updateform_label_expiry` with text "Expiry Date:"
- Validate that the page does show element `#updateform_input_expiry`
- Validate that the page does show element `input#updateform_submit[action=submit]`
- Open `/logout` (cleanup)

## R3.9: The ticket-selling form can be posted to /sell
Additional Test Data:
```
test_ticket = Ticket(
    owner='test_frontend@example.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    expiry='20200901'
)
```

Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Fill fields
    - Fill element `#sellform_input_name` with the ticket name
    - Fill element `#sellform_input_quantity` with the quantity
    - Fill element `#sellform_input_price` with the ticket price
    - Fill element `#sellform_input_expiry` with the ticket expiry date
- Click element `#sellform_submit`
- Validate that a POST request is sent to `/sell` with the correct information as specified in the fields listed above
- Open `/logout` (cleanup)

## R3.10: The ticket-buying form can be posted to /buy
Additional Test Data:
```
test_ticket = Ticket(
    owner='test_frontend@example.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    expiry='20200901'
)
```

Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Fill fields
    - Fill element `#buyform_input_name` with the ticket name
    - Fill element `#buyform_input_quantity` with the quantity
- Click element `#buyform_submit`
- Validate that a POST request is sent to `/buy` with the correct information as specified in the fields listed above
- Open `/logout` (cleanup)

## R3.11: The ticket-update form can be posted to /update
Additional Test Data:
```
test_ticket = Ticket(
    owner='test_frontend@example.com',
    name='test_ticket_yo',
    quantity=10,
    price=10,
    expiry='20200901'
)
```

Mocking:
- Mock backend.get_user to return the test user

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login`
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type='submit']`
- Open `/`
- Fill fields
    - Fill element `#updateform_input_name` with the ticket name
    - Fill element `#updateform_input_quantity` with the quantity
    - Fill element `#updateform_input_price` with the ticket price
    - Fill element `#updateform_input_expiry` with the ticket expiry date
- Click element `#updateform_submit`
- Validate that a POST request is sent to `/update` with the correct information as specified in the fields listed above
- Open `/logout` (cleanup)
