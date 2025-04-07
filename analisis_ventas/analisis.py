'''
Ejercicio 1: 
Desarrollar un programa que procese un conjunto de registros de ventas para extraer informacion relevante. Deben aplicar funciones internas como map, filter y reduce
Para transformar y filtrar los datos, calculando totales y promedios

•	[ ] El programa procesa correctamente un conjunto de registros de ventas.
•	[ ] Se utilizan las funciones map, filter y reduce para transformar y filtrar los datos.
•	[ ] Se calculan correctamente los totales de ventas.
•	[ ] Se calculan correctamente los promedios de ventas.
•	[ ] El código es legible y está bien documentado.

Necesitariamos datos como: 
    Productos
    Precios unitarios
    Cantidades 

La funcion map podemos usarla para calcular total de cada venta
La funcion filter nos puede ayudar a filtrar ventas mayores a ciertos montons
La funcion reduce nos puede ayudar a calcular totales de ventas

Si queremos enfocarnos en POO podemos crear dos clases
    Una para ventas en donde podriamos tener los atributos de producto, precio y cantidad
    Otra para la gestion de las ventas donde se realicen todas las funciones de mapear, filtrar y reducir
'''

from functools import reduce # Para la funcion reduce tenemos que importar la libreria functiontools

# Función para ingresar los datos de venta
def ingresar_venta(): # Definimos una funcion donde se ingresaran los datos de la venta
    try:
        producto = input("Ingrese el nombre del producto: ")
        if ord(producto) < 65 and ord(producto) > 90:
            raise TypeError
    except TypeError as e:
        print(f'Error: {e}')
        print('Por favor ingrese solamente texto')
        return ingresar_venta()
    else:
        try:
            precio = float(input("Ingrese el precio unitario: "))
            if precio <= 0: 
                raise ValueError
            elif isinstance (precio, str):
                raise TypeError
        except ValueError as e: 
            print(f'Error: {e}')
            print('Por favor ingrese valores en un rango correcto > 0 ')
            return ingresar_venta()
        except TypeError as e: 
            print(f'Error: {e}')
            print('Por favor ingrese valores correctos (flotantes o enteros)')
            return ingresar_venta()
        else: 
            try:    
                cantidad = int(input("Ingrese la cantidad: "))
                if cantidad <= 0: 
                    raise ValueError
                elif isinstance(cantidad, str or float): 
                    raise TypeError
            except ValueError as e:
                print(f'Error: {e}')
                print(f'Ingrese datos correctos (enteros)')
                return ingresar_venta()
            except TypeError as e: 
                print(f'Error: {e}')
                print(f'Por favor ingrese tipos de valores correctos (enteros)')
                return ingresar_venta()
            else: 
                return {"producto": producto, "precio": precio, "cantidad": cantidad} # Retornamos un diccionario con los datos ingresados
    
    

# Creamos una lista vacia para almacenar los registros de venta que el usuario vaya a ingresar.
ventas = [] 

# Pedimos al usuario cuántas ventas va a ingresar
def input_ventas():
    try: 
        num_ventas = int(input("¿Cuántas ventas desea ingresar? "))
        if num_ventas <= 0:
            raise ValueError
        elif isinstance(num_ventas, str or float):
            raise TypeError
    except TypeError as e: 
        print(f'Error: {e}')
        print('Ingrese valores correctos (enteros)')
        return input_ventas()
    except ValueError as e: 
        print(f'Error: {e}')
        print('Ingrese tipos valores corrector (enteros)')
        return input_ventas()
    else: 
        # Ingresamos las ventas usando un bucle for que se repite para cada venta anteriormente dada
        for i in range(num_ventas):
            venta = ingresar_venta() # Llamamos a la funcion ingresar_venta para que ingrese los datos
            ventas.append(venta)  # Con el metodo append agregamos la venta a la lista que creamos anteriormente6

# Resultados
input_ventas()

# 1. Usamos map para calcular el total de cada venta
totales_individuales = list(map(lambda v: v["precio"] * v["cantidad"], ventas))
# Aqui lo que estamos diciendo es que vamos a tomar cada venta (v) de la lista 
# Vamos a multiplicar el precio por la cantidad  

# 2. Usamos filter para obtener solo las ventas con total mayor a 300
ventas_mayores_300 = list(filter(lambda v: v["precio"] * v["cantidad"] > 300, ventas))
# Aqui lo que estamos diciendo es que vamos a recorrer cada venta y evaluar si el total es mayor a 300
# De ser asi, incluimos este resultado  

# 3. Usamos reduce para calcular el total general de ventas
total_general = reduce(lambda acc, v: acc + (v["precio"] * v["cantidad"]), ventas, 0)
# Acc es el acumulador que empieza en 0 y se va sumando el total de cada venta
# Para cada venta (v), calcula el total, luego que calcula el total lo suma al acumulador y al final devuelve la suma de todos los totales


# 4. Calculamos el promedio de ventas
promedio_ventas = total_general / len(ventas) if ventas else 0
# Aqui dividimos el total general de ventas entre cantidad de registros 
# Si la lista esta vacio, devuelve 0

print("\nTotales individuales de cada venta:", totales_individuales)
print("Ventas con total mayor a $300:", [v["producto"] for v in ventas_mayores_300])
print("Total general de ventas:", total_general)
print("Promedio de ventas:", promedio_ventas)