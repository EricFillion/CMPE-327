from flask import render_template, request, session, redirect
from qa327 import app
import qa327.backend as bn
from qa327.validate_login_format import validate_login_format,validate_name_format
from qa327.ticket_utils import validate_ticket_name_format,validate_ticket_quantity,calculate_price_ticket
from datetime import date

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

@app.route('/buy', methods=['POST'])
def buy():
    name = request.form.get('buyform_input_name')
    quantity = request.form.get('buyform_input_quantity')

    error_message = ""
    # validate ticket name
    if not validate_ticket_name_format(name):
        error_message="The name of the ticket is invalid."
        return render_template('index.html',buy_message=error_message)
    # validate ticket quantity
    if not validate_ticket_quantity(int(quantity)):
        error_message="The quantity of ticket is invalid."
        return render_template('index.html',buy_message=error_message)
    # get all ticket
    tickets = bn.get_all_tickets()
    valid_tickets = list(filter(lambda x: x.expiry >= date.today(), tickets))
    current_ticket = filter(lambda x:x.name==name,valid_tickets)
    # validate existence of current ticket to buy
    if not current_ticket:
        error_message="The ticket does not exist."
        return render_template('index.html',buy_message=error_message)
    # validate the number ticket to buy
    if quantity > current_ticket.quantity:
        error_message="The quantity is less than the quantity requested."
        return render_template('index.html',buy_message=error_message)
    # get current user
    email = session['logged_in']
    user = bn.get_user(email)
    total_price=calculate_price_ticket(quantity,current_ticket.price)
    # validate balance and ticket price
    if total_price > user.balance:
        error_message="Must have more balance than the ticket price."
        return render_template('index.html',buy_message=error_message)
    if not bn.buy_ticket(email,total_price):
        error_message="Cannot buy ticket"
        return render_template('index.html',buy_message=error_message)
    return render_template('index.html')
        