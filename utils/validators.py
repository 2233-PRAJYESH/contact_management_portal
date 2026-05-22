import re


def is_valid_email(email):

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(email_pattern, email)







def is_strong_password(password):

    # Minimum 8 chars
    if len(password) < 8:

        return False

    # Uppercase letter
    if not re.search(r"[A-Z]", password):

        return False

    # Lowercase letter
    if not re.search(r"[a-z]", password):

        return False

    # Number
    if not re.search(r"[0-9]", password):

        return False

    # Special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):

        return False

    return True