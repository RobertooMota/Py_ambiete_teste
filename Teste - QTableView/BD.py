import sqlite3


class BD:
	def AtualizarBD(self):
		dados = sqlite3.connect('bd.db')
		banco = dados.cursor()
		banco.execute("""SELECT * FROM TABELA""")
		informacoes = banco.fetchall()
		return informacoes
