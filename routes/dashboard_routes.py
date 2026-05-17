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
    fetch_contacts
)

dashboard = Blueprint("dashboard", __name__)


@dashboard.route("/dashboard", methods=["GET", "POST"])
def dashboard_page():

    if "user_id" not in session:

        return redirect("/login")

    if request.method == "POST":

        name = request.form.get("name")
        phone = request.form.get("phone")

        result = add_contact(
            session["user_id"],
            name,
            phone
        )

        if result != "success":

            flash(result)

    contacts = fetch_contacts(
        session["user_id"]
    )

    return render_template(
        "dashboard.html",
        contacts=contacts
    )