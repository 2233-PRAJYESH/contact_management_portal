from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from repositories.auth_repository import (
    get_user_by_email,
    create_user
)

from utils.validators import (
    is_valid_email,
    is_strong_password
)


def register_user(name, email, password):

    if not name or not email or not password:
        return "All fields are required"

    if not is_valid_email(email):
        return "Invalid email format"

    if not is_strong_password(password):
        return "Password must be at least 6 characters"

    existing_user = get_user_by_email(email)

    if existing_user:
        return "Email already exists"

    hashed_password = generate_password_hash(password)

    create_user(name, email, hashed_password)

    return "success"


def login_user(email, password):

    user = get_user_by_email(email)

    if user and check_password_hash(user["password"], password):

        return user

    return None