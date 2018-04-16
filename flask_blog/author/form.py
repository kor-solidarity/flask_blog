from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    fullname = StringField('Full name', [validators.Required()])
    email = EmailField('email', [validators.Required()])
    username = StringField('username', [
        validators.Required(), 
        validators.Length(min=4, max=25)
        ])
    password = PasswordField('new password',[
        validators.Required(),
        validators.EqualTo('confirm', message='password not same'),
        validators.Length(min=4, max=80)
        ])
    confirm = PasswordField('repeat password')


class LoginForm(Form):
    username = StringField("username", [
        validators.Required(),
        validators.Length(min=4, max=25)
    ])
    password = PasswordField('password', [
        validators.Required(),
        validators.Length(min=4, max=8)
    ])