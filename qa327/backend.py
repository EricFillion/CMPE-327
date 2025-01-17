from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime,date
from sqlalchemy.exc import IntegrityError

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=5000)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_all_tickets():
    """
    Query all tickets from the database
    :return: a list containing all tickets in the database
    """
    return list(Ticket.query)

def buy_ticket(email,price,name,quantity):
    """
    Update user balance
    :param email: email of user
    :param price: price of ticket
    :param name: name of ticket
    :param quantity: quantity to buy
    """
    user=User.query.filter_by(email=email).first()
    user.balance=int(float(user.balance)-float(price))
    ticket=Ticket.query.filter_by(name=name).first()
    ticket.quantity-=int(quantity)
    try:
        db.session.commit()
    except IntegrityError as e:
        return "Cannot buy tickets"
        raise e
    return False

def get_ticket(name):
    """
    get a ticket 
    :param name: ticket name
    """
    tickets =get_all_tickets()
    valid_tickets = list(filter(lambda x: x.expiry >= date.today(), tickets))
    return list(filter(lambda x:x.name==name,valid_tickets))
    


def get_ticket_by_name(name):
    """
    Query the database to get a ticket with a given name
    :param name: the name of the ticket to get
    :return: a Ticket object, or None if the ticket was not in the database
    """
    matching_ticket = Ticket.query.filter(Ticket.name==name).first()
    return matching_ticket

def update_ticket(name, quantity, price, expiryDate):
    """
    Update the quantity, price and expiry date of a ticket of a given name
    :param name: the name of the ticket to be updated
    :param quantity: the new quantity for the ticket
    :param price: the new price for the ticket
    :param expiryDate: the new expiry date of the ticket
    :return: a string describing the error that occurred, or False for no error
    """
    # Get ticket
    ticket = get_ticket_by_name(name)
    if ticket is None:
        return "The ticket of the given name must exist."
    # Update ticket data
    ticket.quantity = quantity
    ticket.price = float(price)*100
    ticket.expiry = datetime.strptime(expiryDate, '%Y%m%d').date()
    # Commit ticket to database
    db.session.commit()
  

def sell_ticket(user, name, quantity, price, expiryDate):
    """
    Update the quantity, price and expiry date of a ticket of a given name
    :param user: the user who is selling the ticket
    :param name: the name of the ticket to be updated
    :param quantity: the new quantity for the ticket
    :param price: the new price for the ticket
    :param expiryDate: the new expiry date of the ticket
    :return: a string describing the error that occurred, or False for no error
    """
    if not isinstance(user, User):
        return "Internal Error: 'user' must be of type 'User'"
    if not isinstance(name, str):
        return "Internal Error: 'name' must be of type 'str'"
    if not isinstance(quantity, int):
        return "Internal Error: 'quantity' must be of type 'int'"
    if not isinstance(price, float):
        return "Internal Error: 'price' must be of type 'float'"
    if not isinstance(expiryDate, date):
        return "Internal Error: 'expiryDate' must be of type 'date'"
    if User.query.filter_by(id=user.id).first() is None:
        return "Internal Error: user does not exist in database"
    new_ticket = Ticket()
    new_ticket.owner = user
    new_ticket.name = name
    new_ticket.quantity = quantity
    new_ticket.price = int(price*100)
    new_ticket.expiry = expiryDate
    db.session.add(new_ticket)
    try:
        db.session.commit()
    except IntegrityError as e:
        db.session.rollback()
        # We got an integrity error. Check if it was due to
        # UNIQUE constraint being violated.
        # I can't find a better way to do this unfortunately.
        args_str = ' '.join(e.args)
        if 'UNIQUE constraint failed' in args_str:
            return 'A ticket with that name already exists.'
        raise e
    return False
