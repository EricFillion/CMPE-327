from flask import render_template, request, session, redirect, flash
from qa327 import app
import qa327.backend as bn
from qa327.validate_login_format import validate_login_format,validate_name_format
from datetime import date
import qa327.validate_ticket_format as validate_ticket_format
"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""



@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    if 'logged_in' in session:
        return redirect('/',code=303)
    else:
        return render_template('register.html', message='')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    error_message = None


    if password != password2:
        error_message = "The passwords do not match"

    elif not validate_login_format(email, password):
        error_message = "email/password format is incorrect."
    elif not validate_name_format(name) :
        error_message="username format is incorrect."
    else:
        user = bn.get_user(email)
        if user:
            error_message = "this email has been ALREADY used"
        elif not bn.register_user(email, name, password, password2):
            error_message = "Failed to store user info."
    # if there is any error messages when registering new user
    # at the backend, go back to the register page.
    if error_message:
        return render_template('register.html', message=error_message)
    else:
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html', message='Please login')


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    error_message = ""

    if not validate_login_format(email, password):
        error_message = "email/password format is incorrect."
    else:
        user = bn.login_user(email, password)
        if user:
            session['logged_in'] = user.email
            """
            Session is an object that contains sharing information 
            between browser and the end server. Typically it is encrypted 
            and stored in the browser cookies. They will be past 
            along between every request the browser made to this services.
    
            Here we store the user object into the session, so we can tell
            if the client has already login in the following sessions.
    
            """
            # success! go back to the home page
            # code 303 is to force a 'GET' request
            return redirect('/', code=303)
        else:
            error_message = "email/password combination incorrect"
    return render_template('login.html', message=error_message)

@app.route('/update', methods=['POST'])
def update_post():
    """ 
    Called when a user clicks update on the update form. If the given inputs match 
    R5 requirements the quantity, price and expiry date of a ticket of the given name
    are update, else an error message is shown. 
    """
    name = request.form.get('name')
    quantity = request.form.get('quantity')
    price = request.form.get('price')
    expiry = request.form.get('expiry')
    formatError = validate_ticket_format.check_for_update_ticket_format_error(name, quantity, price, expiry)
    if(not formatError):
        bn.update_ticket(name, quantity, price, expiry)
        return redirect('/')
    else:
        flash(formatError)
        return redirect('/')

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
            else:
                # If user does not exist, reset logged_in
                del session['logged_in']
        # if we haven't returned a value yet (invalid token or not logged in),
        # redirect to the login page
        return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    # The authentication functionality above satisfies R3.1
    
    # Get all tickets from backend
    tickets = bn.get_all_tickets()
    # We need to filter out expired tickets as per R3.5.2-3.5.3
    valid_tickets = list(filter(lambda x: x.expiry >= date.today(), tickets))
    return render_template('index.html', user=user, tickets=valid_tickets)

#Custom 404 not found page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# This shows 404 error page instead of a 405 method not allowed error when a get or other request is 
# made to a route that should only have a post request.
# This is to meet R8 (For any other requests except the ones above, the system should return a 404 error)
@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('404.html'), 404