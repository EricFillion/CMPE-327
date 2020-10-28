from email_validator import validate_email, EmailNotValidError
import re

def validate_login_format(email, password):
    # todo doc string

    if not __validate_email_format(email):
        return False

    elif not __validate_password_format(password):
        return False

    return True

def __validate_email_format(email):
    # todo doc string

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
    # todo doc string
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
    elif not __contains_special_char(password):

        return False
    return True

def __contains_special_char(password):
    # todo doc string
    # Use regex to remove all chars that letters or numbers
    special_string = re.findall('[^A-Za-z0-9]', password)
    # Return True if there is at least one special character
    return len(special_string) > 0
