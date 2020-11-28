import re

def validate_ticket_name_format(ticket_name):
    """
    
    """
    if not re.match("^[a-zA-Z0-9][a-zA-Z0-9_ ]+[a-zA-Z0-9]$", ticket_name):
        return False
    elif len(ticket_name)>60:
        return False
    return True

def validate_ticket_quantity(quantity):
    return quantity>0 and quantity<100


def calculate_price_ticket(quantity,price):
    return 1.4 * (quantity * price)