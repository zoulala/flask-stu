from os import path
from uuid import uuid4

from flask import flash, url_for, redirect, render_template, Blueprint
from flask_login import login_user, logout_user
from flask_principal import Identity, AnonymousIdentity, identity_changed, current_app

from zoulalablog.forms import LoginForm, RegisterForm

from zoulalablog.models import db, User



main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder=path.join(path.pardir, 'templates','main')
    )

@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.home'))

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """View function for login."""

    # Create the object for LoginForm
    form = LoginForm()


    # Will be check the account whether rigjt.
    if form.validate_on_submit():

        # Using session to check the user's login status
        # Add the user's name to cookie.
        # session['username'] = form.username.data

        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.home'))

    return render_template('login.html',
                           form=form
                           )


@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    """View function for logout."""
    # Remove the username from the cookie.
    # session.pop('username', None)

    flash("You have been logged out.", category="success")
    return redirect(url_for('main.login'))


@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """View function for Register."""

    # Create the form object for RegisterForm.
    form = RegisterForm()

    # Will be check the username whether exist.
    if form.validate_on_submit():
        new_user = User(form.username.data)
        new_user.set_password(form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Your user has been created, please login.',
              category="success")

        return redirect(url_for('main.login'))
    return render_template('register.html',
                           form=form
                            )