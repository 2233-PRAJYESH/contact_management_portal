from flask import Flask, request, render_template, redirect, session
from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash
from flask import flash
import re

app = Flask(__name__)
app.secret_key = "secret123"  # for sessions


# Home
@app.route("/")
def home():
    return redirect("/login")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")



        # Empty field validation
        if not name or not email or not password:

          flash("All fields are required")

          return redirect("/register")


        # email regx validation 
          # Email validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):

            flash("Invalid email format")

            return redirect("/register")
        
        # Password validation
        if len(password) < 6:

           flash("Password must be at least 6 characters")

           return redirect("/register")






        # Check duplicate email
        cursor.execute(
            "SELECT * FROM users WHERE email=%s" , 
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:

            flash("Email already registered")

            return redirect ("/register")

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Insert user into database
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, hashed_password)
        )

        db.commit()

        return redirect("/login")

    return render_template("register.html")





# login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))

        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):
            session["user_id"] = user["id"]

            return redirect("/dashboard")
        
        flash("Invalid email or password")

    return render_template("login.html")


# Dashboard (contacts)


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Add contact
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")

        cursor.execute(
            "INSERT INTO contacts (user_id, name, phone) VALUES (%s, %s, %s)",
            (session["user_id"], name, phone),
        )
        db.commit()

    # Get contacts
    cursor.execute("SELECT * FROM contacts WHERE user_id=%s", (session["user_id"],))

    contacts = cursor.fetchall()

    return render_template("dashboard.html", contacts=contacts)


# Logout


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


# Run app

if __name__ == "__main__":
    app.run(debug=True)
