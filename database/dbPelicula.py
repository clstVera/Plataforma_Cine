from os import error
import sqlite3
from sqlite3 import Error

from clases.pelicula import Pelicula


def sql_connection():
    try:
        con = sqlite3.connect('dataCine.db')
        return con
    except Error as err:
        print(err)


def sql_insert_pelicula(p: Pelicula):
    try:
        sql = ("INSERT INTO pelicula (titulo,titulo_original,genero,clasificacion,duracion,estreno,director,actores,pais_origen,descripcion,imagen,trailer) "
               "VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
        data = (p.titulo, p.titulo_original, p.genero, p.clasificacion, p.duracion, p.estreno,
                p.director, p.actores, p.pais_origen, p.descripcion, p.imagen, p.trailer)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_select_pelicula(id):
    sql = "select * from pelicula where idPelicula = ?;"
    data = (id,)
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(sql, data)
    pelicula = cursorObj.fetchone()
    return pelicula


def sql_select_peliculas():
    try:
        sql = "select * from pelicula;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        peliculas = cursorObj.fetchall()
        return peliculas
    except Error as err:
        print(err)


def sql_edit_pelicula(p: Pelicula):
    try:
        sql = ("UPDATE pelicula set titulo = ?, titulo_original = ?, genero = ?, clasificacion = ?, duracion = ?, estreno = ?, director = ?, actores = ?, pais_origen = ?, descripcion = ?, imagen = ?, trailer = ?, calificacion = ?, votos = ? "
               "WHERE idPelicula = ?")
        data = (p.titulo, p.titulo_original, p.genero, p.clasificacion, p.duracion, p.estreno, p.director,
                p.actores, p.pais_origen, p.descripcion, p.imagen, p.trailer, p.calificacion, p.votos, p.idPelicula)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_delete_pelicula(id):
    try:
        sql = "delete from pelicula where idPelicula = ?;"
        data = (id,)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)
