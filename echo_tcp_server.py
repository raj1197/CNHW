import socketserver
SECRET_CODE = "SECRET"

class MyTCPHandler(socketserver.BaseRequestHandler):

    def get_number_count(self, message):
        number_value = ""
        for ch in message:
            if ch >= '0' and ch <= '9':
                number_value = number_value + ch
        return number_value, len(number_value)

    def handle(self):
        self.data = str(self.request.recv(10000), "utf-8")

        print("Client sent: " + self.data)
        send_message = ""
        if SECRET_CODE not in self.data:
            send_message = "Secret code not found."
        else:
            num, cnt = self.get_number_count(self.data)
            send_message = "Digits: " + num + " Count: " + str(cnt)

        self.request.sendall(bytes(send_message, "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()