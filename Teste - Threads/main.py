from ui_GUI import *
import sys
from _Thread import *

Status = True


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.TH = MyThread()
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)

		self.interface.btn_Acao.clicked.connect(lambda: self.Iniciar())
		self.interface.btn_Parar.clicked.connect(lambda: self.Parar())

		self.show()

	def Iniciar(self):
		TH = Thread(target=MyTH)
		TH.start()

	def Parar(self):
		StopTH(False)
		sys.exit()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	app.exit(app.exec())
