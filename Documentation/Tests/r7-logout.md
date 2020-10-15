### Logout

**Description**: A user can logout.


#### R7.1 Logout will invalid the current session and redirect to the login page. After logout, the user shouldn't be able to access restricted pages.

Mocking:
- Mock backend.get_user to return a test_user instance

Actions:

- Open /login

- Enter test_user’s email into element #email

- Enter test_user’s password into element #password

- Click element input[type = “submit”]

- Open /logout

- check current session

- check that the current page is /login

- validate whether the page has elements #email, #password

- open / again

- check that the current page is /login

- validate page whether have element #email, #password