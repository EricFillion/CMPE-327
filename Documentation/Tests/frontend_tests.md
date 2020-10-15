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

### R7. /logout

### R8. /*

## Test Plan

**How our team organized the documentations of the test cases**

**Our understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub**

Our chosen testing framework is a combination of pytest, SeleniumBase, and unittest's mocking functionality.
It will allow us to have an instance of the server running, with certain backend functions mocked dynamically for each unit test.
Using SeleniumBase for the unit test, we can manipulate a web browser to click on and enter text into different inputs, and assert that the correct text or webpage is displayed.
This will allow us to ensure that our frontend user interface works the way we intended.

The testcases will be executed automatically as a GitHub Action whenever a pull request is created.
The GitHub Action will provide a clean environment for testing, fetch the requirements for the app, run the testcases, and report if any errors occurred.
This will allow us to ensure that all commits going into the codebase are safe and do not break any existing system functionality (it is automated regression testing).

**How we are going to organize different test case code files?**

## Issues

*If we find any conflicts or any issues related to the specification, please create an issue on GitHub (assume that we are on-site customers). Document what we have found in the same markdown here.*
