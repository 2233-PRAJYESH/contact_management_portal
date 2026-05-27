from db import get_db


# Delete user contacts
def delete_user_contacts(user_id):

    db = get_db()

    cursor = db.cursor()

    cursor.execute(
        """
        DELETE FROM contacts
        WHERE user_id=%s
        """,
        (user_id,)
    )

    db.commit()


# Delete user
def delete_user(user_id):

    db = get_db()

    cursor = db.cursor()

    cursor.execute(
        """
        DELETE FROM users
        WHERE id=%s
        """,
        (user_id,)
    )

    db.commit()