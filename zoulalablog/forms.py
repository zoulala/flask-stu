from flask_wtf import FlaskForm
from wtforms import (StringField,
                     TextAreaField)
from wtforms.validators import DataRequired, Length



class PostForm(FlaskForm):
    """Post Form."""

    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])

class CommentForm(FlaskForm):
    """Form vaildator for comment."""

    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)])

    text = StringField(u'Comment', validators=[DataRequired()])





