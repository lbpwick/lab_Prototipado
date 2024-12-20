from PyQt6 import uic  # Importa uic para cargar archivos .ui
from PyQt6.QtWidgets import QMessageBox

class RegistroWindow():
    def __init__(self):  
        self.reg_vent = uic.loadUi("gui/Registro_Usu.ui")
        self.reg_vent.show()

