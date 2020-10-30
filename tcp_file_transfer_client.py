import socket
import sys

HOST, PORT = "localhost", 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect((HOST, PORT))
	filename = 'sample_file.txt'
	f = open(filename,'rb')
	data = f.readline()
	while(data):
		sock.sendall(data)
		data = f.readline()
	print('Data sent')
	sock.close()
	print('Connection Closed')