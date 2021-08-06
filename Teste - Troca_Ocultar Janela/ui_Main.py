# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MainPPQcCg.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(256, 249)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(36)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)

        self.btn_Goto = QPushButton(self.frame)
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

        self.verticalLayout_2.addWidget(self.btn_Goto)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Janela 1", None))
        self.btn_Goto.setText(QCoreApplication.translate("MainWindow", u"Ir para janela 2", None))
    # retranslateUi

