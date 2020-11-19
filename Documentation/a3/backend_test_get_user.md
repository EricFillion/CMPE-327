# Backend Testing of Get_User function

Selected one backend method unit/method (`get_user`) and created a backend unit test case using a black box systematic approach (input partitioning) we covered so far. This is documentation of the analysis, showing input partitions and test cases for each partition.

The following is a table of the input partitions:

|     Partition    |     Email   Input    |
|-|-|
|     P1     |     Empty string    |
|     P2          |     Email/String with invalid format    |
|     P3    |     Nonexistent email    |
|     P4    |     Valid and existent user email    |
   
   
### P1:  Empty string
**Input**: ""   
**Output**: None

Actions:
 - Call get user with input ""
 - Assert that returned user is equal to None  
   
    
### P2:  Email/String with invalid format
**Input**: "invalid_email"   
**Output**: None

Actions:
 - Call get user with input "invalid_email"
 - Assert that returned user is equal to None   
    
   
### P3:  Nonexistent email
**Input**: "nonexistant_user@example.com"   
**Output**: None
   
Actions:
 - Delete all users in database that have email "nonexistant_user@example.com" (Note it is not possible for a non test user to have this email)
 - Call get user with input "nonexistant_user@example.com"
 - Assert that returned user is equal to None  

        
### P4:  Valid and existent user email
**Input**: "test_backend@example.com"   
**Output**: User(
    email='test_backend@example.com',
    name='Test Email Input', 
    password= `generated password hash of 'q1w2e3Q!W@E#'`, 
    balance=5000
)
   
Actions:
 - Remove user with email "test_backend@example.com" if exists
 - Add user with email: 'test_backend@example.com', name:'Test Email Input', password: 'q1w2e3Q!W@E#' and balance:5000
 - Call get user with input "test_backend@example.com'"
 - Assert that returned user is equal to the added user
 - Delete user
