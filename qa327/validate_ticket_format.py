import datetime

def check_for_ticket_name_error(ticket_name):
    """
    Returns any error message if the ticket name is not alphanumeric, if there is an 
    invalid space in the name or the name is too long for a ticket name. If
    there is no errors it returns false. 

    :param ticket_name: a string for the ticket's name
    :return: false if no error, else returns the error as a string message
    """
    if not ticket_name.replace(' ', '').isalnum():    
        return "The name of the ticket has to be alphanumeric only"
    if (ticket_name[0] == ' ') or (ticket_name[-1] == ' '):
        return "The name of the ticket is only allowed spaces if it is not the first or last character" 
    if len(ticket_name) > 60:
        return "The name of the ticket should be no longer than 60 characters"
    return False


def check_for_ticket_quantity_error(quantity):
    """
    Returns any error message if the ticket's quantity is not between 10 and 100 else if
    there is no errors it returns false.

    :param quantity: the ticket's quantity as a string
    :return: false if no error, else returns the error as a string message
    """
    if int(quantity) < 10 or int(quantity) > 100:   
        return "The quantity of the ticket must be between 10 and 100"
    return False
    
def check_for_ticket_price_error(price):
    """
    Returns any error message if the ticket's price is not between 0 and 100 else if
    there is no errors it returns false.

    :param price: the ticket's price as a string
    :return: false if no error, else returns the error as a string message
    """
    if float(price) < 0 or float(price) > 100:   
        return "The price of the ticket must be between 0 and 100"
    return False


def check_for_ticket_date_error(date):
    """
    Returns any error message if the date is not in the format YYYYMMDD else if
    there is no errors it returns false.

    :param price: the ticket's price as a string
    :return: false if no error, else returns the error as a string message
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return "Date must be given in the format YYYYMMDD (e.g. 20200901)"
    return False

def check_for_update_ticket_format_error(name, quantity, price, date):
    """
    Checks the tickets name, quantity, price and date to ensure they are the correct format.
    If they are not in the correct format an error message is returned, else false is returned 
    indicating that there are no errors

    :param name: the name of the ticket to be updated
    :param quantity: the new quantity for the ticket
    :param price: the new price for the ticket
    :param expiryDate: the new expiry date of the ticket
    :return: false if no error, else returns the error as a string message
    """
    nameError = check_for_ticket_name_error(name)
    quantityError = check_for_ticket_quantity_error(quantity)
    priceError = check_for_ticket_price_error(price) 
    dateError = check_for_ticket_date_error(date)
    if(nameError):
        return nameError
    if(quantityError):
        return quantityError
    if(priceError):
        return priceError
    if(dateError):
        return dateError
    return False