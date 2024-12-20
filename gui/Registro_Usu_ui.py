# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Registro_Usu.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(737, 525)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 111, 91))
        self.label.setPixmap(QPixmap(u"../Logotipo.unal.svg.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 50, 311, 41))
        font = QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(148, 180, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 160, 101, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.comboBox_Reg_Usuario = QComboBox(Dialog)
        self.comboBox_Reg_Usuario.addItem("")
        self.comboBox_Reg_Usuario.addItem("")
        self.comboBox_Reg_Usuario.addItem("")
        self.comboBox_Reg_Usuario.addItem("")
        self.comboBox_Reg_Usuario.setObjectName(u"comboBox_Reg_Usuario")
        self.comboBox_Reg_Usuario.setGeometry(QRect(30, 210, 271, 31))
        self.comboBox_Reg_Usuario.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 160, 221, 31))
        self.label_4.setFont(font1)
        self.txt_Reg_Usuario_Num_Doc = QLineEdit(Dialog)
        self.txt_Reg_Usuario_Num_Doc.setObjectName(u"txt_Reg_Usuario_Num_Doc")
        self.txt_Reg_Usuario_Num_Doc.setGeometry(QRect(420, 210, 261, 31))
        self.txt_Reg_Usuario_Num_Doc.setFont(font1)
        self.txt_Reg_Usuario_Num_Doc.setEchoMode(QLineEdit.Normal)
        self.txt_Reg_Usuario_Num_Doc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txt_Reg_Usuario_Usuario = QLineEdit(Dialog)
        self.txt_Reg_Usuario_Usuario.setObjectName(u"txt_Reg_Usuario_Usuario")
        self.txt_Reg_Usuario_Usuario.setGeometry(QRect(420, 300, 261, 31))
        self.txt_Reg_Usuario_Usuario.setFont(font1)
        self.txt_Reg_Usuario_Usuario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(420, 260, 101, 31))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 350, 111, 31))
        self.label_6.setFont(font1)
        self.txt_Reg_Usuario_Clave = QLineEdit(Dialog)
        self.txt_Reg_Usuario_Clave.setObjectName(u"txt_Reg_Usuario_Clave")
        self.txt_Reg_Usuario_Clave.setGeometry(QRect(30, 390, 281, 41))
        self.txt_Reg_Usuario_Clave.setFont(font1)
        self.txt_Reg_Usuario_Clave.setEchoMode(QLineEdit.Password)
        self.txt_Reg_Usuario_Clave.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 260, 211, 31))
        self.label_7.setFont(font1)
        self.txt_Reg_Usuario_Nom_Ape = QLineEdit(Dialog)
        self.txt_Reg_Usuario_Nom_Ape.setObjectName(u"txt_Reg_Usuario_Nom_Ape")
        self.txt_Reg_Usuario_Nom_Ape.setGeometry(QRect(30, 300, 281, 31))
        self.txt_Reg_Usuario_Nom_Ape.setFont(font1)
        self.txt_Reg_Usuario_Nom_Ape.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_Reg_Usuario = QPushButton(Dialog)
        self.btn_Reg_Usuario.setObjectName(u"btn_Reg_Usuario")
        self.btn_Reg_Usuario.setGeometry(QRect(410, 390, 271, 41))
        self.btn_Reg_Usuario.setFont(font1)
        self.btn_Reg_Usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_Reg_Usuario.setStyleSheet(u"background-color: rgb(148, 180, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Registro Usuario", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Registro de Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Tipo Usuario:", None))
        self.comboBox_Reg_Usuario.setItemText(0, QCoreApplication.translate("Dialog", u"-- Seleccione Una Opcion", None))
        self.comboBox_Reg_Usuario.setItemText(1, QCoreApplication.translate("Dialog", u"Estudiante", None))
        self.comboBox_Reg_Usuario.setItemText(2, QCoreApplication.translate("Dialog", u"Docente", None))
        self.comboBox_Reg_Usuario.setItemText(3, QCoreApplication.translate("Dialog", u"Administrador", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"Numero de Documento:", None))
        self.txt_Reg_Usuario_Num_Doc.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese Numero Documento", None))
        self.txt_Reg_Usuario_Usuario.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese Su Usuario", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Usuario:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Contrase\u00f1a:", None))
        self.txt_Reg_Usuario_Clave.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese La Contrase\u00f1a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Ingrese Nombre y Apellido", None))
        self.txt_Reg_Usuario_Nom_Ape.setPlaceholderText(QCoreApplication.translate("Dialog", u"Ingrese Nombre y Apellido", None))
        self.btn_Reg_Usuario.setText(QCoreApplication.translate("Dialog", u"Registar", None))
    # retranslateUi

