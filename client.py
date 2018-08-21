import socket

class SocketHandler():
	sock = socket.socket()
	def __init__(self):
		self.sock.connect(("CAMP-2ABE89", 3141))
		
	def mysend(self, msg):
		totalsent = 0
		while totalsent < msg.len(str):
			sent = self.sock.send(msg[totalsent:])
			if sent == 0:
				raise RuntimeError("socket connection broken")
			totalsent = totalsent + sent
		
wam = SocketHandler()
print(socket.gethostname())
wam.mysend("hallo".encode("UTF-8"))
print("done")




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
