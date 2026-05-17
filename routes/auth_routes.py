from flask import (
    Blueprint,     #Blueprint = mini Flask app,Used to organize routes.Instead of:one huge route file you create:modular route groups
    request,
    render_template,
    redirect,
    flash,
    session
)

from services.auth_service import (
    register_user,
    login_user
)

auth = Blueprint("auth", __name__)


# Home
@auth.route("/")
def home():

    return redirect("/login")


# Register
@auth.route("/register", methods=["GET", "POST"])
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
@auth.route("/login", methods=["GET", "POST"])
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


# Logout
@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/login")