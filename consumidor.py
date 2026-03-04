import time
import os
from tools import read_and_delete_cola, get_cola_size

print(f"Consumidor iniciado en el proceso {os.getpid()}")

while True:
    time.sleep(1)
    
    linea = read_and_delete_cola()
    
    if linea:
        print(f"[CONSUMIDOR] Consumido: {linea}")
        time.sleep(0.5)
    else:
        print(f"[CONSUMIDOR] Cola vacía, esperando...")
    
    tamaño = get_cola_size()
    print(f"[CONSUMIDOR] Cantidad de mensajes en cola: {tamaño}\n")
