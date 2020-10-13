# Requirement 3 - User's Home Page
## R3.1: If the user is not logged in, redirect to login page
Mocking:

N/A

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/`
- Ensure it redirects to login page
    - TODO: determine how redirect works? HTTP status code? 307?

## R3.2: This page shows a header 'Hi {}'.format(user.name)
Mocking:
- Mock user
    - TODO

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login` and log in as test user as per procedure defined in x...
    - TODO: should we have a defined procedure for logging in as the test user? It feels redundant to have each test case say how to log in..
- Open '/'
- Validate that the page shows an element with text: 'Hi {}'.format(user.name) 

## R3.3: This page shows user balance.
Mocking:
- Mock user
    - TODO

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login` and log in as test user as per procedure defined in x...
- Open '/'
- Validate that the page shows an element with text: "Your balance is ${:.2f}".format(user.balance)

## R3.4: This page shows a logout link, pointing to /logout
Mocking:
- Mock user
    - TODO

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login` and log in as test user as per procedure defined in x...
- Open '/'
- Validate that the page shows an element with text "Logout" and href='/logout'
    - TODO: specify this in the correct format

## R3.5.1: This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. (positive, ensure tickets in database show properly)
Mocking:
- Mock user
    - TODO
- Mock tickets
    - Randomly generate ticket information?

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login` and log in as test user as per procedure defined in x...
- Open '/'
- Validate that the page shows a table with the same ticket information mocked up
    - Ensure quantity
    - Ensure owner's email
    - Ensure price

## R3.5.2: This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. (negative, ensure expired ticket is not displayed)
Mocking:
- Mock user
    - TODO
- Mock tickets
    - Randomly generate ticket information?
    - Ensure one expired ticket

Actions:
- Open `/logout` (to invalidate any previous session)
- Open `/login` and log in as test user as per procedure defined in x...
- Open '/'
- Validate that the page shows a table with the same ticket information mocked up
    - Ensure quantity
    - Ensure owner's email
    - Ensure price
- Validate that the expired ticket is NOT shown


## R3.6: This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date
Mocking:

N/A

Actions:

N/A

## R3.7: This page contains a form that a user can buy new tickets. Fields: name, quantity
Mocking:

N/A

Actions:

N/A

## R3.8: The ticket-selling form can be posted to /sell
Mocking:

N/A

Actions:

N/A

## R3.9: The ticket-buying form can be posted to /buy
Mocking:

N/A

Actions:

N/A

## R3.10: The ticket-update form can be posted to /update
Mocking:

N/A

Actions:

N/A


