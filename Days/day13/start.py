
import time
import threading

start = time.perf_counter()


def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


l = []
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    l.append(t)
for thread in l:
    thread.join()


finish = time.perf_counter()


print('Finished in {} second(s)'.format(round(finish - start, 2)))
