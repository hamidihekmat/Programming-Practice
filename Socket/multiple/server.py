import socket
import sys
from _thread import *


HOST = '127.0.0.1'
PORT = 8883

clients = []
def broadcast(msg):
    for conn in clients:
        conn.sendall(msg)


def clienthread(conn):
    conn.send(bytes('Welcome to the server!\n', 'utf-8)'))

    while True:
        data = conn.recv(1024)
        broadcast(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(10)
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        start_new_thread(clienthread, (conn,))
