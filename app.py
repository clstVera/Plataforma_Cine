import os
from flask import Flask

from pelicula import pelicula_blueprint
from funcion import funcion_blueprint
from comentarios import comentario_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
@app.route('/usuariosAdmin/')
def verUsuarios():
    return 'ok'

app.register_blueprint(pelicula_blueprint)
app.register_blueprint(funcion_blueprint)
app.register_blueprint(comentario_blueprint)



if __name__ == '__main__':
    app.run(debug=True, port=8000)