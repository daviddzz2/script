import os
import time
from datetime import datetime

def write_cola(line):
    """Crea un archivo con timestamp único"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"mensaje_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(line)
    return filename

def read_and_delete_cola():
    """Lee el primer archivo mensaje creado y lo elimina"""
    # Obtener lista de archivos de mensaje
    archivos = [f for f in os.listdir(".") if f.startswith("mensaje_") and f.endswith(".txt")]
    
    if not archivos:
        return None
    
    # Ordenar por nombre (que incluye timestamp) para obtener el primero creado
    archivos.sort()
    primer_archivo = archivos[0]
    
    # Leer contenido
    with open(primer_archivo, "r", encoding="utf-8") as file:
        contenido = file.read().strip()
    
    # Eliminar archivo
    os.remove(primer_archivo)
    
    return contenido

def get_cola_size():
    """Retorna la cantidad de archivos de mensaje pendientes"""
    archivos = [f for f in os.listdir(".") if f.startswith("mensaje_") and f.endswith(".txt")]
    return len(archivos)