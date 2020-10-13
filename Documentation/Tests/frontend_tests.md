# Seet Geek Frontend Tests

## Test Case Summarization Table

## Test Cases

**EXAMPLE/TEMPLATE TO USE FOR TEST CASES DELETE BEFORE SUMBMITTING**   

Mocking:
 - Mock backend.get_user to return a test_user instance 
 
Actions:
 - open /logout (to invalid any logged-in sessions may exist)
 - open /login
 - enter test_user's email into element `#email`
 - enter test_user's password into element `#password`
 - click element `input[type="submit"]`
 - open /login again
 - validate that current page contains `#welcome-header` element


### R1. /Login

### R2. /Register

### R3. /

### R4. /sell

### R5. /update
**Description:**  user can update a ticket for sale. Fields: name, quantity, price, expiration date.


#### **Test Data**
Note: This test ticket will be a ticket that is already in the moch database, so that it can be updated. 
```
the test_tickets = [
    {'name': 't1', 'price': '100', date: '20301001', quantity: '90'}
]
```


**PreSteps - Login**  
Mocking:    
- Mock backend.get_user to return a test_user instance

Actions:       
- open /logout (to invalid any logged-in sessions may exist)
- open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]` 


#### **Test Case R5.1.1 - The name of the ticket has to be alphanumeric-only** 

Mocking:       
- Mock backend.get_ticket to return a the test_ticket instance

Actions:        
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a string containing symbols (ex. "t!cket_1") into the element `#update-name`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “The name of the ticket has to be alphanumeric only”.


#### **Test Case R5.1.2 -  The name is only allowed spaces if it is not the first or the last character. Testing the first character.**  
Mocking:      
- Mock backend.get_ticket to return a the test_ticket instance

Actions:       
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a string, that is less than 60 characters, containing only alphanumeric symbols that has a space for the first character  (ex. " t1")in the element `#update-name`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to'/'and shows an error message stating “The name of the ticket is only allowed spaces if it is not the first or last character”.
 
#### **Test Case R5.1.3 -  The name is only allowed spaces if it is not the first or the last character. Testing the last character.**
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:       
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a string that is less than 60 characters, containing only alphanumeric symbols that has a space for the last character (ex. "t1 ") in the element `#update-name`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “The name of the ticket is only allowed spaces if it is not the first or last character”.
 
#### **Test Case R5.1.4 -  The name is only allowed spaces if it is not the first or the last character. Testing valid space input.**
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:     
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a string that is less than 60 characters, containing only alphanumeric symbols that contains spaces that are not the first and last character (ex. "ticket 1") in the element `#update-name`
- Click element `input[type="submit"]` 
- Validate that  the form has been successfully submitted and that the page contains a ticket-updated  message.
 
#### **Test Case R5.1.5 - Updating a to a valid name.** 

Mocking:       
- Mock backend.get_ticket to return a the test_ticket instance

Actions:        
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a the valid string "updatedName" into the element `#update-name`
- Click element `input[type="submit"]` 
- Validate that the form has been successfully submitted and that the page contains a ticket-updated message.
- Validate that current page contains a #ticket-name header matching the tickets name.

#### **Test Case R5.2 -  The name of the ticket is no longer than 60 characters**
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:     
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a string that containing only alphanumeric symbols that is more than 60 characters in the element `#update-name`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “The name of the ticket should be no longer than 60 characters”.

#### **Test Case R5.3.1 -  The quantity of the tickets has to be more than 0, and less than or equal to 100. Testing quantity below range.**
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:     
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a number less than or equal to 0 (ex. -1) into the element `#update-quantity`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “The quantity of the tickets has to be more than 0, and less than or equal to 100”.

#### **Test Case R5.3.2 - The quantity of the tickets has to be more than 0, and less than or equal to 100. Testing quantity above range.**  
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:     
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a number greater than 100 (ex. 101) into the element `#update-quantity`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “The quantity of the tickets has to be more than 0, and less than or equal to 100”.

#### **Test Case R5.3.3 -  The quantity of the tickets has to be more than 0, and less than or equal to 100. Entering valid price** 

Mocking:       
- Mock backend.get_ticket to return a the test_ticket instance

Actions:        
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter the number 50 into the element `#update-quantity`
- Click element `input[type="submit"]` 
- Validate that the form has been successfully submitted and that the page contains a ticket-updated message.
- Validate that current page contains a #ticket-name header matching the tickets name.

#### **Test Case R5.4.1 -  Price has to be of range [10, 100]. Testing price below the range.** 
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:     
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a number below 10 (ex. 9) into the element `#update-price`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “The price of the ticket must be between 10 and 100”.

#### **Test Case R5.4.2 -  Price has to be of range [10, 100]. Testing price above the range.** 
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:     
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a number above 100 (ex. 101) into the element `#update-price`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “The price of the ticket must be between 10 and 100”.


#### **Test Case R5.4.3 - Price has to be of range [10, 100]. Testing price in the range.**  

Mocking:       
- Mock backend.get_ticket to return a the test_ticket instance

Actions:        
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter the number 50 into the element `#update-price`
- Click element `input[type="submit"]` 
- Validate that the form has been successfully submitted and that the page contains a ticket-updated message.
- Validate that current page contains a #ticket-name header matching the tickets name.

#### **Test Case R5.5.1 -  Date must be given in the format YYYYMMDD (e.g. 20200901). Invalid format test**  
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance

Actions:     
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Enter a date in an invald format (ex. 20201331) into the element `#update-date`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating “Date must be given in the format YYYYMMDD (e.g. 20200901)”.

#### **Test Case R5.5.2 -  Date must be given in the format YYYYMMDD (e.g. 20200901). Valid format test**  
Mocking:       
- Mock backend.get_ticket to return a the test_ticket instance

Actions:        
- Navigate to the update ticket form
- Enter the test_ticket's name in element `#ticket-to-update`
- Call function to get todays date and enter date into the element `#update-date`. Todays date is used so that the date is never in the past. 
- Click element `input[type="submit"]` 
- Validate that the form has been successfully submitted and that the page contains a ticket-updated message.
- Validate that current page contains a #ticket-name header matching the tickets name.

#### **Test Case R5.6 -  The ticket of the given name must exist.**
Mocking:    
- Mock backend.get_ticket to return a the test_ticket instance
- Mock backend.get_all_tickets to return all tickets 

Actions:     
- Navigate to the update ticket form
- Enter generate a random string and check that it is not a name in get_all_tickets, if it is regenerate the string until it does not match. Enter the string in `#ticket-to-update`
- Enter the test_ticket's name in element `#update-name`
- Enter the test_ticket’s price into the element `#update-price`
- Enter the test_ticket’s quantity into the element `#update-quantity`
- Enter the test_ticket’s date into the element `#update-date`
- Click element `input[type="submit"]` 
- Validate that the page has been redirected back to '/' and shows an error message stating "The ticket of the given name must exist."


### R6. /logout

### R7. /*

## Test Plan

**How our team organized the documentations of the test cases**

**Our understanding of how the chosen testing framework works to test the frontend, including yur understandings of when and how the test cases will be running directly on GitHub**

**How we are going to organize different test case code files?**

## Issues

*If we find any conflicts or any issues related to the specification, please create an issue on GitHub (assume that we are on-site customers). Document what we have found in the same markdown here.*
