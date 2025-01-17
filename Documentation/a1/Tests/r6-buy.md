## R6. /buy

**Description**:  user can buy a ticket for sale. Fields: name, quantity. 

### Test Data
```
TEST_USER = User(
    email='test_frontend@test.com',
    name='Test Frontend',
    balance=2000
)
TEST_USER.raw_password = 'q1w2e3Q!W@E#'
TEST_USER.password = generate_password_hash(TEST_USER.raw_password)
```

```
TEST_TICKET = Ticket(
    name="t1",
    quantity=90,
    price=100,
    expiry=date(2030, 1, 1),
    owner_id="test_owener_id",
    owner=TEST_USER,
)
```

### Test Case R6.1.1: The name of the ticket has to be alphanumeric-only - Negative. 

Mocking:      
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter a string containing symbols (ex. "t!cket_1") into the element  `#buyform_input_name`
- Enter the TEST_TICKET's quantity into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows an errormessage stating “The name of the ticket has to be alphanumeric only”.
- Open /logout (clean up)

### Test Case R6.1.2:  The name is only allowed spaces if it is not the first or the last character - Negative. Testing the first character.  
Mocking:      
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:       
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter a string, that is less than 60 characters, containing only alphanumeric symbols that has a space for the first character (ex. " t1") in the element  `#buyform_input_name`
- Enter the TEST_TICKET's quantity into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected back to'/'and shows an error message stating “The name of the ticket is only allowed spaces if it is not the first or last character”.
- Open /logout (clean up)

### Test Case R6.1.3:  The name is only allowed spaces if it is not the first or the last character - Negative. Testing the last character.
Mocking:    
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:       
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter a string that is less than 60 characters, containing only alphanumeric symbols that has a space for the last character (ex. "t1 ") in the element  `#buyform_input_name`
- Enter the TEST_TICKET's quantity into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows an errormessage stating  “The name of the ticket is only allowed spaces if it is not the first or last character”.
 - Open /logout (clean up)

### Test Case R6.1.4:  The name is only allowed spaces if it is not the first or the last character - Positive.
Mocking:    
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter a string that is less than 60 characters, containing only alphanumeric symbols that contains spaces that are not the first and last character (ex. "ticket 1") in the element  `#buyform_input_name`
- Enter the TEST_TICKET's quantity into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows successful
- Open /logout (clean up)

 
### Test Case R6.1.5: Entering a valid name - Positive. 
Mocking:       
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter the TEST_TICKET's name in element  `#buyform_input_name`
- Enter the TEST_TICKET's quantity into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows successful
- Open /logout (clean up)

### Test Case R6.2:  The name of the ticket is no longer than 60 characters - Negative.
Mocking:    
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter a string that containing only alphanumeric symbols that is more than 60 characters in the element  `#buyform_input_name`
- Enter the TEST_TICKET's quantity into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows an errormessage stating  “The name of the ticket should be no longer than 60 characters”.
- Open /logout (clean up)

### Test Case R6.3.1:  The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative. Testing quantity below range.
Mocking:    
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter the TEST_TICKET's name in element  `#buyform_input_name`
- Enter a number less than or equal to 0 (ex.-1) into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows an errormessage stating  “The quantity of the tickets has to be more than 0, and less than or equal to 100”.
- Open /logout (clean up)

### Test Case R6.3.2: The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative. Testing quantity above range.  
Mocking:    
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter the TEST_TICKET's name in element  `#buyform_input_name`
- Enter a number greater than 100 (ex. 101) into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows an errormessage stating  “The quantity of the tickets has to be more than 0, and less than or equal to 100”.
- Open /logout (clean up)

### Test Case R6.3.3:  The quantity of the tickets has to be more than 0, and less than or equal to 100 - Postive. 

Mocking:       
- Mock backend.get_user to return a TEST_USER instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter the TEST_TICKET's name in element  `#buyform_input_name`
- Enter the number 50 into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows successful
- Open /logout (clean up)

### Test Cases R6.4.1: /buy[post] The ticket name exists in the database - Positive.
Mocking:  
- Mock backend.get_user to return a TEST_USER instance
- Mock backend.get_ticket to return a TEST_TICKET instance

Actions:
- Open /logout (to invalidate any logged-in sessions that may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element input[type="submit"]
- Open /
- Navigate to element `#buyform`
- Enter TEST_TICKET's name into element  `#buyform_input_name`
- Enter TEST_TICKET's quantity into element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows successful
- Open /logout (clean up)

### Test Cases R6.4.2: /buy[post] The ticket name exists in the database - Negative.  
Mocking:  
- Mock backend.get_user to return a TEST_USER instance
- Mock backend.get_ticket to return a TEST_TICKET instance

Actions:  
- Open /logout (to invalidate any logged-in sessions that may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element input[type="submit"]
- Open /
- Navigate to element `#buyform`
- Enter "testTicketNonexisted" into element  `#buyform_input_name`
- Enter TEST_TICKET's quantity into element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the `#buy_message` element shows an error message stating "The ticket does not exist". 
- Open /logout (clean up)

### Test Cases R6.4.3: /buy[post] The quantity is more than the quantity requested to buy - Positive.

Additional Test Data:
```
TEST_TICKET_info = {
    name='TEST_TICKET',
    quantity=50
    price=10,
    date='20200901'
}
```
Mocking:  
- Mock backend.get_user to return a TEST_USER instance
- Mock backend.get_ticket to return a TEST_TICKET instance
- Mock backend.get_ticket_info to return a TEST_TICKET_info instance

Actions:
- Open /logout (to invalidate any logged-in sessions that may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element input[type="submit"]
- Open /
- Navigate to element `#buyform`
- Enter TEST_TICKET's name into element  `#buyform_input_name`
- Enter TEST_TICKET's quantity into element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows successful
- Open /logout (clean up)

### Test Cases R6.4.4: /buy[post] The quantity is more than the quantity requested to buy - Negative.  

Additional Test Data:
```
TEST_TICKET_info = {
    name='TEST_TICKET',
    quantity=50
    price=10,
    date='20200901'
}
```

Mocking:  
- Mock backend.get_user to return a TEST_USER instance
- Mock backend.get_ticket to return a TEST_TICKET instance

Actions:  
- Open /logout (to invalidate any logged-in sessions that may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element input[type="submit"]
- Open /
- Navigate to element `#buyform`
- Enter "testTicketNonexisted" into element  `#buyform_input_name`
- Enter 60 into element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the `#buy_message` element shows an error message stating "The quantity is less than the quantity requested". 
- Open /logout (clean up)

### Test Cases R6.5.1: /buy[post] The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) - Positive.

Mocking:  
- Mock backend.get_user to return a TEST_USER instance
- Mock backend.get_ticket to return a TEST_TICKET instance

Actions:
- Open /logout (to invalidate any logged-in sessions that may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element input[type="submit"]
- Open /
- Navigate to element `#buyform`
- Enter TEST_TICKET's name into element  `#buyform_input_name`
- Enter TEST_TICKET's quantity into element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#buy_message` element shows successful
- Open /logout (clean up)

### Test Cases R6.5.2: /buy[post] The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) - Negative. 
Additional test data
```
test_user2 = User(
    email='testFrontend2@test.com',
    name='testFrontend2',
    password=generate_password_hash('testFrontend2')
    balance = 5
)
```

Mocking:  
- Mock backend.get_user to return a TEST_USER instance
- Mock backend.get_ticket to return a TEST_TICKET instance

Actions:  
- Open /logout (to invalidate any logged-in sessions that may exist)
- Open /login
- Enter test_user2's email into element `#email`
- Enter test_user2's password into element `#password`
- Click element input[type="submit"]
- Open /
- Navigate to element `#buyform`
- Enter TEST_TICKET's name into element  `#buyform_input_name`
- Enter TEST_TICKET's quantity into element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the `#buy_message` element shows an error message stating "Must have more balance than the ticket price * quantity + service fee (35%) + tax (5%"). 
- Open /logout (clean up)

### Test Case R5.6.1:  For any errors, redirect back to / and show an error message.  
Mocking:    
- Mock backend.get_user to return a TEST_USER instance
- Mock backend.get_ticket to return a TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter TEST_USER's email into element `#email`
- Enter TEST_USER's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to element `#buyform`
- Enter " no!tATicket " in element  `#buyform_input_name`
- Enter -1 quantity into the element  `#buyform_input_quantity`
- Click element `#buyform_submit`
- Validate that the page has been redirected to /
- Validate that the `#update_message` element contains an error message."
- Open /logout (clean up)
