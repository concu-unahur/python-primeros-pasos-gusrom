import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)



var=10
sema=threading.Semaphore(0)#los threads se esperan entre si,se sincronizan

def sumarUno():
    global var
    try:
        
        var+=1
    finally:
        sema.release()
        #pass


def multiplicarPorDos():
    global var
    global lock
    try:
        sema.acquire()
        var*=2
    finally:
        sema.release()

    

t1=threading.Thread(target=sumarUno)
t2=threading.Thread(target=multiplicarPorDos)

sema.acquire()
t1.start()
#t1.join()
t2.start()
t2.join()

logging.info(var)