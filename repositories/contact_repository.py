from db import get_db


def create_contact(user_id, name, phone):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO contacts (user_id, name, phone) VALUES (%s, %s, %s)",
        (user_id, name, phone)
    )

    db.commit()


def get_user_contacts(user_id):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM contacts WHERE user_id=%s",
        (user_id,)
    )

    return cursor.fetchall()

def delete_contact(contact_id, user_id):

    db = get_db()

    cursor = db.cursor()

    cursor.execute(
        """
        DELETE FROM contacts
        WHERE id=%s AND user_id=%s
        """,
        (contact_id, user_id)
    )

    db.commit()