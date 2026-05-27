

from flask import url_for

from flask import (
    Blueprint,
    request,
    render_template,
    redirect,
    flash,
    session
)

from services.auth_service import (
    register_user,
    login_user,
    google_login_user
)

from utils.logger import log_action
from oauth_config import google



auth = Blueprint("auth", __name__)

#Google login OAuth 
@auth.route("/google-login")
def google_login():

    redirect_uri = url_for(
        "auth.google_callback",
        _external=True
    )

    return google.authorize_redirect(
        redirect_uri
    )

# Callback route 
@auth.route("/google/callback")
def google_callback():

    token = google.authorize_access_token()

    user_info = token["userinfo"]

    email = user_info["email"]

    name = user_info["name"]

    # Create or fetch DB user
    user = google_login_user(
        name,
        email
    )

    # Create proper login session
    session["user_id"] = user["id"]

    session["email"] = user["email"]

    session["role"] = user["role"]

    flash("Google login successful")

    return redirect("/dashboard")
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
            session["role"] = user["role"]
            session["email"] = user["email"]

            # Audit log
            log_action(
                f"User {user['email']} logged in"
            )

            # Admin redirect
            if user["role"] == "admin":

                return redirect("/admin")

            # Normal user redirect
            return redirect("/dashboard")

        flash("Invalid email or password")

    return render_template("login.html")




# Logout
@auth.route("/logout")
def logout():

    log_action(
        f"User {session.get('email')} logged out"
    )

    session.clear()

    return redirect("/login")