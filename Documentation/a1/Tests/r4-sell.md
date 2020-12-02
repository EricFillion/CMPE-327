
## Sell R4:

**Description**: A user can sell their tickets. 

### Test Data
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```  

Note: This test ticket will be a ticket that is already in the moch database, so that it can be updated. 
```
the test_tickets = [
    {'name': 't1', 'price': '100', date: '20301001', quantity: '90'}
]
```


### R4.1: The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character.

#### R4.1.1: The name of the ticket has to be alphanumeric-only

Mocking:
- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions:
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 

- Enter “abc1234#” in the element `#sellform_input_name`


- Enter test_ticket’s quantity into the element `#sellform_input_quantity`

- Enter test_ticket’s date in the element `#sellform_input_expiry`

- Enter test_ticket’s price into the element `#sellform_input_price`

- Click element input[type = “sell”]

- validate that the #sell_message shows "Sell error"
- open /logout 


#### R4.1.2: Space allowed if not first or last character of the ticket's name

Mocking:
- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions:
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 

- Enter “abc 1234” in the element #name



- Enter test_ticket’s quantity into the element `#sellform_input_quantity`

- Enter test_ticket’s date in the element `#sellform_input_expiry`

- Enter test_ticket’s price into the element `#sellform_input_price`

- Click element input[type = “sell”]

- validate that the #sell_message shows "Successfully sold the ticket"
- open /logout 


#### R4.1.3: Space not allowed if it’s the first character

Mocking:
- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions:
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 

- Enter “ abc1234” in the element `#sellform_input_name`

- Enter test_ticket’s quantity into the element `#sellform_input_quantity`

- Enter test_ticket’s date in the element `#sellform_input_expiry`

- Enter test_ticket’s price into the element `#sellform_input_price`

- Click element input[type = “sell”]

- validate that the #sell_message shows "Sell error"
- open /logout 



#### R4.1.4: Space not allowed if it’s the last character

  
Mocking:
- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions:
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 

- Enter “abc1234 ” in the element `#sellform_input_name`

- Enter test_ticket’s quantity into the element `#sellform_input_quantity`

- Enter test_ticket’s date in the element `#sellform_input_expiry`

- Enter test_ticket’s price into the element `#sellform_input_price`

- Click element input[type = “sell”]

- validate that the #sell_message shows "Sell error"
- open /logout 
  

### 4.2.1 The name of the ticket is no longer than 60 characters - Negative

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
  

Actions

 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter “aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa” (61 chars) in the element #name

- Enter test_ticket’s quantity into the element #quantity

- Enter test_ticket’s date in the element #date

- Enter test_ticket’s price into the element #price

- Click element input[type = “sell”]
- validate that the #sell_message shows "Sell error"
- open /logout 

### 4.2.2 The name of the ticket is no longer than 60 characters - Positive

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
  

Actions

 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter “aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ” (60 chars) in the element #name
- Enter test_ticket’s quantity into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter test_ticket’s price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Successfully sold the ticket"
- - open /logout 


### R4.3 The quantity of the tickets has to be more than 0, and less than or equal to 100.


#### R4.3.1 The quantity of tickets has to be more than 0  - Negative

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter 0 into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter test_ticket’s price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Error selling the ticket"
- - open /logout 

#### R4.3.2 The quantity of tickets has to be more than 0 - Positive

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter 1 into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter test_ticket’s price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Successfully sold the ticket"
- open /logout 



#### R4.3.3 The quantity of tickets has to be less than 101  - Negative

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter 101 into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter test_ticket’s price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Error selling the ticket"
- open /logout



#### R4.3.4 The quantity of tickets has to be less than 101  - Positive

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter 100 into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter test_ticket’s price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Successfully sold the ticket"
- open /logout 


### R4.4 Price has to be of range [10, 100]

#### R4.4.1 The price of tickets has to be more than 9 - Positive

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter test_ticket's quantity into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter 10 into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Successfully sold the ticket"
- open /logout 


#### R4.4.2 The price of tickets has to be more than 9 - Negative

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter test_ticket’s quantity into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter 9 price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Error selling the ticket"
- open /logout

#### R4.4.3 The price of tickets has to be less than 101 - Positive

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter test_ticket’s quantity into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter 100 into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Successfully sold the ticket"
- open /logout 
- 
#### R4.4.4 The price of tickets has to be less than 101 - Negative

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
 
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter test_ticket’s quantity into the element #quantity
- Enter test_ticket’s date in the element #date
- Enter 101 into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Error selling  the ticket"
- open /logout 


### R4.5 The date must given in the format YYYYMMDD 

#### R4.5.1 The date must given in the format YYYYMMDD - Negative

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter test_ticket’s quantity into the element #quantity
- Enter "January 1st, 2021" in the element #date
- Enter  test_ticket’s price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Error selling  the ticket"
- open /logout 

#### R4.5.1 The date must given in the format YYYYMMDD - Positive

Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter test_ticket’s quantity into the element #quantity
- Enter "20210101" in the element #date
- Enter  test_ticket’s price into the element #price
- Click element input[type = “sell”]
- validate that the #sell_message element shows "Successfully sold the ticket!"
- open /logout 

### R4.6 For any errors, redirect back to / and show an error message. 
Mocking:
- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions:
- open `/logout`
- open `/login`
- Enter test_user’s email into element `#email`
- Enter test_user’s password into element `#password`
- Click element `input[type = “submit”]`
- open `/` 
- Enter ' ' in the element `#name`
- Enter test_ticket’s quantity into the element `#quantity`
- Enter test_ticket’s expiry date in the element `#date`
- Enter test_ticket’s price into the element `#price`
- Click element `input[type = “sell”]`
- open `/`
- validate that the `#error_message` element shows "Unable to sell"
- open `/logout`

### R4.7 The added new ticket information will be posted on the user profile page 
Mocking:

- Mock backend.get_user to return a test_ticket instance
- Mock backend.get_user to return a test_user instance
Actions
 - open /logout 
- open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
-  open / 
- Enter test_ticket’s  name in the element #name
- Enter test_ticket’s quantity into the element #quantity
- Enter test_ticket’s quantity  in the element #date
- Enter  test_ticket’s price into the element #price
- Click element input[type = “sell”]
- open /
- validate that the #td.tt_name element is equal to test_ticket’s name
- open /logout 
