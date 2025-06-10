from threading import *

def display(str):
    for i in str:
        print(i)

l = Semaphore(2) # In semaphore, we can define no.of threads will run at a time.

t1 = Thread(target=display, args=('Mukhesh',))
t2 = Thread(target=display, args=('Talluri',))
t3 = Thread(target=display, args=('Python',))


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()