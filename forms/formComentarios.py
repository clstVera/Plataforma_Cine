from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class FormComentarios (FlaskForm):
    id = StringField('Id', validators=[
        DataRequired(message='Campo Requerido')])
    Pelicula = StringField('Pelicula', validators=[
        DataRequired(message='Campo Requerido')])
    Comentario = StringField('Comentario', validators=[
        DataRequired(message='Campo Requerido')])
    Usuario = StringField('Usuario', validators=[
        DataRequired(message='Campo Requerido')])
    Actualizar = SubmitField('Actualizar')
