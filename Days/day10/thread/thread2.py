import threading
import time



def thread_func2(name):
    while True:
        print('Thread %s is starting!' % name)
        time.sleep(3)
        print('Thread %s is finished!' % name)

def thread_func(name):
    print('Thread %s is starting!' % name)
    time.sleep(3)
    print('Thread %s is finished!' % name)




if __name__ == '__main__':
    thread_l = []
    for i in range(100):
        thread_l.append(threading.Thread(target=thread_func, args=(i,)))

    for t in thread_l:
        t.start()
    x = threading.Thread(target=thread_func2, args=('L-1',))
    x.start()

    print('Main is finished')
