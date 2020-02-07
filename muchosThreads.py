import threading
import time
import logging
from tiempo import Contador
import clasesYfunciones 


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir():
    time.sleep(1)

cont=Contador()
cont.iniciar()
lista=[]
for i in range(10):
    #crear un thead
    thread=threading.Thread(target=dormir)
    #lanzarlo
    thread.start()
    lista.append(thread)
    thread.join()
cont.finalizar()
cont.imprimir()