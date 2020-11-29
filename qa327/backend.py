from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import update
from datetime import datetime

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

def update_ticket(name, quantity, price, expiryDate):
    """
    Update the quantity, price and expiry date of a ticket of a given name
    :param name: the name of the ticket to be updated
    :param quantity: the new quantity for the ticket
    :param price: the new price for the ticket
    :param expiryDate: the new expiry date of the ticket
    """
    db.session.query(Ticket)\
       .filter(Ticket.name==name)\
       .update({Ticket.quantity: quantity, Ticket.price: float(price)*100, Ticket.expiry: datetime.strptime(expiryDate, '%Y-%m-%d').date()})
    db.session.commit()
  