from PyQt6.QtWidgets import QApplication
from gui.login import Login
from main import MainWindow

class Prototipado:
    def __init__(self):
        self.app = QApplication([])
        self.login_window = Login()
        self.login_window.login_successful.connect(self.show_main_window)
        self.main_window = None  # Asegurarse de que main_window se inicialice como None

    def show_main_window(self):
        if self.main_window is None:  # Solo crear la ventana principal si aún no existe
            self.main_window = MainWindow()
            self.main_window.show()
            self.login_window.login.close()  # Cierra la ventana de login después de mostrar la ventana principal

    def run(self):
        self.app.exec()
