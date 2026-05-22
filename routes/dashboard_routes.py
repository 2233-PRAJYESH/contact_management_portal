from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    session,
    flash
)

from services.contact_service import (
    add_contact,
    fetch_contacts,
    remove_contact
)

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard", methods=["GET", "POST"])
def dashboard_page():

    if not session.get("user_id"):

        return redirect("/login")

    # Add contact
    if request.method == "POST":

        name = request.form.get("name")
        phone = request.form.get("phone")

        result = add_contact(
            session["user_id"],
            name,
            phone
        )

        # Validation failed
        if result != "success":

            flash(result)

            return redirect("/dashboard")

        flash("Contact added successfully")

        return redirect("/dashboard")

    contacts = fetch_contacts(
        session["user_id"]
    )

    return render_template(
        "dashboard.html",
        contacts=contacts
    )
    
@dashboard.route("/delete-contact/<int:contact_id>")
def delete_contact_route(contact_id):

    if not session.get("user_id"):

        return redirect("/login")

    remove_contact(
        contact_id,
        session["user_id"]
    )

    flash("Contact deleted successfully")

    return redirect("/dashboard")