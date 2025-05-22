from concurrent.futures import ThreadPoolExecutor, as_completed
from random import randint
from time import sleep
from collections import deque

llamadas = deque()
agentes_disponibles = ["Ana", "Luis", "Carlos", "Sofía"]

def agregar_llamada():
    n = int(input("Ingrese el número de llamadas a agregar a la cola: "))
    for i in range(n):
        nombre = input(f"Ingrese el nombre cliente {i+1}: ")
        motivo = input(f"Ingrese el motivo de la llamada: ")
        llamada = (nombre, motivo)
        llamadas.append(llamada)
        print("\n")

def atender_llamada(agente, llamada):
    print(f"{agente} está atendiendo la llamada de {llamada[0]} (Motivo: {llamada[1]})")
    duracion = randint(2,6)# simula duración entre 2 y 6 segundos
    sleep(duracion)
    print(f"{agente} terminó de atender a {llamada[0]} (Duración: {duracion}s)")
    return agente

def despachar_llamadas():
    while llamadas:  # mientras haya llamadas en la cola
        tareas = []
        agentes_en_servicio = []
        
    # Usamos el ThreadPoolExecutor con la cantidad actual de agentesn  disponibles
        with ThreadPoolExecutor(max_workers=len(agentes_disponibles)) as executor:
            # asignamos llamadas a todos los agentes disponibles
            while llamadas and agentes_disponibles:
                agente = agentes_disponibles.pop(0)
                llamada = llamadas.popleft()
                tarea = executor.submit(atender_llamada, agente, llamada)
                tareas.append(tarea)
                agentes_en_servicio.append(agente)
            
            # esperamos que todos terminen y devolvemos los agentes disponibles
            for future in as_completed(tareas):
                agente_que_vuelve = future.result()
                agentes_disponibles.append(agente_que_vuelve)
        
        #aqui el ciclo vuelve a evaluar si quedan llamadas y repite el proceso automáticamente
    print("Todas las llamadas han sido atendidas.\n")


def visualizar_cola():
    print("Llamadas en la cola: ")
    if llamadas:
        for i, llamada in enumerate(llamadas, start=1):
            print(f"Llamada {i}: Cliente: {llamada[0]}, Motivo: {llamada[1]}")
    else:
        print("No hay llamadas en la cola para atender")
    print("\n")

def visualizar_agentes():
    print("Agentes disponibles:")
    if agentes_disponibles:
        for agente in agentes_disponibles:
            print(f"- {agente}")
    else:
        print("No hay agentes disponibles en este momento.")
    print("\n")

def menu():
    while True:
        print("Menú call center")
        print("1. Agregar llamadas a la cola")
        print("2. Atender llamadas (simulación automática)")
        print("3. Visualizar llamadas en la cola")
        print("4. Visualizar agentes disponibles")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_llamada()
        elif opcion == "2":
            despachar_llamadas()
        elif opcion == "3":
            visualizar_cola()
        elif opcion == "4":
            visualizar_agentes()
        elif opcion == "5":
            print("saliendo...")
            break
        else:
            print("intenta de nuevo, opción inválida\n")

menu()