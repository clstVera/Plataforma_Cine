from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class FormUsuarios(FlaskForm):
    No = StringField('No')
    Nombre = StringField('Nombre', validators=[
        DataRequired(message='Campo Requerido')])
    Password = PasswordField('Password', validators=[
        DataRequired(message='Campo Requerido')])
    Cedula = StringField('Cedula', validators=[
        DataRequired(message='Campo Requerido')])
    Rol = StringField('Rol', validators=[
        DataRequired(message='Campo Requerido')])
    Email = StringField('Email', validators=[
        DataRequired(message='Campo Requerido')])
    Telefono = StringField('Telefono', validators=[
        DataRequired(message='Campo Requerido')])
    enviar = SubmitField('Guardar')
