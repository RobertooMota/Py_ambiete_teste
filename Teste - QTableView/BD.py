import sqlite3
from ui_table import *

class BDados:
	def __int__(self):
		pass

	def AtualizarBD(self):
		dados = sqlite3.connect('bd.db')
		banco = dados.cursor()
		banco.execute("""SELECT * FROM TABELA""")
		informacoes = banco.fetchall()
		return informacoes

	def ExibirAlerta(self):
		msg = QMessageBox(QMessageBox.Information, 'Atenção', 'Informações Exibidas')
		msg.exec()