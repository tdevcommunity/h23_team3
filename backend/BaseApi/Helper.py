import re

def isEmailOrPhone(chaine):
    """
    Check if the string is an email or a phone number.
    1 - If it is an email, it returns "C'est une adresse e-mail."
    2 - If it is a phone number, it returns "C'est un numéro de téléphone."
    0 - If it is neither, it returns "Ce n'est ni une adresse e-mail ni un numéro de téléphone
    """
    pattern_email = r'^[\w\.-]+@[\w\.-]+$'
    pattern_telephone = r'^[0-9]{10}$'

    if re.match(pattern_email, chaine):
        return 1

    elif re.match(pattern_telephone, chaine):
        return 2

    else:
        return 0