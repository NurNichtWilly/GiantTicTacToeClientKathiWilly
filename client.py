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
		return chunks

class ProtocolCoder():
	@staticmethod
	def parseMessage(msg):
		print(msg)
		parts = msg.split(b'\xff')[:-1]
		if b'I' in parts[0]:
			return ProtocolCoder.parseInfoMessage(parts)
		
	@staticmethod
	def parseInfoMessage(parts):
		print(parts)
		infoMessageParsed = {}
		infoMessageParsed['clientId'] = parts[0].decode()
		for i in range(4,12):
			bigBoard[i%9][i//9] = msg[i]
		infoMessageParsed['bigBoard'] = bigBoard
		for i in range(14,95):
			cells[i%9][i//9] = msg[i]
		infoMessageParsed['cells'] = cells
		for i in range(0,1):
			activeField[i] = msg[i+96]
		infoMessageParsed[activeField] = activeField
		print(infoMessageParsed)
wam = SocketHandler()
#wam.send('Hallo')
msg = wam.receive()
ProtocolCoder.parseInfoMessage(msg)
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
