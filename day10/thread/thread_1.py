import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s starting", name)
    time.sleep(2)
    logging.info("Thread %s finishing", name)

if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt='%HL%M:%S')
    logging.info("Main    :   before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    :    before running thread")
    x.start()
    t = threading.Thread(target=thread_function, args=(2,))
    t.start()
    x.join()
    t.join()
    logging.info("Main  :    wait for the thread to finish")
    logging.info("All done!")
