import time
import os
from tools import write_cola, get_cola_size

print(f"Productor iniciado en el proceso {os.getpid()}")

contador = 0
while True:
    time.sleep(2)
    contador += 1
    
    mensaje = f"Mensaje {contador}: Hola desde el productor"
    print(f"[PRODUCTOR] Escribiendo: {mensaje}")
    
    archivo = write_cola(mensaje)
    print(f"[PRODUCTOR] Archivo creado: {archivo}")
    
    tamaño = get_cola_size()
    print(f"[PRODUCTOR] Cantidad de mensajes en cola: {tamaño}")
