

import socket
import sys


host = '127.0.0.1'
port = 8888
addr = (host, port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(addr)
    s.listen(10)
    print('Socket is ready!')
    conn, address = s.accept()
    print('Connected with {} + {}'.format(address[0], address[1]))
