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
    list = [] # Definimos una lista vacia donde guardaremos los numeros 
    try: # Usamos el bloque try para manejar los errores
        seq = int(input('Cuantos numeros desea agregar: '))
        if seq <= 0: # Aqui usamos un condicional para ver si la secuencia es menor o igual a 0. Mandarlo al bloque except ValueError
            raise ValueError
        elif isinstance(seq, float or str): # Aqui usamos isinstance para ver si la secuencia es un float o un string. Mandarlo al bloque except TypeError
            raise TypeError
    except TypeError as e:  # Si se lanza un TypeError, se ejecuta este bloque
        print(f'Error: {e}')
        print('Por favor ingrese un numero valido (enteros).')
        return input_list() # Aqui volvemos a llamar a la funcion input_list para que el usuario vuelva a ingresar la secuencia
    except ValueError as e: # Repetimos el proceso que el anterior except
        print(f'Error: {e}')
        print('Por favor ingrese un numero valido (enteros).')
        return input_list()
    except Exception as e: # Si se lanza un error diferente, se ejecuta este bloque
        print(f'Error: {e}')
        print('Ocurrio un error inesperado.')
        return input_list() 
    else: # Si el bloque try no presenta ningun error vamos directo al else 
        for i in range(seq): # Bucle for para agregar cada numero a la lista
            try: # Otra vez usamos try para manejar errores
                x = input('Ingrese un numero entero: ')
                if '.' in x or ',' in x: # No encontre mejor manera de hacerlo que con un condicional if. Si el numero tiene un punto o una coma, lanzamos un ValueError
                    raise ValueError
                x = int(x) # Aqui decimos que el dato que agregamos sera un entero
                list.append(x) # Guardamos el numero en la lista 
            except ValueError as e: # Si se lanza un ValueError, se ejecuta este bloque
                print(f'Error: {e}')
                print('Por favor ingrese un numero valido (enteros)')
                return input_list() # Lo unico malo es aqui que tendria que volver al inicio de la funcion y puede ser un poco tedioso. 
    return list # Si no se lanza ningun error, retornamos la lista con los numeros ingresados por el usuario

def bubble(list): # Definimos la funcion bubble que reciba la lista anterior como argumento, esta sera la lista que vamos a ordenar
    indexing_len = len(list) - 1  # Aqui calculamos el ultimo indice de la lista, ya que el rango empieza desde 0 y no desde 1 por eso se le resta 1
    sorted = False # Esta variable booleana nos ayudara a saber si la lista esta ordenada o no. 
    # La iniciamos en False porque al principio la lista no esta ordenada.
    
    while not sorted: # Este bucle se continuara ejecutando mientras la lista este desordenada  
        sorted = True # Aqui cambiamos la variable sorted a True, ya que si no se lanza ningun error, la lista estara ordenada
        for i in range(0, indexing_len): # Recorremos la lista desde el primer hasta el penultimo indice. 
            if list[i] > list[i + 1]: # Aqui lo que hacemos es comparar el valor actual con el siguiente valor
                sorted = False # Si encontramos un par desordenado pues indicamos que la variable 'sorted' es falsa esto permite repetir el bucle
                list[i], list[i + 1] = list[i + 1], list[i] # Esta es la tecnica para intercambiar valores. 
                # Lo que hacemos es decir que el elemento a que es list[con indice 0] se convertira en el elemento b que es list[con indice 1] y viceversa.
    return list
    
test = input_list()
print(f'Lista desordenada: {test}')
print(f'Lista ordenada: {bubble(test)}')
