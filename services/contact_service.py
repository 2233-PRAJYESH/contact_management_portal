from repositories.contact_repository import (
    create_contact,
    get_user_contacts
)


def add_contact(user_id, name, phone):

    if not name or not phone:
        return "All fields are required"

    create_contact(user_id, name, phone)

    return "success"


def fetch_contacts(user_id):

    return get_user_contacts(user_id)