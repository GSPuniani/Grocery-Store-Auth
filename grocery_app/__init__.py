from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from grocery_app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

# Set up flask_login

# Create a flask_login.LoginManager instance
login_manager = LoginManager()
# Set the login view to auth.login
login_manager.login_view = 'auth.login'
# Initialize it with the app
login_manager.init_app(app)

from .models import User

# Look up a user by id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Initialize an instance of flask_bcrypt.Bcrypt with the app
bcrypt = Bcrypt(app)

from grocery_app.routes import main, auth

app.register_blueprint(main)

# Register new blueprint for auth routes
app.register_blueprint(auth)

with app.app_context():
    db.create_all()
