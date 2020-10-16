
# Test Cases Summary Table

| Specification                                                                     | Test Case ID | Purpose                                                                                                 |
|-----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------|
| If the user hasn't logged in, show the login page                                 | R1.1         | Check if the login page is shown if the user hasn’t logged in                                           |
| The login page has a message that by default says 'please login'                  | R1.2         | Check if the correct message is displayed on the login page                                             |
| If the user has logged in, redirect to the user profile page                      | R1.3         | To confirm that the user is brought to the correct page if they are logged in                           |
| The login page provides a login form which requests two field: email and password | R1.4         | To confirm that the login page contains both an email and password form                                 |
| The login form can be submitted as a post request to the current URL (/login)     | R1.5         | To check if the user can login via a post request                                                       |
| Email and password cannot be empty.                                               | R1.6.1       | Login automatically fails if email is empty.                                                            |
| Email and password cannot be empty.                                               | R1.6.2       | Login automatically fails if the password is empty.                                                     |
| Email has to follow addr-specs defined in RFC 5322.                               | R1.7.1       | Login email cannot have a “.” as the first character, or else login fails                               |
| Email has to follow addr-specs defined in RFC 5322.                               | R1.7.2       | Login email must have an “@” symbol, or else login fails                                                |
| Email has to follow addr-specs defined in RFC 5322.                               | R1.7.3       | Login email cannot have a special character like “!”, or else login fails                               |
| Email has to follow addr-specs defined in RFC 5322.                               | R1.7.4       | Login email  must end with a “.xxx” where “xxx” specified a valid Top Level Domain, or else login fails |
| Password has to meet required complexity                                          | R1.8.1       | Login automatically fails if the password is less than 6 characters                                     |
| Password has to meet required complexity                                          | R1.8.2       | Login automatically fails if password does not contain at least one lowercase letter                    |
| Password has to meet required complexity                                          | R1.8.3       | Login automatically fails if password does not contain at least one special character                   |
| Password must contain one upper case                                              | R1.8.4       | Login automatically fails if password does not contain at least one uppercase letter                    |
| If email/password are correct, redirect to /                                      | R1.9         | Confirm that the web application redirect to the home page if the user logs in successfully             |
| If email/password are not correct, redirect to /login                             | R1.10        | Check that the web application redirects to the login page if the user does not successfully login      |


### R2: /register
| Specification                              | Test Case ID | Purpose                                                                                                 |
|------------------------------------|--------------|---------------------------------------------------------------------------------------------------------|
| If the user has logged in, redirect back to the user profile page| R2.1 | To avoid repeat login, if they have logged |
| otherwise, show the user registration page the registration page shows a registration form requesting: email, user name, password, password2 | R2.2,R2.3 |  To make sure everyone can register if they haven’t login |
| check email not empty validation | R2.4.1 | Email cannot be empty for registration  
| check password not empty validation | R2.4.2 | Password cannot be empty for registration
| Email has to follow addr-spec defined in RFC 5322 | R2.4.3  |  Email must be real, follow rules
| Password has minimum length 6 | R2.4.4.1  |  Password must be save enough,make it hard to decode
| Password has at least one upper case  |   R2.4.4.2  | Password must be save enough,make it hard to decode
| Password has at least one lower case  | R2.4.4.3  | Password must be save enough,make it hard to decode
| Password has  at least one special letter | R2.4.4.4  | Password must be save enough,make it hard to decode
| User name has to be non-empty | R2.5.1  | User cannot have empty username
| User name has to be alphanumeric-only | R2.5.2  | User should have formal username
| User name has to be space allowed only if it is not the first or the last character | R2.5.3  | User cannot have a name with spaces at head or end of it, we don’t offer trim
| If the email already exists, show message 'this email has been ALREADY used'  | R2.6  | User cannot have two accounts with same email for out website
| User name has to be longer than 2 characters  | R2.7.1  | User should have a longer name
| User name has to be less than 20 characters | R2.7.2  | User cannot have a very long name 
| check password repeat validation  | R2.8  | If passwords are not same then impossible for website to confirm
| The registration form can be submitted as a POST request to the current URL (/register) | R2.9  |The form must be submitted to specific endpoint, otherwise the form action is useless
| If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page  | R2.10 | User must login after they register a account


### R3: /
| Specification                                                                     | Test Case ID | Purpose                                                                                                 |
|-----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------|
| If the user is not logged in, redirect to login page | R3.1 | The homepage can't be accessed unless the user is logged in and has a valid session |
| This page shows a header 'Hi {}'.format(user.name) | R3.2 | The homepage should greet the user :) |
| This page shows user balance | R3.3 | The user must be able to see their balance on the homepage (since this is where they buy and sell tickets) |
| This page shows a logout link, pointing to /logout | R3.4 | The user must be able to log out of the service |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.1 | This is a positive test case with only valid tickets, to ensure that all of the correct information is displayed for all of the tickets. |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.2 | This is a test case that exercises the frontend's exclusion of expired tickets. Both expired and valid tickets will be present, and there are checks to ensure no expired tickets are displayed. |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.3 | This is a test case that exercises the frontend's exclusion of expired tickets. Only expired tickets will be present, and there is a check to ensure that the ticket table is not shown and instead a message stating there are no tickets available is shown. |
| This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired. | R3.5.4 | This is a test case that exercises the frontend's ability to display an empty ticket list. No tickets will be present, and there is a check to ensure that the ticket table is not shown and instead a message stating there are no tickets available is shown. |
| This page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date | R3.6 | This tests that the sale form is present and has all the required fields. |
| This page contains a form that a user can buy new tickets. Fields: name, quantity | R3.7 | This tests that the purchase form is present and has all the required fields. |
| This page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date | R3.8 | This tests that the update form is present and has all the required fields. |
| The ticket-selling form can be posted to /sell | R3.9 | This tests that the sale form can be posted successfully to the /sell endpoint. |
| The ticket-buying form can be posted to /buy | R3.10 | This tests that the purchase form can be posted successfully to the /buy endpoint. |
| The ticket-update form can be posted to /update | R3.11 | This tests that the update form can be posted successfully to the /update endpoint. |


### R4: /sell
| Specification                                                                     | Test Case ID | Purpose                                                                                                 |
|-----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------|
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character. | R4.1.1       | Confirm that selling action fails if the ticket’s name is non-alphanumeric                                                                 |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character. | R4.1.2       | Confirm that ticket selling actions succeeds if there is a space in the middle of alphanumeric text                                        |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character. | R4.1.3       | Selling actions fails if the first character is space                                                                                      |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character. | R4.1.4       | Selling actions fails if the last character is space                                                                                       |
| The name of the ticket is no longer than 60 characters                                                               | R4.2.1       | Selling actions fails if the name of the ticket is 61 characters long                                                                      |
| The name of the ticket is no longer than 60 characters                                                               | R4.2.2       | Selling actions succeeds if the length of the ticket is 60 characters long                                                                 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                                    | R4.3.1       | Selling actions fails if the quantity sold is less than 1                                                                                  |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                                    | R4.3.2       | Selling action succeeds if the quantity sold is 1 or more                                                                                  |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                                    | R4.3.3       | Selling action fails if quantity sold is more than 100                                                                                     |
| The quantity of the tickets has to be more than 0, and less than or equal to 100.                                    | R4.3.4       | Selling action succeeds if quantity sold is 100. R4.3.2 + R4.3.4 imply tickets can be sold if the quantity is between 1-100 inclusively.   |
| Ticket price has to be in the range [10, 100]                                                                        | R4.4.1       | Selling action succeeds if the price of the ticket is $10                                                                                  |
| Ticket price has to be in the range [10, 100]                                                                        | R4.4.2       | Selling action fails if the price of the ticket is less than $10                                                                           |
| Ticket price has to be in the range [10, 100]                                                                        | R4.4.3       | Selling action succeeds if the price of the ticket is $100.  R4.4.1 + R4.4.3 imply tickets can be sold if the price is  $1-100 inclusively |
| Ticket price has to be in the range [10, 100]                                                                        | R4.4.4       | Selling action fails if the price of the ticket is more than $100                                                                          |
| The date must be given in the format YYYYMMDD                                                                        | R4.5.1       | Selling actions fails if the ticket’s date does not match the YYYYMMDD format                                                              |
| The date must be given in the format YYYYMMDD                                                                        | R4.5.2       | Selling actions succeeds if the ticket’s date matches the  YYYYMMDD format                                                                 |
| The added new ticket information will be posted on the user’s profile   





### R5/update


### R6/update


### R6/Buy



### R7 /logout
| Specification                                                                     | Test Case ID | Purpose                                                                                                 |
|-----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------|
| Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.  | R7  | User cannot access any restricted page after they logout



### R8 /* (404 Page)
| Specification                                                                     | Test Case ID | Purpose                                                                                                 |
|-----------------------------------------------------------------------------------|--------------|---------------------------------------------------------------------------------------------------------|
| For any requests except those in the specification's routes table, the system should return a 404 error | R8.1.1 | This test confirms that a non-existent page returns the 404 page. |
| For any requests except those in the specification's routes table, the system should return a 404 error | R8.1.2 | This test confirms that performing an HTTP GET on a POST-only endpoint results in a 404. |
