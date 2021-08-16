# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tableFHfTje.ui'
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
		MainWindow.resize(640, 480)
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
		self.tbl_Lista = QTableView(self.frame)
		self.tbl_Lista.setObjectName(u"tbl_Lista")

		self.verticalLayout_2.addWidget(self.tbl_Lista)

		self.btn_Atualizar = QPushButton(self.frame)
		self.btn_Atualizar.setObjectName(u"btn_Atualizar")

		self.verticalLayout_2.addWidget(self.btn_Atualizar)

		self.verticalLayout.addWidget(self.frame)

		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)

		QMetaObject.connectSlotsByName(MainWindow)

	# setupUi

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
		self.btn_Atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
	# retranslateUi
