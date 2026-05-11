from flask import Flask, request, render_template, redirect, session
from db import get_db

app = Flask(__name__)
app.secret_key = "secret123"   # for sessions

# Home
@app.route('/')
def home():
    return redirect('/login')

# Register 

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        db.commit()

        return redirect('/login')

    return render_template('register.html')

# login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cursor.fetchone()

        if user:
            session['user_id'] = user['id']
            return redirect('/dashboard')

    return render_template('login.html')

# Dashboard (contacts)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Add contact
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')

        cursor.execute(
            "INSERT INTO contacts (user_id, name, phone) VALUES (%s, %s, %s)",
            (session['user_id'], name, phone)
        )
        db.commit()

    # Get contacts
    cursor.execute(
        "SELECT * FROM contacts WHERE user_id=%s",
        (session['user_id'],)
    )

    contacts = cursor.fetchall()

    return render_template('dashboard.html', contacts=contacts)


#Logout

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

# Run app 

if __name__ == "__main__":
    app.run(debug=True)