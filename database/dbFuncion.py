from os import error
import sqlite3
from sqlite3 import Error

from clases.funcion import Funcion


def sql_connection():
    try:
        con = sqlite3.connect('dataCine.db')
        return con
    except Error as err:
        print(err)


def sql_insert_funcion(f: Funcion):
    try:
        sql = ("INSERT INTO funcion(fecha,horario,formato,idioma,sala,idPelicula)"
               "VALUES (?, ?, ?, ?, ?, ?)")
        data = (f.fecha, f.horario, f.formato, f.idioma, f.sala, f.idPelicula)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_select_funcion(id):
    try:
        sql = "select * from funcion where idFuncion = ?;"
        data = (id,)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        funcion = cursorObj.fetchone()
        return funcion
    except Error as err:
        print(err)


def sql_select_funciones():
    try:
        sql = "select * from funcion;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        funciones = cursorObj.fetchall()
        return funciones
    except Error as err:
        print(err)


def sql_edit_funcion(f: Funcion):
    try:
        sql = ("UPDATE funcion set fecha = ?, horario = ?, formato = ?, idioma = ?, sala = ?, calificacion = ? "
               "WHERE idFuncion = ?;")
        data = (f.fecha, f.horario, f.formato, f.idioma,
                f.sala, f.calificacion, f.idFuncion)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_delete_funcion(id):
    try:
        sql = "delete from funcion where idFuncion = ?;"
        data = (id,)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)

def sql_select_funcionDetalle(id):
    try:
        sql = "select * from Funcion inner join Pelicula on Funcion.idPelicula = Pelicula.idPelicula where Pelicula.idPelicula = ?;"
        data = (id,)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        funcion = cursorObj.fetchall()
        
        return funcion
    except Error as err:
        print(err)