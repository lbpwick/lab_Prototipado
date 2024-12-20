import os
import pandas as pd
from sqlalchemy import create_engine
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox
import sys

class EjecutarBaseDatos(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejecutar Base de Datos")

        layout = QVBoxLayout()

        self.db_label = QLabel("Seleccione archivo de base de datos (opcional):")
        layout.addWidget(self.db_label)

        self.db_button = QPushButton("Examinar")
        self.db_button.clicked.connect(self.seleccionar_db)
        layout.addWidget(self.db_button)

        self.ejecutar_button = QPushButton("Ejecutar")
        self.ejecutar_button.clicked.connect(self.ejecutar_proceso)
        layout.addWidget(self.ejecutar_button)

        self.setLayout(layout)

        self.db_path = None

    def seleccionar_db(self):
        self.db_path, _ = QFileDialog.getOpenFileName(self, "Seleccione archivo de base de datos", "", "Archivos de base de datos (*.db)")
        self.db_label.setText(f"Archivo seleccionado: {self.db_path}")

    def ejecutar_proceso(self):
        # Guardar la base de datos en la misma ubicación que este código
        if not self.db_path:
            self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inventario_prototipado.db")

        try:
            engine = create_engine(f'sqlite:///{self.db_path}')
            # Aquí puedes agregar el código para realizar consultas o procesos sobre la base de datos
            QMessageBox.information(self, "Éxito", f"Base de datos cargada/guardada en {self.db_path}.")
        except Exception as e:
            QMessageBox.warning(self, "Advertencia", f"Error al cargar/guardar la base de datos: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EjecutarBaseDatos()
    window.show()
    sys.exit(app.exec())
