#Creado por: Juan Carlos Castellón Rivera
#Fecha: 7 de abril del año 2025
#Ejercicio 3 - BusquedaLineal

def MóduloBusquedaLineal(lista, meta):
    for x in range(len(lista)):
        if lista[x] == meta:
            return x
    return -1
