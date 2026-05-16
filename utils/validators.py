import re


def is_valid_email(email):

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(email_pattern, email)


def is_strong_password(password):

    return len(password) >= 6