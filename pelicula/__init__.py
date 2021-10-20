from flask import Blueprint, render_template, request, redirect, url_for

from datetime import datetime
from forms.formPelicula import FormPelicula
from clases.pelicula import Pelicula
from database.dbPelicula import sql_select_pelicula, sql_select_peliculas, sql_insert_pelicula, sql_edit_pelicula, sql_delete_pelicula

pelicula_blueprint = Blueprint('pelicula_blueprint', __name__, template_folder='templates')

@pelicula_blueprint.route('/peliculas/')
def verPelicula():
    peliculas = sql_select_peliculas()
    return render_template('peliculas.html', peliculas=peliculas)

@pelicula_blueprint.route('/peliculas/add/', methods=['GET', 'POST'])
def crearPelicula():
    if request.method == "GET":
        form = FormPelicula()
        return render_template('pelicula.html', form=form, action='Add')
    if request.method == "POST":
        pelicula = Pelicula()
        pelicula.titulo = request.form["titulo"]
        pelicula.titulo_original = request.form["tituloOriginal"]
        pelicula.genero = request.form["genero"]
        pelicula.clasificacion = request.form["clasificacion"]
        pelicula.duracion = request.form["duracion"]
        pelicula.estreno = request.form["estreno"]
        pelicula.director = request.form["director"]
        pelicula.actores = request.form["actores"]
        pelicula.pais_origen = request.form["paisOrigen"]
        pelicula.descripcion = request.form["descripcion"]
        pelicula.imagen = request.form["imagen"]
        pelicula.trailer = request.form["trailer"]
        sql_insert_pelicula(pelicula)
        return redirect(url_for('pelicula_blueprint.verPelicula'))

@pelicula_blueprint.route('/peliculas/edit/<string:idPelicula>', methods=['GET', 'POST'])
def editarPelicula(idPelicula):
    pelicula = sql_select_pelicula(idPelicula)
    form = FormPelicula(obj=pelicula)
    if form.validate_on_submit():
        pelicula = Pelicula()
        pelicula.idPelicula = idPelicula
        pelicula.titulo = form.titulo.data
        pelicula.titulo_original = form.tituloOriginal.data
        pelicula.genero = form.genero.data
        pelicula.clasificacion = form.clasificacion.data
        pelicula.duracion = form.duracion.data
        pelicula.estreno = form.estreno.data
        pelicula.director = form.director.data
        pelicula.actores = form.actores.data
        pelicula.pais_origen = form.paisOrigen.data
        pelicula.descripcion = form.descripcion.data
        pelicula.imagen = form.imagen.data
        pelicula.trailer = form.trailer.data
        pelicula.calificacion = form.calificacion.data
        pelicula.votos = form.votos.data
        sql_edit_pelicula(pelicula)
        return redirect(url_for('pelicula_blueprint.verPelicula'))

    form.idPelicula.data = idPelicula
    form.titulo.data = pelicula[1]
    form.tituloOriginal.data = pelicula[2]
    form.genero.data = pelicula[3]
    form.clasificacion.data = pelicula[4]
    form.duracion.data = pelicula[5]
    form.estreno.data = datetime.strptime(pelicula[6], '%Y-%m-%d')
    form.director.data = pelicula[7]
    form.actores.data = pelicula[8]
    form.paisOrigen.data = pelicula[9]
    form.descripcion.data = pelicula[10]
    form.imagen.data = pelicula[11]
    form.trailer.data = pelicula[12]
    form.calificacion.data = pelicula[13]
    form.votos.data = pelicula[14]
    return render_template('pelicula.html', form=form, action='Edit')

@pelicula_blueprint.route('/peliculas/delete/<string:idPelicula>', methods=['GET'])
def eliminarPelicula(idPelicula):
    sql_delete_pelicula(idPelicula)
    return redirect(url_for('pelicula_blueprint.verPelicula'))