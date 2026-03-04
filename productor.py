import time
import os
from tools import write_cola

print(f"Productor iniciado en el proceso {os.getpid()}")

contador = 0
while True:
    time.sleep(2)
    contador += 1
    
    mensaje = f"Mensaje {contador}: Hola desde el productor"
    print(f"[PRODUCTOR] Escribiendo: {mensaje}")
    
    write_cola(mensaje)
    
    with open("cola.txt", "r", encoding="utf-8") as f:
        tamaño = len(f.readlines())
    print(f"[PRODUCTOR] Tamaño de cola actual: {tamaño}")
