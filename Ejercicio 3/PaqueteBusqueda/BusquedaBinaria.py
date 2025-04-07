#Creado por: Juan Carlos Castellón Rivera
#Fecha: 7 de abril del año 2025
#Ejercicio 3 - BusquedaBinaria

def MóduloBusquedaBinaria(lista, meta):
    izq, der = 0, len(lista) - 1
    while izq <= der:
        cen = izq + (der - izq) // 2

        if lista[cen] == meta:
            return cen

        elif lista[cen] < meta:
            izq = cen + 1

        else:
            der = cen - 1

    return -1
