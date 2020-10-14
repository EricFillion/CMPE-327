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

### R6. /buy

**PreSteps - Login**  
Mocking:    
- Mock backend.get_user to return a test_user instance

Actions:       
- open /logout (to invalid any logged-in sessions may exist)
- open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]` 

#### **R6.5 - The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)**  

Mocking:    
- Mock backend.get_user to return a test_user instance

Actions:       
- open /logout (to invalid any logged-in sessions may exist)
- open /login
- Enter test_user's email into element `#email`
- Enter test_user's password into element `#password`
- Click element `input[type="submit"]`


### R7. /logout

### R8. /*

## Test Plan

**How our team organized the documentations of the test cases**

**Our understanding of how the chosen testing framework works to test the frontend, including yur understandings of when and how the test cases will be running directly on GitHub**

**How we are going to organize different test case code files?**

## Issues

*If we find any conflicts or any issues related to the specification, please create an issue on GitHub (assume that we are on-site customers). Document what we have found in the same markdown here.*
