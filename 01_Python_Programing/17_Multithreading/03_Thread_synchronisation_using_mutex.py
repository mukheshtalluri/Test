from threading import *

def display(str):
    l.acquire()
    for x in str:
        print(x)
    l.release()

l = Lock()
t1 = Thread(target=display, args=('Mukhesh',))
t2 = Thread(target=display, args=('Talluri',))

t1.start()
t2.start()


t1.join()
t2.join()