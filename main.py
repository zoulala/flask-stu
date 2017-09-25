from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)


posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id')))

class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post',
                            backref='users',
                            lazy='dynamic')

    def __init__(self, username):
        self.username = username


    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)


class Post(db.Model):
    """Represents Proected posts."""

    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    # Set the foreign key for Post
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    comments = db.relationship('Comment',
                            backref='posts',
                            lazy='dynamic')
    # many to many: posts <==> tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)

class Comment(db.Model):
    """Represents Proected posts."""

    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    # Set the foreign key for Post
    post_id = db.Column(db.Integer(), db.ForeignKey('posts.id'))

    def __repr__(self):
        return "<Model Comment `{}`>".format(self.text[:15])


class Tag(db.Model):
    """Represents Proected tags."""

    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.title)



@app.route('/')
def home():
    return '<h1>hello world</h1>'

if __name__ == "__main__":
    app.run()
