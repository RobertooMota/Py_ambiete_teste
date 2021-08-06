from ui import *
from ui_Main import *
import sys


class MainWindow(QMainWindow):
	def __init__(self):
		print('Iniciou a 1')
		QMainWindow.__init__(self)
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)
		self.interface.btn_Goto.clicked.connect(lambda:funcoes.goto2(self))
		self.show()



class SecWindow(QMainWindow):
	def __init__(self):
		print('Iniciou a 2')
		QMainWindow.__init__(self)
		self.interface2 = Ui_SecWindow()
		self.interface2.setupUi(self)
		self.interface2.btn_Goto.clicked.connect(lambda: funcoes.goto1(self))



class funcoes(MainWindow, SecWindow):
	def goto1(obj):
		print('goto1')
		obj.jan1 = MainWindow()
		obj.jan1.show()
		obj.hide()

	def goto2(self):
		print('goto2')
		self.jan2 = SecWindow()
		self.jan2.show()
		self.hide()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	sys.exit(app.exec())
