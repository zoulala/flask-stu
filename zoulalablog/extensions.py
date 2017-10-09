

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_openid import OpenID
from flask_principal import Principal,Permission,RoleNeed
from flask_admin import Admin

# Create the Flask-Bcrypt's instance, a hash algorithm for password
bcrypt = Bcrypt()

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    """Load the user's info."""

    from models import User
    return User.query.filter_by(id=user_id).first()