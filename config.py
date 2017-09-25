
class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True

    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:560320@localhost:3306/flask_stu'
    # SQLite connection
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'

