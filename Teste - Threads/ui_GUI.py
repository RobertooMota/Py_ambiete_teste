# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIhlwWHC.ui'
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
        MainWindow.resize(325, 290)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.txt_Primaria = QLabel(self.frame_2)
        self.txt_Primaria.setObjectName(u"txt_Primaria")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(False)
        self.txt_Primaria.setFont(font1)

        self.verticalLayout_2.addWidget(self.txt_Primaria)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_3.addWidget(self.label_2)

        self.txt_Secundaria = QLabel(self.frame_3)
        self.txt_Secundaria.setObjectName(u"txt_Secundaria")
        self.txt_Secundaria.setFont(font1)

        self.verticalLayout_3.addWidget(self.txt_Secundaria)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_Parar = QPushButton(self.frame_4)
        self.btn_Parar.setObjectName(u"btn_Parar")

        self.horizontalLayout_2.addWidget(self.btn_Parar)

        self.btn_Acao = QPushButton(self.frame_4)
        self.btn_Acao.setObjectName(u"btn_Acao")

        self.horizontalLayout_2.addWidget(self.btn_Acao)

        self.btn_Sair = QPushButton(self.frame_4)
        self.btn_Sair.setObjectName(u"btn_Sair")

        self.horizontalLayout_2.addWidget(self.btn_Sair)


        self.verticalLayout.addWidget(self.frame_4)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Princiapal", None))
        self.txt_Primaria.setText(QCoreApplication.translate("MainWindow", u"Princiapal", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Secundaria", None))
        self.txt_Secundaria.setText(QCoreApplication.translate("MainWindow", u"Secundaria", None))
        self.btn_Parar.setText(QCoreApplication.translate("MainWindow", u"Parar", None))
        self.btn_Acao.setText(QCoreApplication.translate("MainWindow", u"Acionar", None))
        self.btn_Sair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi

