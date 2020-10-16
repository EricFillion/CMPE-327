
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



### R3: /


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


### /*