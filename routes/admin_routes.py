from flask import (
    Blueprint,
    session,
    redirect,
    render_template
)

from db import get_db

admin = Blueprint("admin", __name__)


@admin.route("/admin")
def admin_dashboard():

    # User not logged in
    if not session.get("user_id"):

        return redirect("/login")

    # User is not admin
    if session.get("role") != "admin":

        return redirect("/dashboard")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Get all users
    cursor.execute(
        "SELECT id, name, email, role FROM users"
    )

    users = cursor.fetchall()

    # Get all contacts
    cursor.execute(
        """
        SELECT contacts.name,
               contacts.phone,
               users.email
        FROM contacts
        JOIN users
        ON contacts.user_id = users.id
        """
    )

    contacts = cursor.fetchall()

    return render_template(
        "admin_dashboard.html",
        users=users,
        contacts=contacts
    )