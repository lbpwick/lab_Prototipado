import conexion as con
from model.usuario import Usuario


class UsuarioData():

    def login(self,usuario:Usuario):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        res = self.cursor.execute("SELECT * FROM Usuarios WHERE Usuario = '{}' AND Clave = '{}' ".format(usuario._usuario,usuario._clave))
        fila = res.fetchone()
        if fila:
            usuario = Usuario(nombre = fila[1], usuario=fila[2])
            self.cursor.close()
            self.db.close()
            return usuario
        else:
            self.cursor.close()
            self.db.close()
            None
            