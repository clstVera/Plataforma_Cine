from os import error
import sqlite3
from sqlite3 import Error

from clases.comentario import Comentario


def sql_connection():
    try:
        con = sqlite3.connect('dataCine.db')
        return con
    except Error as err:
        print(err)


def sql_insert_comentario(c: Comentario):
    try:
        sql = ("INSERT INTO comentario (id, Pelicula, Comentario, Usuario)"
               "VALUES (?, ?, ?, ?)")
        data = (c.id, c.Pelicula, c.Comentario, c.Usuario)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_select_comentario(id):
    try:
        sql = "select * from comentario where id = ?;"
        data = (id,)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        comentario = cursorObj.fetchone()
        return comentario
    except Error as err:
        print(err)


def sql_select_comentarios():
    try:
        sql = "select * from comentario;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        comentarios = cursorObj.fetchall()
        return comentarios
    except Error as err:
        print(err)


def sql_edit_comentario(c: Comentario):
    try:    
        sql = ("UPDATE Comentario set  Pelicula = ?, Comentario = ?, Usuario = ? "
               "WHERE id = ?;")
        data = (c.Pelicula, c.Comentario, c.Usuario, c.id)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)
    


def sql_delete_comentario(id):
    try:
        sql = "delete from comentario where id = ?;"
        data = (id,)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)
