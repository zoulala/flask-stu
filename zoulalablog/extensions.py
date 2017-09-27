

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_openid import OpenID
from flask_principal import Principal,Permission,RoleNeed
from flask_admin import Admin

# Create the Flask-Bcrypt's instance, a hash algorithm for password
bcrypt = Bcrypt()