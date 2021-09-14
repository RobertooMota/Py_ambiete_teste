from threading import Thread
from time import sleep
from main import *

Status = True


class TH(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)



	def MyTH(self):
		count = 0
		while 1:
			global Status
			if not Status:
				Status = True
				break
			count += 1
			print(count)

			sleep(1)

	def StartTH(self):
		th = Thread(target=self.MyTH)
		th.start()

	def StopTH(self, value):
		global Status
		Status = value
