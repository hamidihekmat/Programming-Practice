import threading
import socket


clients = []

class Server:
    def __init__(self, ADDRESS):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDRESS)
        self.server.listen(5)
        print('Socket has been created on {} with port {}. Waiting for Connection...'.format(ADDRESS[0], ADDRESS[1]))

    def await_connection(self):
        '''
        await for incoming connections
        logs the connection and assign names to connections
        '''
        while True:
            client, addr = self.server.accept()
            print('Connection from: {}'.format(addr))
            clients.append(client)
            thread = threading.Thread(target=self.handle_connections, args=(client,))
            thread.start()
            print(threading.active_count())

    def handle_connections(self, client):
        '''
        handle receiving and sending messages
        '''
        welcome = bytes('Welcome to the chat!')
        client.sendall(welcome)
        while True:
            message = client.recv(1024)
            self.broadcast(message)


    def broadcast(self, message):
        '''
        broadcast messages to other clients
        '''
        for client in clients:
            client.sendall(message)


HOST = '127.0.0.1'
PORT = 8888
ADDRESS = (HOST, PORT)

s = Server(ADDRESS).await_connection()

# left off at client broadcast loop -> needs a fix
