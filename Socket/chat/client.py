import socket
import threading

class Client:

    def __init__(self, ADDRESS):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(ADDRESS)


    def receive_message(self):
        '''
        Constantly receive message and print to console
        '''
        while True:
            message = self.server.recv(1024)
            print(threading.active_count())
            print(message.decode('utf-8'))

    def send_message(self):
        '''
        constantly send messages
        '''
        while True:
            message = bytes(input(''), 'utf-8')
            self.server.send(message)

    def start(self):
        thread1 = threading.Thread(target=self.receive_message)
        thread1.start()
        thread2 = threading.Thread(target=self.send_message)
        thread2.start()


HOST = '23.96.14.40'
PORT = 8888
ADDRESS = (HOST, PORT)

client = Client(ADDRESS).start()
