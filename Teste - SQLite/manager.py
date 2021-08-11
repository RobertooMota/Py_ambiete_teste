import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

nome = ''
idade = 0

while 1:
	nome = str(input('Digite o Nome: '))
	idade = int(input('Digite a Idade: '))

	cursor.execute(	"""INSERT INTO TABELA (NOME, IDADE) VALUES (?, ?)""", (nome, idade)	)
	conn.commit()
	if str(input('Deseja continuar? ')) in 'Nn':
		conn.close()
		break

	else:
		pass

