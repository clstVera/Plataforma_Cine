from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class FormPelicula(FlaskForm):
    titulo = StringField('Titulo', validators=[
        DataRequired(message='Campo Requerido')])
    tituloOriginal = StringField('Titulo Original', validators=[
        DataRequired(message='Campo Requerido')])
    genero = SelectField('Genero', choices=[('Acción', 'Acción'), ('Aventuras', 'Aventuras'), ('Ciencia Ficción', 'Ciencia Ficción'), ('Comedia', 'Comedia'), ('Documental', 'Documental'), ('Drama', 'Drama'), ('Fantasía', 'Fantasía'), ('Musical', 'Musical'), ('Suspenso', 'Suspenso'), ('Terror', 'Terror')], validators=[
        DataRequired(message='Campo Requerido')])
    clasificacion = SelectField('Clasificación', choices=[('Todos', 'Niños – Apta para todo público'), ('7+', 'Recomendada para mayores de 7 años'), ('12+', 'Recomendada para mayores de 12 años'), ('15+', 'Apta para mayores de 15 años'), ('18+', 'Apta para mayores de 18 años')], validators=[
        DataRequired(message='Campo Requerido')])
    paisOrigen = StringField('País Origen', validators=[
        DataRequired(message='Campo Requerido')])
    duracion = StringField('Duración', validators=[
        DataRequired(message='Campo Requerido')])
    estreno = DateField('Estreno', format='%Y-%m-%d', validators=[
        DataRequired(message='Campo Requerido')])
    director = StringField('Director', validators=[
        DataRequired(message='Campo Requerido')])
    actores = TextAreaField('Actores', validators=[
        DataRequired(message='Campo Requerido')])
    descripcion = TextAreaField('Descripción', validators=[
        DataRequired(message='Campo Requerido')])
    imagen = StringField('Imagen (url)', validators=[
        DataRequired(message='Campo Requerido')])
    trailer = StringField('Tráiler (url)', validators=[
        DataRequired(message='Campo Requerido')])
    calificacion = StringField('Calificación')
    votos = StringField('Votos')
    idPelicula = StringField('Id')
    enviar = SubmitField('Guardar')
