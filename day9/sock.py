
import socket
import sys

HOST = "172.217.1.3"
PORT = 80

# message for google ->  "GET / HTTP 1.1"
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = "GET / HTTP/1.1\r\n\r\n"
        s.sendall(message.encode())
        reply = s.recv(4096)
        print(reply.decode('utf-8'))

except:
    print('Failed to connect!')
    sys.exit()

print('Socket Created')
