# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainViVLiF.ui'
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
		MainWindow.resize(472, 480)
		self.centralwidget = QWidget(MainWindow)
		self.centralwidget.setObjectName(u"centralwidget")
		self.verticalLayout = QVBoxLayout(self.centralwidget)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName(u"verticalLayout")
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.frame = QFrame(self.centralwidget)
		self.frame.setObjectName(u"frame")
		self.frame.setFrameShape(QFrame.StyledPanel)
		self.frame.setFrameShadow(QFrame.Raised)
		self.horizontalLayout = QHBoxLayout(self.frame)
		self.horizontalLayout.setObjectName(u"horizontalLayout")
		self.frame_3 = QFrame(self.frame)
		self.frame_3.setObjectName(u"frame_3")
		self.frame_3.setFrameShape(QFrame.StyledPanel)
		self.frame_3.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
		self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
		self.tableWidget = QTableWidget(self.frame_3)
		if (self.tableWidget.columnCount() < 3):
			self.tableWidget.setColumnCount(3)
		__qtablewidgetitem = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
		__qtablewidgetitem1 = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
		__qtablewidgetitem2 = QTableWidgetItem()
		self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
		self.tableWidget.setObjectName(u"tableWidget")

		self.horizontalLayout_2.addWidget(self.tableWidget)

		self.horizontalLayout.addWidget(self.frame_3)

		self.frame_2 = QFrame(self.frame)
		self.frame_2.setObjectName(u"frame_2")
		self.frame_2.setFrameShape(QFrame.StyledPanel)
		self.frame_2.setFrameShadow(QFrame.Raised)
		self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
		self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
		self.txt_Resultado = QLabel(self.frame_2)
		self.txt_Resultado.setObjectName(u"txt_Resultado")
		font = QFont()
		font.setPointSize(18)
		font.setItalic(True)
		self.txt_Resultado.setFont(font)

		self.horizontalLayout_3.addWidget(self.txt_Resultado)

		self.horizontalLayout.addWidget(self.frame_2)

		self.verticalLayout.addWidget(self.frame)

		self.btn_Atualizar = QPushButton(self.centralwidget)
		self.btn_Atualizar.setObjectName(u"btn_Atualizar")
		self.btn_Atualizar.setMaximumSize(QSize(200, 16777215))

		self.verticalLayout.addWidget(self.btn_Atualizar, 0, Qt.AlignHCenter)

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QMenuBar(MainWindow)
		self.menubar.setObjectName(u"menubar")
		self.menubar.setGeometry(QRect(0, 0, 472, 22))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QStatusBar(MainWindow)
		self.statusbar.setObjectName(u"statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)

		QMetaObject.connectSlotsByName(MainWindow)

	# setupUi

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
		___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
		___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
		___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
		___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
		___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
		___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"IDADE", None));
		self.txt_Resultado.setText(QCoreApplication.translate("MainWindow", u"RESULTADO:", None))
		self.btn_Atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
	# retranslateUi
