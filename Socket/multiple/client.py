import socket
import sys



HOST = '127.0.0.1'
PORT = 8883

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    while True:
        msg = s.recv(1024)
        print(msg.decode())
        data = input('Enter message: ')
        s.sendall(data.encode())
