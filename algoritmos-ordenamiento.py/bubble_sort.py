'''
Ejercicio 2: 
Diseñe un modulo independiente que contenga implementaciones de algoritmos de ordenamiento simples (bubble sort)
Invoque los metodos del modulo para ordenar una lista de numeros
•	[ ] Se ha creado un módulo independiente para los algoritmos de ordenamiento.
•	[ ] El módulo contiene una implementación funcional de bubble sort.
•	[ ] Se invoca correctamente el método del módulo para ordenar una lista de números.
•	[ ] El código es eficiente y está bien estructurado
'''

def input_list():
    list = []
    seq = int(input('Cuantos numeros desea agregar: '))
    for i in range(seq):
        x = int(input('Ingrese un numero: '))
        list.append(x)
    return list

def bubble(list): 
    indexing_len = len(list) - 1 
    sorted = False 
    
    while not sorted: 
        sorted = True
        for i in range(0, indexing_len):
            if list[i] > list[i + 1]: 
                sorted = False
                list[i], list[i + 1] = list[i + 1], list[i]
    return list
    
lista = input_list()
print(f'Lista desordenada: {lista}')
print(f'Lista ordenada: {bubble(lista)}')
