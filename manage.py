
import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from zoulalablog import create_app
from zoulalablog import models

# Get the ENV from os_environ, default app.config='Dev'+'Config'
env = os.environ.get('BLOG_ENV', 'Dev')
# Create the app instance via Factory Method
app = create_app('zoulalablog.config.%sConfig' % env.capitalize())



manager = Manager(app)  # init project's manager tool
migrate = Migrate(app, models.db)  # init db's advance tool

manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag)

if __name__ == "__main__":
    manager.run()