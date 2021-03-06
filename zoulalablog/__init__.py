
from flask import Flask, redirect, url_for

from zoulalablog.config import DevConfig,Dev2Config
from zoulalablog.controllers import blog,main
from zoulalablog.models import db
from zoulalablog.extensions import bcrypt,login_manager

def create_app(object_name):


    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    @app.route('/')
    def index():
        return redirect(url_for('blog.home',page=3))


    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)
    return app

if __name__ == "__main__":

    app = create_app(DevConfig)
    #app = create_app(Dev2Config)

    app.run()
