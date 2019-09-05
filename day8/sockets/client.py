
import socket


HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    l = input('Type here: ')
    s.sendall(l.encode('ASCII'))
    data = s.recv(1024)

print('Received', data.decode('utf-8'))
