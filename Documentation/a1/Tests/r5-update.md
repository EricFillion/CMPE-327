## R5. /update

Description:  user can update a ticket for sale. Fields: name, quantity, price, expiration date.


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

Note: This test ticket will be a ticket that is already in the mock database, so that it can be updated. 
```
TEST_TICKET = Ticket(
    name="t1",
    quantity=90,
    price=100,
    expiry=date(2030, 1, 1),
    owner_id="test_owener_id",
    owner=TEST_USER,
)
TEST_TICKET.raw_expiry = "20301001"
```

### Test Case R5.1.1: The name of the ticket has to be alphanumeric-only - Negative. 

Mocking:      
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter a string containing symbols (ex. "t!cket_1") into the element `#updateform_input_name`
- Enter the TEST_TICKET's quantity in element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating “Unable to update ticket: The name of the ticket has to be alphanumeric only”.
- Open /logout (clean up)

### Test Case R5.1.2:  The name is only allowed spaces if it is not the first or the last character - Negative. Testing the first character.  
Mocking:      
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:       
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Enter a string, that is less than 60 characters, containing only alphanumeric symbols that has a space for the first character  (ex. " t1")in the element `#updateform_input_name`
- Enter the TEST_TICKET's quantity in element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating “Unable to update ticket: The name of the ticket is only allowed spaces if it is not the first or last character”.
- Open /logout (clean up)

### Test Case R5.1.3:  The name is only allowed spaces if it is not the first or the last character - Negative. Testing the last character.
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:       
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter a string that is less than 60 characters, containing only alphanumeric symbols that has a space for the last character (ex. "t1 ") in the element `#updateform_input_name`
- Enter the TEST_TICKET's quantity in element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “The name of the ticket is only allowed spaces if it is not the first or last character”.
 - Open /logout (clean up)

### Test Case R5.1.4:  The name is only allowed spaces if it is not the first or the last character - Positive.
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter a string that is less than 60 characters, containing only alphanumeric symbols that contains spaces that are not the first and last character (ex. "ticket 1") in the element `#updateform_input_name`
- Enter the TEST_TICKET's quantity in element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_info` element shows "Ticket was updated successfully"
- Open /logout (clean up)

 
### Test Case R5.1.5: Updating to a valid name - Positive. 
Mocking:       
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter test tickets's name into the element `#updateform_input_name`
- Enter the TEST_TICKET's quantity in element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_info` element shows "Ticket was updated successfully"
- Open /logout (clean up)

### Test Case R5.2:  The name of the ticket is no longer than 60 characters - Negative.
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter “aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa” (61 chars) in the element element `#updateform_input_name`
- Enter the TEST_TICKET's quantity in element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: The name of the ticket should be no longer than 60 characters”.
- Open /logout (clean up)

### Test Case R5.3.1:  The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative. Testing quantity below range.
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET's name in element `#updateform_input_name`
- Enter a number less than or equal to 0 (ex.-1) into the element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: The quantity of the ticket must be between 1 and 100”.
- Open /logout (clean up)

### Test Case R5.3.2: The quantity of the tickets has to be more than 0, and less than or equal to 100 - Negative. Testing quantity above range.  
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET's name in element `#updateform_input_name`
- Enter a number greater than 100 (ex. 101) into the element `#updateform_input_quantity`
- Enter the TEST_TICKET's price in element `#updateform_input_price`
- Enter the TEST_TICKET's expiry date in element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: The quantity of the ticket must be between 1 and 100”.
- Open /logout (clean up)

### Test Case R5.3.3:  The quantity of the tickets has to be more than 0, and less than or equal to 100 - Positive. 

Mocking:       
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET’s name into the element `#updateform_input_name`
- Enter the number 50 into the element `#updateform_input_quantity`
- Enter the TEST_TICKET’s price into the element `#updateform_input_price`
- Enter the TEST_TICKET’s date into the element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_info` element shows "Ticket was updated successfully"
- Validate that current page contains a #ticket-name header matching the tickets name.
- Open /logout (clean up)

### Test Case R5.4.1:  Price has to be of range [10, 100] - Negative. Testing price below the range. 
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET’s name into the element `#updateform_input_name`
- Enter the TEST_TICKET’s quantity into the element `#updateform_input_quantity`
- Enter a number below 10 (ex. 9) into the element `#updateform_input_price`
- Enter the TEST_TICKET’s date into the element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: The price of the ticket must be between 10 and 100”.
- Open /logout (clean up)

### Test Case R5.4.2:  Price has to be of range [10, 100] - Negative. Testing price above the range. 
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET’s name into the element `#updateform_input_name`
- Enter the TEST_TICKET’s quantity into the element `#updateform_input_quantity`
- Enter a number above 100 (ex. 101) into the element `#updateform_input_price`
- Enter the TEST_TICKET’s date into the element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: The price of the ticket must be between 10 and 100”.
- Open /logout (clean up)

### Test Case R5.4.3: Price has to be of range [10, 100] - Positive.  

Mocking:       
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET’s name into the element `#updateform_input_name`
- Enter the TEST_TICKET’s quantity into the element `#updateform_input_quantity`
- Enter the number 50 into the element `#updateform_input_price`
- Enter the TEST_TICKET’s date into the element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_info` element shows "Ticket was updated successfully"
- Validate that current page contains a #ticket-name header matching the tickets name.
- Open /logout (clean up)

### Test Case R5.5.1:  Date must be given in the format YYYYMMDD (e.g. 20200901) - Negative.    
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET’s name into the element `#updateform_input_name`
- Enter the TEST_TICKET’s quantity into the element `#updateform_input_quantity`
- Enter the TEST_TICKET’s price into the element `#updateform_input_price`
- Enter a date in an invalid format (ex. 20201331) into the element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: Date must be given in the format YYYYMMDD (e.g. 20200901)”.
- Open /logout (clean up)

### Test Case R5.5.2:  Date must be given in the format YYYYMMDD (e.g. 20200901) - Positive.   
Mocking:       
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance

Actions:        
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter the TEST_TICKET’s name into the element `#updateform_input_name`
- Enter the TEST_TICKET’s quantity into the element `#updateform_input_quantity`
- Enter the TEST_TICKET’s price into the element `#updateform_input_price`
- Call function to get todays date and enter date into the element `#updateform_input_expiry`. Todays date is used so that the date is never in the past. 
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_info` element shows "Ticket was updated successfully"
- Validate that current page contains a #ticket-name header matching the tickets name.
- Open /logout (clean up)

### Test Case R5.6.1:  The ticket of the given name must exist - Negative.  
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance
- Mock backend.get_all_tickets to return all tickets 

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter "nonExistentTicket" in element `#updateform_input_name`
- Enter the TEST_TICKET's name in element `#updateform_input_name`
- Enter the TEST_TICKET’s quantity into the element `#updateform_input_quantity`
- Enter the TEST_TICKET’s price into the element `#updateform_input_price`
- Enter the TEST_TICKET’s date into the element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element shows an error message stating  “Unable to update ticket: The ticket of the given name must exist."
- Open /logout (clean up)

### Test Case R5.7.1:  For any errors, redirect back to / and show an error message.  
Mocking:    
- Mock backend.get_user to return a test_user instance 
- Mock backend.get_ticket to return the TEST_TICKET instance
- Mock backend.get_all_tickets to return all tickets 

Actions:     
- Open /logout (to invalid any logged-in sessions may exist)
- Open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`
- Open /
- Navigate to the form `#updateform`
- Enter " no!tATicket " in element `#updateform_input_name`
- Enter the TEST_TICKET’s quantity into the element `#updateform_input_quantity`
- Enter the TEST_TICKET’s price into the element `#updateform_input_price`
- Enter the TEST_TICKET’s date into the element `#updateform_input_expiry`
- Click element `#updateform_submit`
- Validate that the page shows element `#welcome`
- Validate that the `#message_error` element is shown."
- Open /logout (clean up)
