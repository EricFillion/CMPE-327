### Register 

**Description**: Allows a user to create an account using an email and password, so long that they are both valid. 

#### **R2.1 If the user has logged in, redirect back to the user profile page /**

Mocking:
- Mock backend.get_user to return a test_user instance

Actions:
- Open /logout 
- Open /login
- Enter test_user’s email into element #email
- Enter test_user’s password into element #password
- Click element input[type = “submit”]
- Open /register page 
- Validate that the current page has been redirected to /
- Open /logout

#### **R2.2 R2.3 otherwise, show the user registration page the registration page shows a registration form requesting: email, user name, password, password2**
Mocking:
- N/A

Actions:

- Open /logout
- Open /register
- Validate whether have #email , #password, #password2, #name element

#### ** R2.4 Email, password, password2 all have to satisfy the same required as defined in R1 **

##### **R2.4.1 check email not empty validation**
- Open /logout

- Open /register

- Enter “J12345678a!” into element #password

- Enter “J12345678a!” into element #password2

- Enter “” into element #email

- Enter "aaaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “Email format is incorrect"

##### **R2.4.2 check password not empty valdiation**
- Open /logout

- Open /register

- Enter “” into element #password

- Enter “” into element #password2

- Enter “a@qq.com” into element #email

- Enter "aaaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “Password format is incorrect”


##### **R2.4.3 Email has to follow addr-spec defined in RFC 5322**
- Open /logout

- Open /register

- Enter “J1230a!” into element #password

- Enter “J1230a!” into element #password2

- Enter “a” into element #email

- Enter "aaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “email format is incorrect ”

##### **R2.4.4 Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character**

###### **R2.4.4.1 Password has minimum length 6**
- Open /logout

- Open /register

- Enter “12Aa!” into element #password

- Enter “12Aa!” into element #password2

- Enter “a@qq.com” into element #email

- Enter "aaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “password format is incorrect"

###### **R2.4.4.2 Password has at least one upper case**
- Open /logout

- Open /register

- Enter “123456!a” into element #password

- Enter “123456!a” into element #password2

- Enter “a@qq.com” into element #email

- Enter "aaaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “password format is incorrect ”

###### **R2.4.4.3 Password has at least one lower case**
- Open /logout

- Open /register

- Enter “A123456!” into element #password

- Enter “A123456!” into element #password2

- Enter “a@qq.com” into element #email

- Enter "aaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “password format is incorrect”

###### **R2.4.4.4 Password has  at least one special letter**
- Open /logout

- Open /register

- Enter “A12345a” into element #password

- Enter “A12345a” into element #password2

- Enter “a” into element #email

- Enter "a" into element #name

- Click element input[type = “submit”]


- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “password format is incorrect ”

#### **R2.5 User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character**

##### **R2.5.1 User name has to be non-empty**
- Open /logout

- Open /register

- Enter “J1234a!” into element #password

- Enter “J1234a!” into element #password2

- Enter “a@qq.com” into element #email

- Enter "" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “username format is incorrect.”

##### **R2.5.2 User name has to be alphanumeric-only**
- Open /logout

- Open /register

- Enter “A1230o!” into element #password

- Enter “A1230o!” into element #password2

- Enter “2@qq.com” into element #email

- Enter "22" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “username format is incorrect.”

##### **R2.5.3 User name has to be space allowed only if it is not the first or the last character**
- Open /logout

- Open /register

- Enter “!1234Aa” into element #password

- Enter “!1234Aa” into element #password2

- Enter “2@qq.com” into element #email

- Enter " aaaa " into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “username format is incorrect.”


#### R2.6 If the email already exists, show message 'this email has been ALREADY used'

Mocking:
- Mock backend.get_user to return a test_user instance
```python
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```
Actions:
- Open /logout

- Open /register

- Enter “1222222!aA” into element #password

- Enter “1222222!aA” into element #password2

- Enter “test_frontend@test.com” into element #email

- Enter "test_frontend" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “'this email has been ALREADY used”

#### **R2.7 User name has to be longer than 2 characters and less than 20 characters**

##### **R2.7.1 User name has to be longer than 2 characters** 
- Open /logout

- Open /register

- Enter “1111Aa!” into element #password

- Enter “1111Aa!” into element #password2

- Enter “2@qq.com” into element #email

- Enter "a" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “username format is incorrect.”

##### **R2.7.2 User name has to be less than 20 characters**
- Open /logout

- Open /register

- Enter “1111Aa!” into element #password

- Enter “1111Aa!” into element #password2

- Enter “2@qq.com” into element #email

- Enter "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to “username format is incorrect.”


#### **R2.8 check password repeat validation**
- Open /logout

- Open /register

- Enter “1Ja!111111111” into element #password

- Enter “2J1!sassaaaa” into element #password2

- Enter “aaaa@gmail.com” into element #email

- Enter "aaaa" into element #name

- Click element input[type = “submit”]

- Validate existence of element #password, #password2, #name, #email

- Validate that the #message element is equal to "password format is incorrect”


#### R2.9 The registration form can be submitted as a POST request to the current URL (/register)
- Open /logout

- Open /register

- Validate the existence of a form with attribute method equal to 'post'

- Validate the existence of a form with attribute action equal to '/register'

- Create a post request to current url (/register) with data containing testuser's email, name and password.

- Validate that the request returns a status code of 200


#### **R2. 10 If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page**
- Open /logout

- Open /register

- Enter testuser's email into element #email

- Enter testuser's name into element #name

- Enter testuser's password into element #password

- Enter testuser's password into element #password2

- Click element input[type = “submit”]

- Validate that the current page has been redirected to /login







