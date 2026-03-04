import os

def write_cola(line):
    fila_name = "cola.txt"
    with open(fila_name, "a", encoding="utf-8") as file:
        file.write(line + "\n")

def read_and_delete_cola():
    fila_name = "cola.txt"
    
    if not os.path.exists(fila_name):
        return None
    
    with open(fila_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    if not lines:
        return None
    
    first_line = lines[0].strip()
    
    with open(fila_name, "w", encoding="utf-8") as file:
        file.writelines(lines[1:])
    
    return first_line

def get_cola_size():
    fila_name = "cola.txt"
    
    if not os.path.exists(fila_name):
        return 0
    
    with open(fila_name, "r", encoding="utf-8") as file:
        return len(file.readlines())