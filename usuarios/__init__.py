from flask import Blueprint, render_template, request, redirect, url_for

from datetime import datetime
from forms.formUsuarios import FormUsuarios
from clases.usuario import Usuario
from database.dbUsuario import sql_select_usuario, sql_select_usuarios, sql_insert_Usuario, sql_edit_usuario, sql_delete_usuario

usuario_blueprint = Blueprint('usuario_blueprint', __name__, template_folder='templates')

@usuario_blueprint.route('/Usuarios/')
def verUsuarios():
    usuarios = sql_select_usuarios()
    return render_template('Usuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/Usuarios/add', methods=['GET', 'POST'])
def crearUsuario():
    if request.method == "GET":
        form = FormUsuarios()
        return render_template('Usuario.html', form=form, action='Add')
    if request.method == "POST":
        usuario = Usuario()
        usuario.No = request.form["No"]
        usuario.Nombre = request.form["Nombre"]
        usuario.Edad = request.form["Edad"]
        usuario.Cedula = request.form["Cedula"]
        usuario.Rol = request.form["Rol"]
        usuario.Email = request.form["Email"]
        usuario.Telefono = request.form["Telefono"]
        sql_insert_Usuario(usuario)
        return redirect(url_for('usuario_blueprint.verUsuarios'))

@usuario_blueprint.route('/Usuarios/edit/<Cedula>', methods=['GET', 'POST'])
def editarUsuario(Cedula,):
    usuario = sql_select_usuario(Cedula)
    form = FormUsuarios(obj=usuario)
    if form.validate_on_submit():
        usuario = Usuario()
        usuario.No = form.No.data
        usuario.Nombre = form.Nombre.data
        usuario.Edad = form.Edad.data
        usuario.Cedula= Cedula
        usuario.Rol = form.Rol.data
        usuario.Email = form.Email.data
        usuario.Telefono = form.Telefono.data
        
        sql_edit_usuario(usuario)
        return redirect(url_for('usuario_blueprint.verUsuarios'))

    form.No.data = Usuario[0]
    form.Nombre.data = Usuario[1]
    form.Edad.data = Usuario[2]
    form.Cedula.data = Usuario[3]
    form.Rol.data = Usuario[4]
    form.Email.data = Usuario[5]
    form.Telefono.data = Usuario[6]
    
    return render_template('usuario.html', form=form, action='Edit')

@usuario_blueprint.route('/Usuarios/delete/<Cedula>', methods=['GET'])
def eliminarUsuario(Cedula,):
    sql_delete_usuario(Cedula)
    return redirect(url_for('usuario_blueprint.verUsuarios'))