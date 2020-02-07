import threading
import time
import logging
from tiempo import Contador
import clasesYfunciones 


logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

# la función para usar para el thread
def dormir(segs):
    time.sleep(segs)

cont=Contador()
cont.iniciar()
lista=[]

for i in range(10):
    #crear un thead
    thread=threading.Thread(target=dormir,args=[1.5])
    #lanzarlo
    thread.start()
    lista.append(thread)
    thread.join()
for thread in lista:
    thread.join()

cont.finalizar()
cont.imprimir()

