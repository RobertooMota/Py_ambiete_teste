from ui_interface import *
import sys


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)
		self.setWindowTitle('Exemplo de lista')
		self.interface.btn_AdicionarItem.clicked.connect(lambda: MainWindow.AdicionarItem(self))
		self.interface.btn_Atualizar.clicked.connect(lambda: MainWindow.AtualizarItem(self))
		self.interface.lst_Itens.itemDoubleClicked.connect(lambda: MainWindow.AtualizarItem(self))

		self.show()

	def AdicionarItem(self):
		self.interface.lst_Itens.addItem(self.interface.txt_Nome.text())
		self.interface.txt_Nome.clear()
		self.interface.txt_Nome.setFocus()

	def AtualizarItem(self):
		try:
			self.interface.txt_Selecionado.setText(self.interface.lst_Itens.currentItem().text())
		except:
			self.interface.txt_Selecionado.setText('Nada selecionado!')
if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	sys.exit(app.exec())
