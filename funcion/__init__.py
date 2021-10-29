from flask import Blueprint, render_template, request, redirect, url_for

from datetime import datetime
from forms.formFuncion import FormFuncion
from clases.funcion import Funcion
from database.dbFuncion import sql_select_funcion, sql_select_funciones, sql_insert_funcion, sql_edit_funcion, sql_delete_funcion

funcion_blueprint = Blueprint('funcion_blueprint', __name__, template_folder='templates')

@funcion_blueprint.route('/funciones/')
def verFuncion():
    funciones = sql_select_funciones()
    return render_template('funciones.html', funciones=funciones)

@funcion_blueprint.route('/funciones/add/', methods=['GET', 'POST'])
def crearFuncion():
    if request.method == "GET":
        form = FormFuncion()
        return render_template('funcion.html', form=form)
    if request.method == "POST":
        funcion = Funcion()
        funcion.fecha = request.form["fecha"]
        funcion.horario = request.form["horario"]
        funcion.formato = request.form["formato"]
        funcion.idioma = request.form["idioma"]
        funcion.sala = request.form["sala"]
        funcion.idPelicula = request.form["idPelicula"]
        sql_insert_funcion(funcion)
        return redirect(url_for('funcion_blueprint.verFuncion'))
 
@funcion_blueprint.route('/funciones/edit/<string:idFuncion>', methods=['GET', 'POST'])
def editarFuncion(idFuncion):
    funcion = sql_select_funcion(idFuncion)
    form = FormFuncion(obj=funcion)
    if form.validate_on_submit():
        funcion = Funcion()
        funcion.idFuncion = idFuncion
        funcion.fecha = form.fecha.data
        funcion.horario = form.horario.data
        funcion.formato = form.formato.data
        funcion.idioma = form.idioma.data
        funcion.sala = form.sala.data
        funcion.calificacion = form.calificacion.data
        sql_edit_funcion(funcion)
        return redirect(url_for('funcion_blueprint.verFuncion'))

    form.idFuncion.data = idFuncion
    form.fecha.data = datetime.strptime(funcion[1], '%Y-%m-%d')
    form.horario.data = funcion[2]
    form.formato.data = funcion[3]
    form.idioma.data = funcion[4]
    form.sala.data = funcion[5]
    form.calificacion.data = funcion[6]
    return render_template('funcion.html', form=form, action='Edit')

@funcion_blueprint.route('/funciones/delete/<string:idFuncion>', methods=['GET'])
def eliminarFuncion(idFuncion):
    sql_delete_funcion(idFuncion)
    return redirect(url_for('funcion_blueprint.verFuncion'))

