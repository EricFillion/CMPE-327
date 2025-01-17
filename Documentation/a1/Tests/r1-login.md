##  Login R1

**Description**: A user can log into the the website using their credentials 

### Test Data
```
TEST_USER = User(
    email='testFrontend@test.com',
    name='testFrontend',
    password=generate_password_hash('testFrontend')
    balance = 200
)
```

### R1.1: if the user hasn’t logged in, show the login page


Mocking:

NA

Actions:

- open /logout

- Validate that current page contains the #log-in header element



### R1.2: The login page has a message that by default says ‘please login’


Mocking:

- NA

 Actions:

- open /logout

- open /login

- Validate that #message element says "Please login"

- open /logout



### R1.3: If the user has logged in, redirect to the user profile page
#### Given as an example

Mocking:

- Mock backend.get_user to return a TEST_USER instance


Actions:

- Open /logout

- Open /login

- Enter TEST_USER’s email into element #email

- Enter TEST_USER’s password into element #password

- Click element input[type = “submit”]

- Validate that current page contains #welcome element

- open /logout



### R1.4 The login page provides a login form which requests two field: email and password

 Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions
- Open /logout

- Open /login

- Validate that the page contains an #email element

- Validate that the page contains a #password element

- open /logout


### R1.5: The login form can be submitted as a post request to the current URL (/login)

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions
- Open /logout

- Open /login

- find element with id "form" and save it into a variable called "element"

- assert that element's method attribute equals "post"

- assert that element's action attribute equals the base_url + "/login"

- open /logout


### R1.6 : Email and password cannot be empty:


#### R1.6.1 : Email cannot be empty:

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's password into element #password

- Enter “ ” into element #email

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout


#### R1.6.2 : Password cannot be empty:

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

 - Open /logout

- Open /login

- Enter “” into element #password

- Enter TEST_USER's email into element #email

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout


### R1.7 : Email has to follow addr-specs defined in RFC 5322  

#### positive case is covered in R1.9

#### R1.7.1 : Email has to follow addr-specs defined in RFC 5322  Negative 1

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's password into element #password

- Enter ".test@gmail.com" into element #email

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout


#### R1.7.2 : Email has to follow addr-specs defined in RFC 5322  Negative 2

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's password into element #password

- Enter "testgmail.com" into element #email

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout



#### R1.7.3 : Email has to follow addr-specs defined in RFC 5322  Negative 3

Mocking:

- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's password into element #password

- Enter "test@gmail" into element #email

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout


### R1.8 : Password has to meet required complexity: minimum length 6, at least one upper case, at least one lower case and at least one special character 

#### R1.8.1 Password must be at least 6 characters: 
Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's email into element #email

- Enter “A#cde” into element #password

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout


#### R1.8.2 Password must contains one lower case :

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's email into element #email

- Enter “A#CDEF” into element #password

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout

 
#### R1.8.3 Password must contains one special character: 

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's email into element #email

- Enter “Abcdef” into element #password

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout

#### R1.8.4 Password must contains one upper case: 

Mocking:
- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER's email into element #email

- Enter “a#cdef” into element #password

- Click element input[type = “submit”]

- Validate that the #message element is equal to “email/password format is incorrect.”

- open /logout



### R1.9: If email/password are correct, redirect to / 

Mocking:

- Mock backend.get_user to return a TEST_USER instance

Actions:

- Open /logout

- Open /login

- Enter TEST_USER’s email into element #email

- Enter TEST_USER’s password into element #password

- Click element input[type = “submit”]

- Validate that current page contains #welcome element

- open /logout

### R1.10: If email/password are not correct, redirect to /login 


Mocking:

- Mock backend.get_user to return a TEST_USER instance


Actions:

- Open /logout

- Open /login

- Enter TEST_USER’s email into element #email

- Enter “W$ongpassword” into element #password

- Click element input[type = “submit”]

- Validate that current page is “/login”

- Validate that the #message element is equal to “email/password combination is incorrect.”

- open /logout
