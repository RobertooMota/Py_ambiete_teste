class Teste1:
	def __int__(self, a=100, b=200):
		self.valorA = a
		self.valorB = b


class TesteValores(Teste1):
	def __init__(self, x=10, y=20):
		TesteValores.__int__(self)
		self.valorX = x
		self.valorY = y


obj = TesteValores()
print(f'ValorX: {obj.valorX}   ValorY: {obj.valorY}   ValorA: {obj.valorA}   ValorB: {obj.valorB}   ')
