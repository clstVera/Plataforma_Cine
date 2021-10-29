import os
from flask import Flask, render_template, request, session, redirect
from database.dbUsuario import sql_select_usuario
from forms.formLogin import FormLogin
from forms.formUsuarios import FormUsuarios
from clases.usuario import Usuario

from pelicula import pelicula_blueprint
from funcion import funcion_blueprint
from usuarios import usuario_blueprint
from comentarios import comentario_blueprint


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)



app.register_blueprint(pelicula_blueprint)
app.register_blueprint(funcion_blueprint)
app.register_blueprint(usuario_blueprint)
app.register_blueprint(comentario_blueprint)



if __name__ == '__main__':
    app.run(debug=True, port=8000)