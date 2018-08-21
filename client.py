
<<<<<<< HEAD
class SocketHandler():
	sock = socket.socket()
	def __init__(self):
		self.sock.connect(("localhost", 3141))
	#def connect(self, host, port):
        #sock.connect((host, port))
	def send(self, msg):
		self.sock.send(msg)
wam = SocketHandler()
wam.send('Hallo')
print(socket.gethostname())
=======



>>>>>>> ef47596c8566bedb70990892818f4f31ff314838
# class Wsdf():
	# x = 5
	
	# def __init__(self):
		# # konstruktor
	
	# @staticmethod
	# def __str__():
	
	# def yxcv(self, bar):
		# return bar
	
	# def qwer(self, foo):
		# self.x = 5
		# test = self.yxcv(self.x)
		# return (test, foo)
		

# uiae = asdf()
# print(uiae)
# x, y = uiae.qwer("uio")

# s = socket.socket(socket.AF_INET, socket.SOCK_DATAGRAM)
# socket.recv
# socket.send

# 'test\x00string'.encode('utf-8')

# if __name__ == '__main__':
	# pass

	
	
	
#https://docs.python.org/3/howto/sockets.html#socket-howto
#https://docs.python.org/3/library/socket.html
#https://docs.python.org/3/library/struct.html
#https://docs.python.org/3/library/index.html
