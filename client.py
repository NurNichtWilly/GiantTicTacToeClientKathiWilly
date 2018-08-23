import socket

class SocketHandler():
	sock = socket.socket()
	def __init__(self):
		self.sock.connect(("CAMP-2ABE5C", 3141))
	def send(self, msg):
		self.sock.send(msg)
	def receive(self):
		chunks = []
		bytes_recd = 0
		chunk = self.sock.recv(2048)	
		chunks.append(chunk)
		bytes_recd = bytes_recd + len(chunk)
		return b''.join(chunks)

class ProtocolCoder():
	@staticmethod
	def parseMessage(msg):
		parts = msg.split(b'\xff')[:-1]
		if b'I' in parts[0]:
			return ProtocolCoder.parseInfoMessage(parts)
		
	@staticmethod
	def parseInfoMessage(parts):
		print('parts:')
		print(parts)
		infoMessageParsed = {}
		infoMessageParsed['id'] = parts[0].decode()
		infoMessageParsed['clientId'] = ord(parts[1])
		bigBoard = [['_'] * 3 for i in range(3)]
		cells = [['_'] * 9 for i in range(9)]
		for i in range(9):
			bigBoard[i%3][i//3] = parts[2][i]
		infoMessageParsed['bigBoard'] = bigBoard
		for i in range(81):
			cells[i%9][i//9] = parts[3][i]
		infoMessageParsed['cells'] = cells
		infoMessageParsed['activeField'] = (ord(parts[4][0]), ord(parts[4][1]))
		print(infoMessageParsed)
wam = SocketHandler()
#wam.send('Hallo')
msg = wam.receive()
ProtocolCoder.parseMessage(msg)
print(msg)
print(socket.gethostname())




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
