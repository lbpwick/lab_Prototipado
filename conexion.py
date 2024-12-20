import sqlite3  # Importa el módulo sqlite3 para manejar la base de datos SQLite

class Conexion:
    def __init__(self):
        try:
            # Conecta o crea una base de datos llamada Inventario_prototipado.db
            self.con = sqlite3.connect("Inventario_prototipado.db")
            self.crearTablas()  # Llama al método para crear tablas
            self.crearAdmin()  # Llama al método para crear el usuario administrador
        except Exception as ex:
            print(ex)  # Imprime cualquier excepción que ocurra

    def crearTablas(self):
        # Define la sentencia SQL para crear la tabla Usuarios si no existe
        sql_create_table1 = """CREATE TABLE IF NOT EXISTS Usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Numero_doc INT UNIQUE,
            Nombre TEXT, 
            Usuario TEXT UNIQUE, 
            Clave TEXT,
            Rol TEXT
            )"""
        with self.con:
            cur = self.con.cursor()  # Crea un cursor para ejecutar sentencias SQL
            cur.execute(sql_create_table1)  # Ejecuta la sentencia SQL para crear la tabla

    def crearAdmin(self):
        try:
            # Define la sentencia SQL para insertar un usuario administrador
            sql_insert = """INSERT INTO Usuarios values(null, '1065205626', 'Luis Borrero', 'luborrero', 'Nolose01', 'Administrador')"""
            with self.con:
                cur = self.con.cursor()  # Crea un cursor para ejecutar la sentencia SQL
                cur.execute(sql_insert)  # Ejecuta la inserción del usuario
                self.con.commit()  # Confirma los cambios en la base de datos
        except sqlite3.IntegrityError:
            print("Ya se Creó el Usuario")
        except Exception as ex:
            print("Error al crear el usuario admin:", ex)  # Maneja otras excepciones
 
    def conectar(self):
        return self.con
