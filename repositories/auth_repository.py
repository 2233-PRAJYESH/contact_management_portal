from db import get_db


def get_user_by_email(email):

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE email=%s",
        (email,)
    )

    return cursor.fetchone()


def create_user(name, email, password):

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )

    db.commit()
    
def create_google_user(name, email):

    db = get_db()

    cursor = db.cursor()

    cursor.execute(
        """
        INSERT INTO users
        (name, email, password, role)
        VALUES (%s, %s, %s, %s)
        """,
        (
            name,
            email,
            "google-oauth-user",
            "user"
        )
    )

    db.commit()