# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceuRehYf.ui'
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
        MainWindow.resize(414, 359)
        MainWindow.setMinimumSize(QSize(414, 359))
        MainWindow.setMaximumSize(QSize(640, 480))
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(120, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_AdicionarItem = QPushButton(self.frame_4)
        self.btn_AdicionarItem.setObjectName(u"btn_AdicionarItem")

        self.verticalLayout_2.addWidget(self.btn_AdicionarItem)

        self.btn_Atualizar = QPushButton(self.frame_4)
        self.btn_Atualizar.setObjectName(u"btn_Atualizar")

        self.verticalLayout_2.addWidget(self.btn_Atualizar)


        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.txt_Nome = QLineEdit(self.frame_6)
        self.txt_Nome.setObjectName(u"txt_Nome")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txt_Nome)


        self.verticalLayout_4.addLayout(self.formLayout)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 30))
        self.frame_7.setMaximumSize(QSize(16777215, 30))
        self.frame_7.setFrameShape(QFrame.Panel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.txt_Selecionado = QLineEdit(self.frame_7)
        self.txt_Selecionado.setObjectName(u"txt_Selecionado")
        self.txt_Selecionado.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.txt_Selecionado)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lst_Itens = QListWidget(self.frame_2)
        self.lst_Itens.setObjectName(u"lst_Itens")

        self.horizontalLayout_4.addWidget(self.lst_Itens)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_AdicionarItem.setText(QCoreApplication.translate("MainWindow", u"Adicionar Item", None))
        self.btn_Atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Clicado:", None))
    # retranslateUi

