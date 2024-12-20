from PyQt6 import uic, QtWidgets
from data.Regis_Usuario import UsuarioData
from model.regis_usu import Registro_Usuario
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import os
import pandas as pd
from sqlalchemy import create_engine

class MainWindow(QMainWindow):  # Hereda de QMainWindow
    def __init__(self):
        super().__init__()  # Llama al constructor de la superclase
        # Carga la interfaz de usuario del archivo main.ui
        self.ui = uic.loadUi("gui/main.ui", self)  # Cambia self.main a self.ui
        self.initGUI()  # Inicializa los componentes de la GUI
        self.showMaximized()  # Muestra la ventana de inicio de sesión

    def initGUI(self):
        self.ui.btn_import_Excel_a_db.triggered.connect(self.cargarExcel)
        self.ui.btn_Reg_Usuario.triggered.connect(self.adrir_reg)
        self.registro_usu = uic.loadUi("gui/Registro_Usu.ui")

    def adrir_reg(self):
        self.limpiarCampos()  # Limpiar los campos de texto
        self.registro_usu.show()
        self.registro_usu.btn_Reg_Usuario.clicked.connect(self.registar_usuarios)

    def registar_usuarios(self):
        if self.registro_usu.comboBox_Reg_Usuario.currentText() == "-- Seleccione Una Opcion":
            mbox = QMessageBox()
            mbox.setText("Debe Seleccionar Rol de Usuario")
            mbox.exec()
            self.registro_usu.comboBox_Reg_Usuario.setFocus()
        elif not self.registro_usu.txt_Reg_Usuario_Num_Doc.text().isnumeric() or len(self.registro_usu.txt_Reg_Usuario_Num_Doc.text()) < 2:
            mbox = QMessageBox()
            mbox.setText("Debe Ingresar Número de Documento Válido")
            mbox.exec()
            self.registro_usu.txt_Reg_Usuario_Num_Doc.setFocus()
            self.registro_usu.txt_Reg_Usuario_Num_Doc.setText("0")
        else:
            regis_usua = Registro_Usuario(
                num_doc=self.registro_usu.txt_Reg_Usuario_Num_Doc.text(),
                nom_ape=self.registro_usu.txt_Reg_Usuario_Nom_Ape.text().capitalize(),
                usuario=self.registro_usu.txt_Reg_Usuario_Usuario.text().lower(),
                clave=self.registro_usu.txt_Reg_Usuario_Clave.text(),
                rol=self.registro_usu.comboBox_Reg_Usuario.currentText()
            )
            self.registro_usu.hide()

        objectData = UsuarioData()
        mbox = QMessageBox()
        if objectData.Reg_Usuario(info=regis_usua):
            mbox.setText("Usuario No Registrado.")
        else:
            mbox.setText("Usuario Registrado")
        mbox.exec()


    def cargarExcel(self):
        self.excel_path = None
        self.excel_path, _ = QFileDialog.getOpenFileName(self, "Seleccione archivo Excel", "", "Archivos Excel (*.xlsx)")
        if self.excel_path:
            # Procesar el archivo Excel
            db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inventario_prototipado.db")
            try:
                engine = create_engine(f'sqlite:///{db_path}')
                df1 = pd.read_excel(self.excel_path, sheet_name='Equipos', skiprows=1)
                df2 = pd.read_excel(self.excel_path, sheet_name='Insumos', skiprows=1)
                df1.columns = ['Item', 'Cantidad', '% De Avance En Hermes', 'Placa', 'Equipo/Nombre', 'Marca', 'Modelo', 'Numero Serial', 'Para Que Se Utiliza', 'Procedencia', 'Usos', 'Responsable', 'N° De odc Y Año', 'Año De Compra', 'Precio', 'Proveedor', 'Fecha De Fabricación Del Equipo', 'Vida útil Estimada En Años', 'Fecha De instalación', 'Fin De Depreciación Del Equipo', 'Tiempo De garantía En Meses', 'Ubicación', 'Información Que Hace Falta Del Equipo', 'Observaciones']
                df2.columns = ['Item', 'Código', 'Descripción', 'Cantidad', 'Responsable', 'N° De Odc', 'Año De Compra', 'Precio', 'Proveedor', 'Ubicación']
                df1.to_sql('Equipos', con=engine, if_exists='replace', index=False)
                df2.to_sql('Insumos', con=engine, if_exists='replace', index=False)
                QMessageBox.information(self, "Éxito", "Base de datos creada a partir del archivo Excel.")
            except Exception as e:
                QMessageBox.warning(self, "Advertencia", f"Error al crear la base de datos: {e}")
        else:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un archivo Excel.")


    def limpiarCampos(self):
        self.registro_usu.txt_Reg_Usuario_Num_Doc.clear()
        self.registro_usu.txt_Reg_Usuario_Nom_Ape.clear()
        self.registro_usu.txt_Reg_Usuario_Usuario.clear()
        self.registro_usu.txt_Reg_Usuario_Clave.clear()
        self.registro_usu.comboBox_Reg_Usuario.setCurrentIndex(0)