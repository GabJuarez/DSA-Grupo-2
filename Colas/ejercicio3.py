"""
Ejercicio #3 - Gestión de turnos en una farmacia
Implemente un sistema de turnos en una farmacia, donde los pacientes son atendidos en el orden en que
llegan. Cada paciente tiene un nombre y un tipo de servicio (compra, consulta, receta). El sistema debe
permitir registrar nuevos pacientes, atender al siguiente en la fila y mostrar los turnos pendientes.
"""

import os
from collections import deque
ColaPacientes = deque()

def LimpiarConsola():
    os.system('cls' if os.name == 'nt' else 'clear')

def AgregarPaciente():
    print("1. Agregar Pacientes")
    Num1 = int(input("\nCuantos pacientes desea agregar: "))

    if Num1 > 0:
        for i in range(Num1):
            ContPacientes = len(ColaPacientes) + 1

            print("\nPaciente No.", ContPacientes)
            Nombre = input("Ingrese el nombre del paciente: ")
            
            print("\nServicios: 1. Compra, 2. Consulta, 3. Receta")

            while True:
                try:
                    NumTipo = int(input("Ingrese el tipo de servicio: "))
                    match NumTipo:
                        case 1:
                            Tipo = "Compra"
                            break
                        case 2:
                            Tipo = "Consulta"
                            break
                        case 3:
                            Tipo = "Receta"
                            break
                        case _:
                            print("\nIngrese un servicio entre 1 a 3...")
                except ValueError:
                    print("\nIngrese un número y servicio entre 1 a 3...")

            Paciente = "No. {0}, Nombre: {1}, Servicio: {2}".format(ContPacientes, Nombre, Tipo)
            ColaPacientes.append(Paciente)
            print("\nPaciente Registrado!")
    
    if Num1 <= 0:
        print("\nIngrese una cantidad correcta de pacientes...\n")

def AtenderPaciente():
    print("2. Atender Pacientes")

    if ColaPacientes:
        Num2 = int(input("\nCuantos pacientes desea atender: "))

        if Num2 > 0:
            for n in range(Num2):
                PacienteAtendido = ColaPacientes.popleft()
                print("Se atendio a", PacienteAtendido)
        print("\nFila actual de Pacientes:")
        for s in ColaPacientes:
            print(s)
        print("\n------------------------------------\n")

        if Num2 <= 0:
            print("\nIngrese una cantidad correcta de pacientes...\n")
    else:
        print("\nNo hay pacientes en la fila...\n")

def MostrarTurnos():
    print("3. Mostrar Turnos Pendientes\n")
    
    if ColaPacientes:
        for p in ColaPacientes:
            print(p)
        print("\n------------------------------------\n")
    else:
        print("\nNo hay pacientes en la fila...\n")

def main():
    print("Bienvenido a la farmacia!")

    while True:
        print("1. Agregar Paciente, 2. Atender Paciente, 3. Mostrar Turnos Pendientes, 4. Salir")

        try:
            opc = int(input("\nSeleccione una opción: "))

            match opc:
                case 1:
                    LimpiarConsola()
                    AgregarPaciente()
                    LimpiarConsola()
                
                case 2:
                    LimpiarConsola()
                    AtenderPaciente()

                case 3:
                    LimpiarConsola()
                    MostrarTurnos()

                case 4:
                    LimpiarConsola()
                    print("\nCerrando Sistema...")
                    break

                case _:
                    LimpiarConsola()
                    print("\nIngrese una opción valida entre 1 a 4...\n")

        except ValueError:
            LimpiarConsola()
            print("\nIngrese un número y una opción valida entre 1 a 4...\n")

main()
