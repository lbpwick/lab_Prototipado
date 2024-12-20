from PyQt6 import uic, QtCore  # Importa uic para cargar archivos .ui
from PyQt6.QtWidgets import QMessageBox
from data.usuarioData import UsuarioData
from main import MainWindow
from model.usuario import Usuario

class Login(QtCore.QObject):
    login_successful = QtCore.pyqtSignal()  # Definir una señal de éxito de login

    def __init__(self):
        super().__init__()
        self.login = uic.loadUi("gui/login.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()
 
    def ingresar(self):
        if len(self.login.txtUsario.text()) < 2:
            self.login.lblMensaje.setText("Ingrese Un Usuario Válido")
            self.login.txtUsario.setFocus()
        elif len(self.login.txtClave.text()) < 3:
            self.login.lblMensaje.setText("Ingrese Una Contraseña Válida")
            self.login.txtClave.setFocus()
        else:
            self.login.lblMensaje.setText("")
            usu = Usuario(usuario=self.login.txtUsario.text(), clave=self.login.txtClave.text())
            usuData = UsuarioData()
            res = usuData.login(usu)
            if res:
                self.login.lblMensaje.setText("Ok")
                self.login_successful.emit()  # Emitir la señal de éxito de login
            else:
                self.login.lblMensaje.setText("Datos Inválidos")

    def initGUI(self):
        self.login.btnAcceso.clicked.connect(self.ingresar)
