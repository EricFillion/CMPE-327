# Question: Descriptions on how you modified the template to conduct the testing if any. If you propose a different approach than the template, explain how you did that and justify why.

The team followed the provided template for structuring and running the test cases.  As per the template, tests are run with each push to the repository. Also, they are divided into classes where each class is for a page of the front-end. Then, each class contains methods that act as single tests for each requirement.
 
The main difference between our test cases and the template is how we introduced functionality for auto login. That way, for the test cases, the team did not have to repeat the same code each time we wanted to simulate a user logging in. This was done by creating a function decorator called "auto_login".  The decorator takes in a user class, which contains all of the user's information such as their email address, password and balance, and then uses this information to mock the login functions in the backend and use the web interface to log in prior to running the decorated test function. In addition, the decorator also automatically performs logout after the code from the calling function is done.
 
Overall, the team followed the given template, and also expanded upon the template by adding unique auto login functionality which led to clean and concise code.

Note: This answer is identical to the one we submitted in A3 for the same question, as we have not made any additional changes. 
