"""#2: Gestión de llamadas en un centro de atención al cliente
Cree un sistema que simule la atención de llamadas en un Call Center. 
Cada llamada debe ingresar a una cola con datos como el nombre del cliente
y el motivo de la llamada. A medida que los agentes estén disponibles, se
debe atender al siguiente cliente en orden de llegada.
"""
from collections import deque


llamadas = deque()

def agregar_llamada():
    n = int(input("Ingrese el número de llamadas a agregar a la cola: "))


    for i in range (n):
        nombre = input(f"Ingrese el nombre cliente {i+1}: ")
        motivo = input(f"Inngrese el motivo de la llamda: ")
        llamada =  (nombre, motivo)
        llamadas.append(llamada)
        print("\n")


def atender_llamadas():
    if llamadas:
        llamada = llamadas.popleft()
        print(f"La llamada de: {llamada[0]}, con el motivo: {llamada[1]} ha sido atendido")
    else:
        print("No hay llamadas en la cola para atender")
    print("\n")


def visualizar_cola():
    print("Llamadas en la cola: ")
    if llamadas:
        for i, llamada in enumerate(llamadas, start = 1):
            print(f"Llamada {i}: Cliente: {llamada[0]}, Motivo: {llamada[1]}")
    else:
        print("No hay llamadas en la cola para atender")
    print("\n")
    

def menu():
    while True:
        print("Menú call center")
        print("1. Agregar llamadas a la cola")
        print("2. Atender siguiente llamada")
        print("3. Visualizar llamadas en la cola")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_llamada()
        elif opcion == "2":
            atender_llamadas()
        elif opcion == "3":
            visualizar_cola()
        elif opcion == "4":
            print("saliendo...")
            break
        else:
            print("intenta de nuevo, opción inválida\n")

menu()
