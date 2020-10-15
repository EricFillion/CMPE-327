### Logout

Mocking:
- Mock backend.get_user to return a test_user instance

Actions:

- Open /login

- Enter test_user’s email into element #email

- Enter test_user’s password into element #password

- Click element input[type = “submit”]

- Open /logout

- check that the current page is /login

- validate whether the page has elements #email, #password

- open / again

- check that the current page is /login

- validate page whether have element #email, #password