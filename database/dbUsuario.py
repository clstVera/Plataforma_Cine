from os import error
import sqlite3
from sqlite3 import Error

from clases.usuario import Usuario 


def sql_connection():
    try:
        con = sqlite3.connect('dataCine.db')
        return con
    except Error as err:
        print(err)


def sql_insert_usuario(u: Usuario):
    try:
        sql = ("INSERT INTO usuario (No, Nombre, Password, Cedula, Rol, Email, Telefono )"
               "VALUES (?,?,?,?,?,?,?)")
        data = (u.No, u.Nombre, u.Password, u.Cedula, u.Rol, u.Email, u.Telefono)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)



def sql_select_usuario(Cedula):
    try:
        
        sql = "select * from Usuario where Cedula = ?;"
        data = (Cedula,)
        con = sql_connection()
        cursorObj = con.cursor()
        retult =  cursorObj.execute(sql, data)
        print(retult)
        if( retult):
            return retult.fetchone()
        else:
            return None
    

    except Error as err:
        print(err)


def sql_select_usuarios():
    try:
        sql = "select * from Usuario;"
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql)
        usuarios = cursorObj.fetchall()
        return usuarios
    except Error as err:
        print(err)


def sql_edit_usuario(u: Usuario):
    try:
        sql = ("UPDATE Usuario set No = ?, Nombre = ?, Password =? Rol = ?, Email = ?, Telefono = ? "
            "WHERE Cedula = ?")
        data = (u.No, u.Nombre, u.Password, u. Rol, u.Email, u.Telefono, u.Cedula)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)


def sql_delete_usuario(Cedula):
    try:
        sql = "delete from usuario where Cedula = ?;"
        data = (Cedula,)
        con = sql_connection()
        cursorObj = con.cursor()
        cursorObj.execute(sql, data)
        con.commit()
        con.close()
    except Error as err:
        print(err)


