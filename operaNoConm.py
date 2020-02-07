import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)



var=10
lock=threading.Lock()#los threads se esperan entre si,se sincronizan

def sumarUno():
    global var
    global lock
    try:
        lock.acquire()
        var+=1
    finally:
        #lock.release()
        pass


def multiplicarPorDos():
    global var
    global lock
    try:
        lock.acquire()
        var*=2
    finally:
        lock.release()

    

thread1=threading.Thread(target=sumarUno)
thread2=threading.Thread(target=multiplicarPorDos)

thread1.start()
#thread1.join()
thread2.start()
#thread2.join()

logging.info(var)