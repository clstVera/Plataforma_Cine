from flask import Blueprint, render_template, request, redirect, url_for

from datetime import datetime
from forms.formComentarios import FormComentarios
from clases.comentario import Comentario
from database.dbComentario import sql_select_comentario, sql_select_comentarios, sql_insert_comentario, sql_edit_comentario, sql_delete_comentario

comentario_blueprint = Blueprint('comentario_blueprint', __name__, template_folder='templates')

@comentario_blueprint.route('/comentarios/')
def verComentarios():
    comentarios = sql_select_comentarios()
    return render_template('comentarios.html', comentarios=comentarios)

@comentario_blueprint.route('/comentarios/add', methods=['GET', 'POST'])
def crearComentario():
    if request.method == "GET":
        form = FormComentarios()
        return render_template('comentario.html', form=form, action='Add')
    if request.method == "POST":
        comentario = Comentario()
        comentario.id = request.form["id"]
        comentario.Pelicula = request.form["Pelicula"]
        comentario.Comentario = request.form["Comentario"]
        comentario.Usuario = request.form["Usuario"]
        sql_insert_comentario(comentario)
        return redirect(url_for('comentario_blueprint.verComentarios'))

@comentario_blueprint.route('/comentarios/edit/<id>', methods=['GET', 'POST'])
def editarComentario(id,):
    comentario = sql_select_comentario(id)
    form = FormComentarios(obj=comentario)
    if form.validate_on_submit():
        comentario = Comentario()
        comentario.id = id
        comentario.Pelicula = form.Pelicula.data
        comentario.Comentario = form.Comentario.data
        comentario.Usuario = form.Usuario.data
        
        sql_edit_comentario(comentario)
        return redirect(url_for('comentario_blueprint.verComentarios'))

    form.id.data = comentario[0]
    form.Pelicula.data = comentario[1]
    form.Comentario.data = comentario[2]
    form.Usuario.data = comentario[3]
    
    return render_template('comentario.html', form=form, action='Edit')

@comentario_blueprint.route('/comentarios/delete/<id>', methods=['GET'])
def eliminarComentario(id,):
    sql_delete_comentario(id)
    return redirect(url_for('comentario_blueprint.verComentarios'))
    