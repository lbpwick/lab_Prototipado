# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(976, 759)
        self.btn_import_Excel_a_db = QAction(Main)
        self.btn_import_Excel_a_db.setObjectName(u"btn_import_Excel_a_db")
        self.btn_import_db = QAction(Main)
        self.btn_import_db.setObjectName(u"btn_import_db")
        self.btn_Reg_Usuario = QAction(Main)
        self.btn_Reg_Usuario.setObjectName(u"btn_Reg_Usuario")
        self.btn_Reg_Equipo = QAction(Main)
        self.btn_Reg_Equipo.setObjectName(u"btn_Reg_Equipo")
        self.btn_Reg_Insumos = QAction(Main)
        self.btn_Reg_Insumos.setObjectName(u"btn_Reg_Insumos")
        self.btn_Prest_Insumos = QAction(Main)
        self.btn_Prest_Insumos.setObjectName(u"btn_Prest_Insumos")
        self.btn_Prest_Equipos = QAction(Main)
        self.btn_Prest_Equipos.setObjectName(u"btn_Prest_Equipos")
        self.btn_Dev_Equipos = QAction(Main)
        self.btn_Dev_Equipos.setObjectName(u"btn_Dev_Equipos")
        self.btn_Dev_Insumos = QAction(Main)
        self.btn_Dev_Insumos.setObjectName(u"btn_Dev_Insumos")
        self.centralwidget = QWidget(Main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 70, 391, 61))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(148, 180, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 40, 141, 111))
        self.label.setPixmap(QPixmap(u"../Logotipo.unal.svg.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 976, 22))
        self.menArchivo = QMenu(self.menubar)
        self.menArchivo.setObjectName(u"menArchivo")
        self.menuRegistro = QMenu(self.menubar)
        self.menuRegistro.setObjectName(u"menuRegistro")
        self.menuPrestamo = QMenu(self.menubar)
        self.menuPrestamo.setObjectName(u"menuPrestamo")
        self.menuDevolucion = QMenu(self.menubar)
        self.menuDevolucion.setObjectName(u"menuDevolucion")
        Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Main)
        self.statusbar.setObjectName(u"statusbar")
        Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menArchivo.menuAction())
        self.menubar.addAction(self.menuRegistro.menuAction())
        self.menubar.addAction(self.menuPrestamo.menuAction())
        self.menubar.addAction(self.menuDevolucion.menuAction())
        self.menArchivo.addAction(self.btn_import_Excel_a_db)
        self.menArchivo.addAction(self.btn_import_db)
        self.menuRegistro.addAction(self.btn_Reg_Usuario)
        self.menuRegistro.addAction(self.btn_Reg_Equipo)
        self.menuRegistro.addAction(self.btn_Reg_Insumos)
        self.menuPrestamo.addAction(self.btn_Prest_Insumos)
        self.menuPrestamo.addAction(self.btn_Prest_Equipos)
        self.menuDevolucion.addAction(self.btn_Dev_Equipos)
        self.menuDevolucion.addAction(self.btn_Dev_Insumos)

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Laboratorio Prototipado Unal-La Paz", None))
        self.btn_import_Excel_a_db.setText(QCoreApplication.translate("Main", u"Importar Excel a db", None))
        self.btn_import_db.setText(QCoreApplication.translate("Main", u"importar db", None))
        self.btn_Reg_Usuario.setText(QCoreApplication.translate("Main", u"Usuario", None))
        self.btn_Reg_Equipo.setText(QCoreApplication.translate("Main", u"Equipos", None))
        self.btn_Reg_Insumos.setText(QCoreApplication.translate("Main", u"Insumos", None))
        self.btn_Prest_Insumos.setText(QCoreApplication.translate("Main", u"Insumos", None))
        self.btn_Prest_Equipos.setText(QCoreApplication.translate("Main", u"Equipos", None))
        self.btn_Dev_Equipos.setText(QCoreApplication.translate("Main", u"Equipos", None))
        self.btn_Dev_Insumos.setText(QCoreApplication.translate("Main", u"Insumos", None))
        self.label_2.setText(QCoreApplication.translate("Main", u"Laboratorio De Prototipado", None))
        self.label.setText("")
        self.menArchivo.setTitle(QCoreApplication.translate("Main", u"Archivo", None))
        self.menuRegistro.setTitle(QCoreApplication.translate("Main", u"Registro", None))
        self.menuPrestamo.setTitle(QCoreApplication.translate("Main", u"Prestamo", None))
        self.menuDevolucion.setTitle(QCoreApplication.translate("Main", u"Devolucion", None))
    # retranslateUi

