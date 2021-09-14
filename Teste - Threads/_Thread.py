from threading import Thread
from time import sleep

Status = True

def MyTH():
	while 1:
		global Status
		if not Status:
			Status = True
			break
		MyThread.count += 1
		print(MyThread.count)
		sleep(1)

def StopTH(value):
	global Status
	Status = value

class MyThread (Thread):
	count = 0
	def __int__(self):
		Thread.__init__(self)




	def run(self):
		while True:
			global Status
			if not Status:
				break
			MyThread.count += 1
			print(MyThread.count)
			sleep(1)


