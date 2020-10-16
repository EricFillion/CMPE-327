
# Test Cases Summary Table

### R1: /login

### R2: /register

### R3: /

### R4: /sell

### R5/update

| Specification  | Test Case ID | Purpose  |
|-|-|-|
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R5.1.1 | Confirm that updating action fails if the ticket’s name is non-alphanumeric  |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R5.1.2 | Confirm updating actions fails if the first character is space. |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R5.1.3 | Confirm updating actions fails if the last character is space. |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R5.1.4 | Confirm that ticket updating actions succeeds if there is a space in the middle of alphanumeric text |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R5.1.5 | Confirm that ticket updating actions succeeds if the name of the ticket is valid |
| The name of the ticket is no longer than 60 characters | R5.2.1 | Confirm updating actions succeeds if the name of the ticket is less than 60 characters long  |
| The name of the ticket is no longer than 60 characters | R5.2.2 | Confirm updating actions fail if the length of the ticket is more than 60 characters long  |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R5.3.1 | Confirm updating actions fails if the quantity sold is less than 1 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R5.3.2 | Confirm updating action fails if quantity sold is more than 100 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R5.3.3 | Confirm updating action succeeds if the quantity sold is between 1 and 100 |
| Ticket price has to be in the range [10, 100] | R5.4.1 | Confirm updating action fails if the price of the ticket is $9 (less than $10). |
| Ticket price has to be in the range [10, 100] | R5.4.2 | Confirm updating action fails if the price of the ticket is  $101 (more than $100). |
| Ticket price has to be in the range [10, 100] | R5.4.3 | Confirm updating action succeeds if the price of the ticket is between $ 10-10 inclusively. |
| The date must be given in the format YYYYMMDD | R5.5.1  | Confirm updating actions fails if the ticket’s date does not match the YYYYMMDD format |
| The date must be given in the format YYYYMMDD | R5.5.2 | Confirm updating actions succeeds if the ticket’s date matches the  YYYYMMDD format |
| The ticket of the given name must exist | R5.6.1 | Confirm updating action fails if the ticket does not exist  |
| The ticket of the given name must exist | R5.6.2 | Confirm updating action succeeds if the ticket of the given name exists |


### R6/Buy
| Specification  | Test Case ID | Purpose  |
|-|-|-|
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R6.1.1 | Confirm that buying action fails if the ticket’s name is non-alphanumeric  |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R6.1.2 | Confirm buying actions fails if the first character is space. |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R6.1.3 | Confirm buying actions fails if the last character is space. |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R6.1.4 | Confirm that ticket buying actions succeeds if there is a space in the middle of alphanumeric text |
| The name of the ticket must be alphanumeric-only, and space is only allowed if it’s not the first or last character.   | R6.1.5 | Confirm that ticket buying actions succeeds if the name of the ticket is valid |
| The name of the ticket is no longer than 60 characters | R6.2 | Confirm buying actions succeeds if the name of the ticket is less than 60 characters long  |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R6.3.1 | Confirm buying actions fails if the quantity sold is less than 1 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R6.3.2 | Confirm buying action fails if quantity sold is more than 100 |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R6.3.3 | Confirm buying action succeeds if the quantity sold is between 1 and 100 |
| The ticket name exists in the database and the quantity is more than the quantity requested to buy | R6.4.1 | Confirm buying action succeeds if the ticket of the given name exists |
| The ticket name exists in the database and the quantity is more than the quantity requested to buy | R6.4.2 | Confirm buying action fails if the ticket does not exist  |
| The ticket name exists in the database and the quantity is more than the quantity requested to buy | R6.4.3 | Confirm buying action succeeds if the quantity is more than the quantity requested to buy.  |
| The ticket name exists in the database and the quantity is more than the quantity requested to buy | R6.4.4 | Confirm buying action fails if the quantity is less than the quantity requested to buy. |
| The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) | R6.5.1 | Confirm buying action succeeds if the user has more than the required balance.  |
| The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%) | R6.5.2 | Confirm buying action fails if the user has less than the required balance.  |
| For any errors, redirect back to / and show an error message | R6.6 | Confirm that page is redirected to / and shows an error message if there is an error.  |


### R7 /logout

### R8 /* (404 Page)
