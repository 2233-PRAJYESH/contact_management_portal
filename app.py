from flask import Flask

from flask_wtf.csrf import CSRFProtect

from routes.auth_routes import auth
from routes.dashboard_routes import dashboard

app = Flask(__name__)

app.secret_key = "secret123"

csrf = CSRFProtect(app)

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(dashboard)


if __name__ == "__main__":

    app.run(debug=True)