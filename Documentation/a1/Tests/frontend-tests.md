# Seet Geek Frontend Tests


**How our team organized the documentations of the test cases**  
All of the documentation of the test cases are in the *Documentation/Tests* folder. We created the Documentation folder to have a centralized place to have all our documentation. The subfolder called *Tests* was created as a place for all our test documentation. For our documentation we have one main file called *frontend_tests.md* (this file) which contains our test case summarization table, our test plan, and issues that we encountered. We also created individual md files for each requirement/specification. These files are also located in */Documentation/Tests/* and are named based on the requirement in the form "R{requirement_number} {route}.md" (ex. *R1-login.md*). 

We are also have a separate file that summarizes the test cases under *Documentation/Tests/test-cases-summary.md*. This table has its own dedicated file to make it easier to manage and to make our files more readable by not being too long. 

**Our understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub**
Our chosen testing framework is a combination of PyTest, SeleniumBase, and unittest's mocking functionality.
It will allow us to have an instance of the server running, with certain backend functions mocked dynamically for each unit test.
Using SeleniumBase for the unit test, we can manipulate a web browser to click on and enter text into different inputs and assert that the correct text or webpage is displayed.
This will allow us to ensure that our front-end user interface works the way we intended.

The test cases will be executed automatically as a GitHub Action whenever a pull request is created.
GitHub Actions will provide a clean environment for testing, fetching the requirements, and running the test cases.
Each action outputs a report that indicates if any errors occurred, so that the team can quickly identify potential bugs.
GitHub Actions will ensure that all commits going into the codebase are safe and do not break any existing system functionality while saving the team time.

**How we are going to organize different test case code files?**  
We are going to have our test cases in *qa327_test/frontend*.  In this folder there will be  subfolders, one for each route/requirement. These folders will have python files for each of the request types for that requirement. For example there will be a login folder with a file for the get request tests and the post request tests. The files will all have the same name convention. They will be named *test_{requirement_number}_{requirement_name}_{request_type}*.py. For instance for the login example the get test file will be called *test_r2_login_get.py*.

In each of the python test case code files we will import all the necessary testing libraries, described above, such as pytest, seleniumbase, and unitttest.mock.

We will also create a YAML configuration file for the automatic running of the testcases using github actions. It will be located at */.github/workflows/tests.yml*. This file will be set up similar to the example given here: https://www.techiediaries.com/python-unit-tests-github-actions/


## Issues
*The conflicts and issues related to the specification that we found. For these issue we created an issue on GitHub for the on site customer and then documented what we found here*
- Issue 1: Unsure of the need to check R6:1-3(Buy requirments) as these requirements are checked when the ticket is created. We were informed that these needed to be checked in case of issues such as user trying to enter a data with malicious intent. 
- [Issue 2](https://github.com/EricFillion/CMPE-327/issues/9): There was a discrepancy between the specifications provided for the logout endpoint, where the routing table stated both GET and POST support but the requirement only stated POST support. The resolution was to add GET support to the requirement.
