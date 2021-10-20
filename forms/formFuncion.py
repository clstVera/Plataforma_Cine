from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class FormFuncion(FlaskForm):
    fecha = DateField('Fecha', validators=[
        DataRequired(message='Campo Requerido')])
    horario = SelectField('Horario', choices=[('3:15 PM', '3:15 PM'), ('6:15 PM', '6:15 PM'), ('9:15 PM', '9:15 PM')], validators=[
        DataRequired(message='Campo Requerido')])
    formato = SelectField('Formato', choices=[('2D', '2D'), ('3D', '3D')], validators=[
        DataRequired(message='Campo Requerido')])
    idioma = SelectField('Idioma', choices=[('Original', 'Original'), ('Doblada', 'Doblada'), ('Subtitulada', 'Subtitulada')], validators=[
        DataRequired(message='Campo Requerido')])
    sala = SelectField('Sala', choices=[('Sala 1', 'Sala 1'), ('Sala 2', 'Sala 2')], validators=[
        DataRequired(message='Campo Requerido')])
    calificacion = StringField('Calificación')
    idPelicula = StringField('Id Película')
    idFuncion = StringField('Id Función')
    enviar = SubmitField('Guardar')
