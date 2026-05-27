from repositories.admin_repository import (
    delete_user,
    delete_user_contacts
)


def remove_user(user_id):

    # Delete contacts first
    delete_user_contacts(user_id)

    # Delete user
    delete_user(user_id)

    return "success"