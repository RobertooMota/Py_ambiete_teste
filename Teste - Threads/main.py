from ui_GUI import *
import sys
from _Thread import *


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)

		self.TH = TH()

		self.interface.btn_Acao.clicked.connect(lambda: self.Iniciar())
		self.interface.btn_Parar.clicked.connect(lambda: self.Parar())
		self.interface.btn_Sair.clicked.connect(lambda: self.Sair())

		self.show()

	def Iniciar(self):
		self.TH.StartTH()

	def Parar(self):
		self.TH.StopTH(False)

	def Sair(self):
		self.Parar()
		sys.exit()

	def contador(self, valor):
		self.interface.txt_Secundaria.setText(str(valor))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	app.exit(app.exec())
