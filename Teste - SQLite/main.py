import sqlite3
from ui_main import *
import sys


coluns = 3


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)
		self.interface.btn_Atualizar.clicked.connect(self.atualizar)
		self.show()

	def atualizar(self):
		BD = sqlite3.connect('bd.db')
		cursor = BD.cursor()
		cursor.execute("""SELECT * FROM TABELA""")
		informacoes = cursor.fetchall()
		self.interface.tableWidget.setRowCount(len(informacoes))
		self.interface.tableWidget.setColumnCount(coluns)

		for r in range(0, len(informacoes)):
			for c in range(0, coluns):
				self.interface.tableWidget.setItem(r, c, QTableWidgetItem(str(informacoes[r][c])))

		cursor.execute("""SELECT NOME FROM TABELA WHERE IDADE > ?""", (30,))
		nome = cursor.fetchall()
		print(f'Foram encontradas {len(nome)} com 30 anos de idade.')
		for r in range(0, len(nome)):
			for c in range(0, 1):
				print(f'Nome: {nome[r][c]}')
		self.interface.txt_Resultado.setText(nome[0][0])

		BD.close()

		self.show()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	sys.exit(app.exec())
