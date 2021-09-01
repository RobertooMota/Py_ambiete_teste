"""
Classmethod cria um objeto atravez de uma funcao na maioria das vzs usando variaveis da funcao e não
do objeto instanciado
"""


class Carro:
	tipo = 'Terrestre'

	def __init__(self, quantRodas, cor, velMax, tipoDirecao):
		self.quantRodas = quantRodas
		self.cor = cor
		self.velMax = velMax
		self.tipoDirecao = tipoDirecao

	def _quantRodas(self):
		print(self.quantRodas)

	def _cor(self):
		print(self.cor)

	def _velMax(self):
		print(self.velMax)

	def _tipoDirecao(self):
		print(self.tipoDirecao)

	@classmethod
	def porTipo(cls, quantRodas, cor):
		return cls(quantRodas, cor, 200, cls.tipo)


K = Carro.porTipo(5, 'azul')
print(f'********{"GOL"}*********')
K._quantRodas()
K._cor()
K._velMax()
K._tipoDirecao()

Gol = Carro(5, 'Branco', 200, 'Hidraulica')
Palio = Carro(4, 'Azul', 189, 'Mecanico')
print(f'********{"GOL"}*********')
Gol._quantRodas()
Gol._cor()
Gol._velMax()
Gol._tipoDirecao()
print(Gol.tipo)

print(f'********{"Palio"}*********')
Palio._quantRodas()
Palio._cor()
Palio._velMax()
Palio._tipoDirecao()
print(Palio.tipo)
