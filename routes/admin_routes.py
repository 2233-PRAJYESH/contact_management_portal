from flask import (
    Blueprint,
    session,
    redirect,
    render_template,
    flash
)
from services.admin_service import remove_user



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
    
@admin.route("/delete-user/<int:user_id>")
def delete_user_route(user_id):

    # Only admin allowed
    if session.get("role") != "admin":

        return redirect("/login")

    remove_user(user_id)

    flash("User deleted successfully")

    return redirect("/admin")