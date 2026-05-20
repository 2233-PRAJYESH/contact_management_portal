from flask import Flask

from flask_wtf.csrf import CSRFProtect

from routes.auth_routes import auth
from routes.dashboard_routes import dashboard

from routes.admin_routes import admin

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY") #Should move in to env 

csrf = CSRFProtect(app)

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(admin)


if __name__ == "__main__":

    app.run(debug=True)