from threading import *

class Alphabet(Thread):
    def run(self):
        for i in range(65,91):
            print(chr(i))


t = Alphabet()

t.start()
for i in range(65, 91):
    print(i)
t.join()

