from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired


class FormLogin (FlaskForm):
    User = StringField('User', validators = [InputRequired(message='Indique el usuario')])
    Password = PasswordField('Password', validators = [InputRequired(message='Indique la clave')])
    Login = SubmitField('Login')
