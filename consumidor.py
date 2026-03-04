import time
import os
from tools import read_and_delete_cola

print(f"Consumidor iniciado en el proceso {os.getpid()}")

while True:
    time.sleep(1)
    
    linea = read_and_delete_cola()
    
    if linea:
        print(f"[CONSUMIDOR] Consumido: {linea}")
        time.sleep(0.5)
    else:
        print(f"[CONSUMIDOR] Cola vacía, esperando...")
    
    if os.path.exists("cola.txt"):
        with open("cola.txt", "r", encoding="utf-8") as f:
            tamaño = len(f.readlines())
        print(f"[CONSUMIDOR] Tamaño de cola actual: {tamaño}\n")
