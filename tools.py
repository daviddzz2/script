import os
import time
from datetime import datetime

def write_cola(line):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"mensaje_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(line)
    return filename

def read_and_delete_cola():
    archivos = [f for f in os.listdir(".") if f.startswith("mensaje_") and f.endswith(".txt")]
    
    if not archivos:
        return None
    archivos.sort()
    primer_archivo = archivos[0]
    with open(primer_archivo, "r", encoding="utf-8") as file:
        contenido = file.read().strip()
    os.remove(primer_archivo)
    
    return contenido

def get_cola_size():
    archivos = [f for f in os.listdir(".") if f.startswith("mensaje_") and f.endswith(".txt")]
    return len(archivos)