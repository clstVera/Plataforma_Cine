from flask import Blueprint, render_template, request, redirect, url_for, session, flash

from datetime import datetime
from forms.formUsuarios import FormUsuarios
from clases.usuario import Usuario
from database.dbUsuario import sql_select_usuario, sql_select_usuarios, sql_insert_usuario, sql_edit_usuario, sql_delete_usuario,sql_connection

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
        usuario.Password = request.form["Password"]
        usuario.Cedula = request.form["Cedula"]
        usuario.Rol = request.form["Rol"]
        usuario.Email = request.form["Email"]
        usuario.Telefono = request.form["Telefono"]
        sql_insert_usuario(usuario)
        return redirect(url_for('usuario_blueprint.verUsuarios'))

@usuario_blueprint.route('/Usuarios/adduser', methods=['GET', 'POST'])
def crearUsuarioFinal():
    if request.method == "GET":
        form = FormUsuarios()
        return render_template('usuariosfinal.html', form=form, action='Add')
    if request.method == "POST":
        usuario = Usuario()
        usuario.No = ["20"]
        usuario.Nombre = request.form["Nombre"]
        usuario.Password = request.form["Password"]
        usuario.Cedula = request.form["Cedula"]
        usuario.Rol = ["USER"]
        usuario.Email = request.form["Email"]
        usuario.Telefono = request.form["Telefono"]

        sql_insert_usuario(usuario)
        return redirect(url_for('usuario_blueprint.loginUsuario'))

@usuario_blueprint.route('/Usuarios/edit/<string:Cedula>', methods=['GET', 'POST'])
def editarUsuario(Cedula,):
    usuario = sql_select_usuario(Cedula)
    form = FormUsuarios(obj=usuario)
    if form.validate_on_submit():
        usuario = Usuario()
        sql_edit_usuario(usuario)
        usuario.Cedula= Cedula
        usuario.No = form.No.data
        usuario.Nombre = form.Nombre.data
        usuario.Password = form.Password.data
        usuario.Rol = form.Rol.data
        usuario.Email = form.Email.data
        usuario.Telefono = form.Telefono.data 
        sql_edit_usuario(usuario)
        return redirect(url_for('usuario_blueprint.verUsuarios'))
    
    form.Cedula.data =Cedula
    form.No.data = usuario[0]
    form.Nombre.data = usuario[1]
    form.Password.data = usuario[2]
    form.Rol.data = usuario[4]
    form.Email.data = usuario[5]
    form.Telefono.data = usuario[6]
    
    return render_template('usuario.html', form=form, action='Edit')

@usuario_blueprint.route('/Usuarios/delete/<string:Cedula>', methods=['GET'])
def eliminarUsuario(Cedula,):
    sql_delete_usuario(Cedula)
    return redirect(url_for('usuario_blueprint.verUsuarios'))

@usuario_blueprint.route("/loginUsuario", methods=['POST','GET'])
def loginUsuario():
    if request.method == "POST":
        Cedula = request.form["Cedula"]
        Password = request.form["password"]
        comparar=sql_select_usuario(Cedula)
        if comparar != None:
            if comparar[2] == Password:

        
                session['cedula'] = Cedula
            
                if 'cedula' in session and comparar[2]==Password and comparar[4]=="ADMIN":
                        
                        return redirect(url_for('pelicula_blueprint.verPelicula'))
                
                elif 'cedula' in session and comparar[2]==Password and comparar[4]=="USER":
                        return redirect(url_for('pelicula_blueprint.indexlogeado'))
            else:
                flash("Usuario o contraseña incorrectos")
                return render_template("loginUsuario.html")

        
        
        else:    
            return render_template("loginUsuario.html")
    else:    
            return render_template("loginUsuario.html")


@usuario_blueprint.route('/cerrar')
def cerrar():
    session.pop('cedula', None)
    return redirect(url_for('usuario_blueprint.loginUsuario'))


@usuario_blueprint.route('/forgotpassword/')
def forgotpassword():
    usuarios = sql_select_usuarios()
    return render_template('forgotpassword.html')