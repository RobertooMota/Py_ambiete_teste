import sys
from BD import BDados
from ui_table import *


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.interface = Ui_MainWindow()
		self.interface.setupUi(self)

		# Chama a função quando clicado no botão
		self.interface.btn_Atualizar.clicked.connect(lambda: MainWindow.Atualizar(self))
		self.show()

	def Atualizar(self):
		# Cria uma instancia com o Banco de dados
		informacoes = BDados()
		retornoInfo = informacoes.AtualizarBD()

		# Cria um objeto do tipo QStandardItemModel -> necessario para o QTableView
		# Nome do objeto = Função(quantidade de informacao, Colunas)
		model = QStandardItemModel(len(informacoes.AtualizarBD()), 3)

		# Seta Nome das colunas
		model.setHorizontalHeaderLabels(['ID', 'Nome', 'Idade'])

		# Laço para armazenar o formato de colunas e informações dentro do objeto MODEL
		for r, info in enumerate(informacoes.AtualizarBD()):
			for colum, item in enumerate(info):
				if type(item):
					item = str(item)
				elemento = QStandardItem(item)  # OBS: Somente Strings!!!!!

				# Armazena dentro do objeto informação (LINHA da info, Coluna da info, info)
				model.setItem(r, colum, elemento)

		# Coloca dentro da tableView criada as informações que estao armazenadas em MODEL
		self.interface.tbl_Lista.setModel(model)

		# Permite alterar o tamanho das colunas
		self.interface.tbl_Lista.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

		# Seta a ultima coluna para ocupar todo espaco presente
		self.interface.tbl_Lista.horizontalHeader().setStretchLastSection(True)

		# Remove o indice da tabela padrao (1, 2, 3, ...)
		self.interface.tbl_Lista.verticalHeader().setVisible(False)

		# Bloqueia a opção de EDIÇÃO
		self.interface.tbl_Lista.setEditTriggers(QAbstractItemView.NoEditTriggers)

		informacoes.ExibirAlerta()
		print(retornoInfo)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	janela = MainWindow()
	app.exit(app.exec())
