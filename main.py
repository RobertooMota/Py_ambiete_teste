import sys

import ui
from ui import *
from functions import *


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)
		self.interface.btn_botao.clicked.connect(lambda: Ui_Functions.valores(self))


		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	sys.exit(app.exec())
