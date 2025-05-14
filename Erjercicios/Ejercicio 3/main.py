#Creado por: Juan Carlos Castellón Rivera
#Fecha: 7 de abril del año 2025
#Ejercicio 3 - main.py

from PaqueteBusqueda import MóduloBusquedaLineal as BusquedaLineal
from PaqueteBusqueda import MóduloBusquedaBinaria as BusquedaBinaria

Elementos = []

while True:
    try:
        CantElement = int(input('Ingrese la cantidad de números enteros a ingresar: '))
        if CantElement < 1:
            print('')
            print('Ingrese una cantidad mayor a 0')
            print('')
        else:
            break
    except ValueError:
        print('')
        print('Ingrese un valor correcto')
        print('')

print('')
for x in range(CantElement):
    while True:
        try:
            Elemento = int(input('Ingrese el número entero: '))
            Elementos.append(Elemento)
            break
        except ValueError:
            print('')
            print('Ingrese un número válido.')
            print('')

print('')
ElementBus = int(input('Ingrese el elemento que desea buscar: '))

print('')
print('Busqueda Lineal')
PosLineal = BusquedaLineal(Elementos, ElementBus)
if PosLineal != -1:
    print('El elemento', ElementBus, 'está en la posición:', PosLineal)
else:
    print('El elemento no fue encontrado')

ElementosOrdenados = sorted(Elementos)

print('')
print('Busqueda Binaria')
PosBinaria = BusquedaBinaria(ElementosOrdenados, ElementBus)
if PosBinaria != -1:
    print('El elemento', ElementBus, 'está en la posición:', PosBinaria)
else:
    print('El elemento no fue encontrado')

print('')
input('Presione Enter para cerrar el programa')
