from flask_wtf import FlaskForm, Form
from wtforms import StringField, validators, TextAreaField
from author.form import RegisterForm
from blog.models import Category
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class SetupForm(RegisterForm):
    name = StringField('블로그명', [
        validators.Required()
        , validators.Length(max=80)
        ]) 


def categories():
    return Category.query


class PostForm(Form):
    title = StringField('title', [
        validators.required(),
        validators.Length(max=80)
    ])
    body = TextAreaField('content', validators=[
        validators.Required()
    ])
    category = QuerySelectField('category', query_factory=categories, allow_blank=True)
    new_category = StringField('new category')