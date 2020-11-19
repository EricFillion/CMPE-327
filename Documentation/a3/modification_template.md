# Question:Descriptions on how you modified the template to conduct the testing if any. If you propose a different approach than the template, explain how you did that and justify why.
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
- R3:
    - Add a model for Ticket. It contains a unique ID, name,
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
  - Added custom page/template for if a 404 error occurs. On the page there is a 'Return to Homepage' link that the user can click to be redirected to to the main page '/' if already logged in else it will redirect to login page.