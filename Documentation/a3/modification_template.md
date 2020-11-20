# Question:Descriptions on how you modified the template to conduct the testing if any. If you propose a different approach than the template, explain how you did that and justify why.

- PR template Modification:
   - Description:

     1.  A summary of what the pull request changes: all reviewers are able to figure out what have been changed quickly.
     2.  Sections of the assignment's guidelines this pull request addresses: find out which requirement or constraint this PR addresses.
     3.  Issues this pull request addresses: all reviewers are able to see which issue is related to this PR.

   - Type:

      1.  Bug Fix: this checkbox shows that current PR is resolving bugs.
      2.  New Feature: this checkbox shows that current PR is add new features to project.
      3.  New test case(s): this checkbox shows that current PR is add new test cases.
      4.  Refactoring/cleaning: this checkbox shows that current PR is deleting codes from project.
      5.  Breaking change: this checkbox shows that current PR contains breaking change, should be reviewed carefully.
      6.  Documentation: this checkbox shows that current PR is adding documentation for project.

   - Testing:
      1.  Describe any testing you accomplished and provide instructions on how to replicate it: all reviewers can view the accomplishment of current test cases and reproduce test case if test failed.
   
   - Checklist:

      1.  Ran PyLint and have resolved any fixable formatting errors: ensure every PR is formatted for better readability.
      2.  Included comments to describe how the code works: all reviewers can understand the logic of codes .
      3.  Ran new and existing unit tests locally without causing any warnings or errors: all code must be ran under local env before PR.
      4.  No unneeded modifications within the pull request, which for example may be caused by using "git add .": PR should not contain unrelated file change.
      5.  If the pull request contains any merge conflicts, then please address them at the time of creating the pull request: avoid merge conflicts

- Code Modification:

  - R1:
    - Added method and action attribute to the form element (id and ) within login.html so that R1.5 could be completed.

    - Add email and password validation in order to meet requirements and constraints.
      - Check that the email is not blank
      - Uses an open sourced library called email_validator to ensure the email conforms to RFC 5322 guidelines
      - Password validation
        1. Password must not be blank
        2. Password be at least 6 characters long
        3. Password must have at least one lowercase
        4. Password must have at least one upper case
        5. Password must have at least one special character.

  - R2:
    - Add username validation in order to meet requirements and constraints (same as R1).
    - Add redirect functionality to register page, so if the user has logged in, redirect to the user profile page.
  - R3: - Add a model for Ticket. It contains a unique ID, name,
    quantity, price, and a foreign key relationship to the User who owns it.
    Testing was done by manually adding a ticket to the SQLite database:
    insert into ticket (name, quantity, price, owner_id) values ('Test Movie', 2, 1500, 1);
  
    - Reset the database in order to properly add the changes to
      the model. In the future I think we may want to look into automating
      the creation of the test database (independent of the qa327_test stuff).
    - Bug fixing: if you keep a webpage logged in, shut down
      the server, remove the database file, and restart the server,
      and then refresh the page, it will cause an error in the server.
      I fixed this in frontend.py by invalidating the 'logged_in' key in
      the session and redirecting to /login
  
  - R7:
  
    - Nothing changed
  
  - R8:
    - Added custom page/template for if a 404 error occurs. On the page there is a 'Return to Homepage' link that the user can click to be  redirected to to the main page '/' if already logged in else it will redirect to login page.
