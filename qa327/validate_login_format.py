from email_validator import validate_email, EmailNotValidError

def validate_login_format(email, password):

    # email and password cannot be blank
    if password == "" or email == "":
        return False

    elif not __validate_email_format(email):
        return False

    return True

def __validate_email_format(email):

    try:
        valid = validate_email(email)
        return True
    except EmailNotValidError as e:
        return False



