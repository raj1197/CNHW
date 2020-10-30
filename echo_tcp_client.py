import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    sock.sendall(bytes(data, "utf-8"))
    print("Sent:     " + data)

    received = str(sock.recv(10000), "utf-8")
    print("Received: " + received)