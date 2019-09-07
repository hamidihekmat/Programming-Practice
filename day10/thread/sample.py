import threading


def myTask():
    print('Hello World', threading.current_thread())

myThread = threading.Thread(target=myTask)
myThread.start()
