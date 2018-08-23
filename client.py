import socket

class SocketHandler():
	sock = socket.socket()
	def __init__(self):
		self.sock.connect(("CAMP-1CFCB1", 3141))
	def send(self, msg):
		self.sock.send(msg)
	def receive(self):
		chunks = []
		bytes_recd = 0
		chunk = self.sock.recv(2048)	
		chunks.append(chunk)
		bytes_recd = bytes_recd + len(chunk)
		return chunks
		
class PlayingBoard():
	id = -1
	cells = [[0 for x in range(9)] for y in range(9)]
	bigBoard = [[0 for x in range(3)] for y in range(3)]
	activeX = 3
	activeY = 3

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
		board = PlayingBoard()
		board.id = parts[2]
		for i in range(0, 9):
			board.bigBoard[i % 3][i // 3] = parts[4 + i]
		for i in range(0, 81):
			board.cells[i % 9][i // 9] = parts[14 + i]
		board.activeX = parts[96]
		board.activeY = parts[97]
		return board
		
wam = SocketHandler()
#wam.send('Hallo')
msg = wam.receive()
board = ProtocolCoder.parseInfoMessage(msg[0])
print(board.id)
print(board.bigBoard)
print(board.cells)

#https://docs.python.org/3/howto/sockets.html#socket-howto
#https://docs.python.org/3/library/socket.html
#https://docs.python.org/3/library/struct.html
#https://docs.python.org/3/library/index.html
