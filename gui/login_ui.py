# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import Imagenes_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(365, 445)
        Login.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 31, 141, 121))
        self.label.setPixmap(QPixmap(u"../Logotipo.unal.svg.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(122, 151, 121, 51))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 221, 101, 31))
        self.label_3.setFont(font)
        self.label_4 = QLabel(Login)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 271, 111, 31))
        self.label_4.setFont(font)
        self.txtUsario = QLineEdit(Login)
        self.txtUsario.setObjectName(u"txtUsario")
        self.txtUsario.setGeometry(QRect(130, 221, 171, 31))
        self.txtUsario.setFont(font)
        self.txtUsario.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.txtClave = QLineEdit(Login)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setGeometry(QRect(130, 271, 171, 41))
        self.txtClave.setFont(font)
        self.txtClave.setEchoMode(QLineEdit.Password)
        self.txtClave.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btnAcceso = QPushButton(Login)
        self.btnAcceso.setObjectName(u"btnAcceso")
        self.btnAcceso.setGeometry(QRect(140, 331, 101, 31))
        self.btnAcceso.setFont(font)
        self.btnAcceso.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnAcceso.setStyleSheet(u"background-color: rgb(148, 180, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:8px")
        self.lblMensaje = QLabel(Login)
        self.lblMensaje.setObjectName(u"lblMensaje")
        self.lblMensaje.setGeometry(QRect(30, 380, 301, 31))
        self.lblMensaje.setFont(font)
        self.lblMensaje.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.lblMensaje.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Inicio Secci\u00f3n Lab Prototipado", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Login", u"Inicio de Secci\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Usuario:", None))
        self.label_4.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a:", None))
        self.txtUsario.setPlaceholderText(QCoreApplication.translate("Login", u"Ingrese Su Usuario", None))
        self.txtClave.setPlaceholderText(QCoreApplication.translate("Login", u"Ingrese La Contrase\u00f1a", None))
        self.btnAcceso.setText(QCoreApplication.translate("Login", u"Ingresar", None))
        self.lblMensaje.setText(QCoreApplication.translate("Login", u"Mensaje", None))
    # retranslateUi

