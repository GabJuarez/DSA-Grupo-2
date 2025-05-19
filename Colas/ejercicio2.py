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

def atender_llamadas():
    if not agentes_disponibles:
        print("No hay agentes disponibles en este momento.\n")
        return
    if llamadas:
        llamada = llamadas.popleft()
        agente = agentes_disponibles.pop(0)
        print(f"La llamada de: {llamada[0]}, con el motivo: {llamada[1]} está siendo atendida por el agente {agente}")
        input("Presione Enter cuando el agente termine la llamada...")
        agentes_disponibles.append(agente)
        print(f"El agente {agente} ahora está disponible.\n")
    else:
        print("No hay llamadas en la cola para atender\n")

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
        print("2. Atender siguiente llamada")
        print("3. Visualizar llamadas en la cola")
        print("4. Visualizar agentes disponibles")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_llamada()
        elif opcion == "2":
            atender_llamadas()
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
