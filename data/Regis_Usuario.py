import sqlite3
import time
import conexion as con
from model.regis_usu import Registro_Usuario

class UsuarioData():
    
    def __init__(self):
        try:
            # Conecta o crea una base de datos llamada Inventario_prototipado.db
            self.db = con.Conexion().conectar()
            self.con = sqlite3.connect("Inventario_prototipado.db")

            sql_create_table1 = """CREATE TABLE IF NOT EXISTS Usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Numero_doc INT UNIQUE,
                Nombre TEXT, 
                Usuario TEXT UNIQUE, 
                Clave TEXT,
                Rol TEXT
                )"""
            with self.con:
                cur = self.con.cursor()
                cur.execute(sql_create_table1)

        except Exception as ex:
            print("Error al conectar con la base de datos:", ex)  # Maneja el error de conexión
    
    def Reg_Usuario(self, info: Registro_Usuario):
        retries = 5
        while retries > 0:
            try:
                sql_insert = """INSERT INTO Usuarios (Numero_doc, Nombre, Usuario, Clave, Rol) VALUES (?, ?, ?, ?, ?)"""
                with self.con:
                    cur = self.con.cursor()
                    cur.execute(sql_insert, (info._num_doc, info._nom_ape, info._usuario, info._clave, info._rol))
                break  # Salir del bucle si la inserción fue exitosa
            except sqlite3.IntegrityError as ex:
                print("El usuario ya existe:", ex)
                break  # Salir del bucle en caso de error de integridad
            except sqlite3.OperationalError as ex:
                print("Error al insertar el usuario: database is locked", ex)
                retries -= 1
                time.sleep(1)  # Esperar un segundo antes de reintentar
            except Exception as ex:
                print("Error al insertar el usuario:", ex)
                break
    
    def conectar(self):
        return self.con
