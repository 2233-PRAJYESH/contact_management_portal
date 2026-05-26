from repositories.contact_repository import (
    create_contact,
    get_user_contacts
)

from repositories.contact_repository import (
    delete_contact
)

def add_contact(user_id, name, phone):

    if not name or not phone:

        return "All fields are required"

    # Phone number must contain only digits
    if not phone.isdigit():

        return "Phone number must contain only digits"

    # Phone number length must be 10 digits 
    if len(phone) != 10:

        return "Phone number must be  10 digits only"

    create_contact(user_id, name, phone)

    return "success"


def fetch_contacts(user_id):

    return get_user_contacts(user_id)


def remove_contact(contact_id, user_id):

    delete_contact(contact_id, user_id)

    return "success"