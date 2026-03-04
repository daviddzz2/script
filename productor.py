import time
import os
from tools import write_cola, get_cola_size

print(f"Productor iniciado en el proceso {os.getpid()}")

while True:
    time.sleep(2)
    
    mensaje = "Paco,20.Buenos dias"
    print(f"[PRODUCTOR] Escribiendo: {mensaje}")
    
    archivo = write_cola(mensaje)
    print(f"[PRODUCTOR] Archivo creado: {archivo}")
    
    tamaño = get_cola_size()
    print(f"[PRODUCTOR] Cantidad de mensajes en cola: {tamaño}")
