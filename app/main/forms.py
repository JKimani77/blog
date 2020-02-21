from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import Required


class FormBlog(FlaskForm):
    title = StringField('Blog Title', validators=[Required()])
    blog = StringField('Blog', validators=[Required()])
    submit = SubmitField('Post')


class FormComment(FlaskForm):
    opinion = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')
