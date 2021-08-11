# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uineUfkr.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SecWindow(object):
    def setupUi(self, SecWindow):
        if not SecWindow.objectName():
            SecWindow.setObjectName(u"SecWindow")
        SecWindow.resize(252, 229)
        self.centralwidget = QWidget(SecWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.lbl_Contador = QLabel(self.centralwidget)
        self.lbl_Contador.setObjectName(u"lbl_Contador")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        self.lbl_Contador.setFont(font1)

        self.verticalLayout.addWidget(self.lbl_Contador, 0, Qt.AlignHCenter)

        self.btn_Goto = QPushButton(self.centralwidget)
        self.btn_Goto.setObjectName(u"btn_Goto")
        self.btn_Goto.setStyleSheet(u"QPushButton{\n"
"border: 3px solid blue;\n"
"border-style: outset;\n"
"background-color: rgb(85, 170, 255);\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:Pressed{\n"
"border-style: inset;\n"
"background-color: rgb(85, 255, 255);\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.btn_Goto)

        SecWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecWindow)

        QMetaObject.connectSlotsByName(SecWindow)
    # setupUi

    def retranslateUi(self, SecWindow):
        SecWindow.setWindowTitle(QCoreApplication.translate("SecWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SecWindow", u"Jajela 2", None))
        self.lbl_Contador.setText(QCoreApplication.translate("SecWindow", u"Contador", None))
        self.btn_Goto.setText(QCoreApplication.translate("SecWindow", u"Ir para janela 1", None))
    # retranslateUi

