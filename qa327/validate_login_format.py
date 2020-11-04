import re
from email_validator import validate_email, EmailNotValidError

"""
This file contains one public function, validate_login_format, that
determines if the email and password submitted from the login and
register fields conform to the proper guidelines.

It also contains three private private functions to aid with
validating the email and password.
"""


def validate_login_format(email, password):
    """
    Returns True if the email and password strings conform to the formatting guidelines.
    Otherwise, returns False.

    :param email: a string for the user's email address
    :param password: a string for the user's password
    :return: True if valid, else False
    """

    if not __validate_email_format(email):
        return False

    elif not __validate_password_format(password):
        return False

    return True


def __validate_email_format(email):
    """
    Returns True if the email conforms to the following guidelines.
    1. Must not be blank
    2. Must follow RFC 5322 guidelines

    Uses the "email_validator" library to ensure the email follows
    RFC 5322 guidelines.

    Otherwise returns False
    :param email: a string for the user's email address
    :return: True if valid, else False
    """
    # Email cannot be blank
    if email == "":
        return False

    # Using the email_validator library to ensure the email
    # follows proper RFC 5322 guidelines
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        return False


def __validate_password_format(password):
    """
    Returns True if the email conforms to the following guidelines.
    1. Must not be blank
    2. Length must be greater than or equal to 6
    3. Must have one upper case letter
    4. Must have one lower case letter
    5. Must contain one special character

    Otherwise returns False
    :param password: a string for the user's password
    :return: True if valid, else False
    """

    # Password cannot be blank
    if password == "":
        return False
    # Password must be at least 6 characters
    elif len(password) < 6:
        return False
    # Password must contain one upper case
    elif password.islower():
        return False
    # Password must contain one lower case
    elif password.isupper():
        return False
    # Password contains one special character
    elif not __contains_special_char(password):
        return False
    else:
        return True


def __contains_special_char(password):
    """
    Checks of the password contains a special character, such as "&" or "@".
    Returns true if the password contains a special character, otherwise returns False.

    :param password: a string for the user's password
    :return: True if valid, else False
    """
    # Special characters for a password are from the Open Web Application Security Project
    # Source: https://owasp.org/www-community/password-special-characters
    special_chars = [" ", "!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

    res = any(ele in password for ele in special_chars)
    return res


def validate_name_fail(name):
    """
    Returns True if the name strings conform to the formatting guidelines.
    Otherwise, returns False.

    :param name: a string for the user's name
   
    :return: True if valid, else False
    """
    # first or last letter cannot be space , can have space in middle, not empty name, and alphanumeric-only 
    if not re.match("^[a-zA-Z0-9][a-zA-Z0-9_ ]+[a-zA-Z0-9]$", name):
        return True
    # name must longer than 2 less than 20 characters
    elif len(name)<2 or len(name) > 20 :
        return True
    
    else:
        return False

