import socketserver

class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
    	filename = 'server_file.txt'
    	f = open(filename, 'wb')
    	self.data = self.rfile.readline()
    	while self.data:
    		f.write(self.data)
    		self.data = self.rfile.readline()
    	f.close()
    	print('Successfully written the file')


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.handle_request()
    
    print('Connection closed')