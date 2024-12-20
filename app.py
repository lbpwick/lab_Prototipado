from os import system  # Importa el comando system desde el módulo os
system("cls")  # Limpia la pantalla de la consola (en Windows)

from conexion import Conexion
from prototipado import Prototipado  # Importa la clase Prototipado desde el módulo prototipado

if __name__ == '__main__':
    # Crea una instancia de la clase Conexion y Prototipado
    Conexion()
    app = Prototipado()
    app.run()
