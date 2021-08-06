import main
from main import *
from time import sleep

contador = 0


class Ui_Functions(MainWindow):
	def valores(self):
		global contador
		print(self.interface.txt_input.text())
		sleep(2)
		self.interface.txt_input.clear()
		self.interface.txt_input.setText(str(contador))
		contador += 1
