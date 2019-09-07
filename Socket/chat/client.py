import socket




HOST = '127.0.0.1'
PORT = 8888
ADDRESS = (HOST, PORT)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(ADDRESS)
    while True:
        message = s.recv(1024)
        send = bytes('This is broadcast testing!', 'utf-8')
        s.sendall(send)
        print(message.decode('utf-8'))
