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


    for i in range (n):
        id = int(input(f"Ingrese el id del proceso {i+1}: "))
        nombre = input(f"Ingrese el nombre del proceso {i+1}: ")
        duracion = str(randint(10,100))+'ms'
        proceso = (id, nombre, duracion)
        procesos.append(proceso)
        
    print("\n")

def atender_procesos():
    if procesos:
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
    
def menu():
    while True:
        print("Microprocesador")
        print("1. Agregar procesos a la cola")
        print("2. Atender siguiente proceso")
        print("3. Visualizar procesos en la cola")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_procesos()
        elif opcion == "2":
            atender_procesos()
        elif opcion == "3":
            visualizar_cola()
        elif opcion == "4":
            print("saliendo...")
            break
        else:
            print("intenta de nuevo, opción inválida\n")

menu()
