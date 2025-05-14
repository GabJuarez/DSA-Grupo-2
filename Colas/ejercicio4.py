"""#4: Simulación de atención de procesos por el microprocesador
Diseñe un programa que simule cómo un microprocesador atiende procesos 
en una cola de ejecución. Cada proceso tiene un identificador, un nombre
y una duración estimada en milisegundos. A medida que el procesador queda
libre, atiende al siguiente proceso en orden de llegada (FIFO - First In, First Out).
El sistema debe permitir agregar procesos a la cola, mostrar el proceso en ejecución y
visualizar los procesos pendientes.
"""

from collections import deque
from random import randint

procesos = deque()

def registrar_procesos():
    n = int(input("Ingrese el número de procesos a atender: "))

    id = 1
    for i in range (n):
        nombre = input(f"Ingrese el nombre del proceso {i+1}: ")
        duracion = str(randint(10,100))+'ms'
        proceso = (id, nombre, duracion)
        procesos.append(proceso)
        id += 1
    print("\n")

def atender_procesos():
    n = int(input("Ingrese el número de procesos que van a ser atendidos: "))
    if procesos:
        for i in range (n):
            proceso = procesos.popleft()
            print(f"El proceso {proceso[1]}, con identificador {proceso[0]} ha sido atendido")
    else:
        print("No hay procesos en la cola para atender")
    print("\n")


def visualizar_cola():
    print("Procesos en la cola")
    if procesos:
        for i, proceso in enumerate(procesos, start = 1):
            print(f"Proceso {i}: Id:{proceso[0]}, Nombre: {proceso[1],} Duración aproximada: {proceso[2]} ")
    else:
        print("No hay procesos en la cola para atender")
    print("\n")
    
registrar_procesos()
visualizar_cola()
atender_procesos()
visualizar_cola()
