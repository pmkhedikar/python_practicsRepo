from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('Printing Hello')
            sleep(0.2)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('Printing Hi')
            sleep(0.2)

t1 = Hello()
t2 = Hi()
t1.start()
sleep(0.1)
t2.start()
t1.join()
t2.join()   #Bye will print after finishing t1 & t2 Thread

print('Bye')