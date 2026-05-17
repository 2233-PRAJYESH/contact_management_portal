from flask import (
    Flask,
    request,
    render_template,
    redirect,
    session,
    flash
)

from flask_wtf.csrf import CSRFProtect

from db import get_db

from services.auth_service import (
    register_user,
    login_user
)

from services.contact_service import (
    add_contact,
    fetch_contacts
)
app = Flask(__name__)

app.secret_key = "secret123"

csrf = CSRFProtect(app)


# Home
@app.route("/")
def home():

    return redirect("/login")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        result = register_user(
            name,
            email,
            password
        )

        if result != "success":

            flash(result)

            return redirect("/register")

        flash("Registration successful")

        return redirect("/login")

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = login_user(email, password)

        if user:

            session["user_id"] = user["id"]

            return redirect("/dashboard")

        flash("Invalid email or password")

    return render_template("login.html")



# Dashboard
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():

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

# Logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# Run app
if __name__ == "__main__":

    app.run(debug=True)