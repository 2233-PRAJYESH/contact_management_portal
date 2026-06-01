from flask import Flask

from flask_wtf.csrf import CSRFProtect

import os

from dotenv import load_dotenv

from oauth_config import oauth, google


load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

csrf = CSRFProtect(app)

# Initialize OAuth
oauth.init_app(app)

# Google credentials from the cloud console
google.client_id = os.getenv(
    "GOOGLE_CLIENT_ID"
)

google.client_secret = os.getenv(
    "GOOGLE_CLIENT_SECRET"
)

# import routes & O AUTH setup 
from routes.auth_routes import auth
from routes.dashboard_routes import dashboard
from routes.admin_routes import admin

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(admin)


if __name__ == "__main__":

    app.run(debug=True)