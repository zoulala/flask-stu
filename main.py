import datetime
from config import DevConfig
from flask import Flask,render_template,url_for,redirect
from models import db,User,Post,Tag,posts_tags,Comment

from sqlalchemy import func
from forms import PostForm,CommentForm



app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)



def sidebar_data():
    """Set the sidebar function."""

    # Get post of recent
    recent = db.session.query(Post).order_by(
            Post.publish_date.desc()
        ).limit(5).all()

    # Get the tags and sort by count of posts.
    top_tags = db.session.query(
            Tag, func.count(posts_tags.c.post_id).label('total')
        ).join(
            posts_tags
        ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags



@app.route('/')
@app.route('/<int:page>')
def home(page=1):
    """View function for home page"""

    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)

    recent, top_tags = sidebar_data()

    return render_template('home.html',
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)

@app.route('/post/<int:post_id>', methods=('GET', 'POST'))
def post(post_id):

    # Form object: `Comment`
    form = CommentForm()
    # form.validate_on_submit() will be true and return the
    # data object to form instance from user enter,
    # when the HTTP request is POST
    if form.validate_on_submit():
        new_comment = Comment()
        new_comment.name=form.name.data
        new_comment.text = form.text.data
        new_comment.date = datetime.datetime.now()
        new_comment.post_id = post_id
        db.session.add(new_comment)
        db.session.commit()


    post = Post.query.get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('post.html',
                           form=form,
                           post=post,
                           tags=tags,
                           comments=comments,
                           recent=recent,
                           top_tags=top_tags)

@app.route('/tag/<string:tag_name>')
def tag(tag_name):
    """View function for tag page"""

    tag = db.session.query(Tag).filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('tag.html',
                           tag=tag,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)

@app.route('/user/<string:username>')
def user(username):
    """View function for user page"""
    user = db.session.query(User).filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('user.html',
                           user=user,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    """View function for new_port."""

    form = PostForm()

    # Will be execute when click the submit in the create a new post page.
    if form.validate_on_submit():
        new_post = Post(form.title.data)
        new_post.text = form.text.data
        new_post.publish_date = datetime.datetime.now()

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('new_post.html',
                           form=form)


@app.route('/edit/<string:id>', methods=['GET', 'POST'])
def edit_post(id):
    """View function for edit_post."""
    post = Post.query.get_or_404(id)

    form = PostForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.text = form.text.data
        post.publish_date = datetime.datetime.now()

        # Update the post
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('post', post_id=post.id))

    # Still retain the original content, if validate is false.
    form.title.data = post.title
    form.text.data = post.text
    return render_template('edit_post.html', form=form, post=post)





if __name__ == "__main__":
    app.run()
