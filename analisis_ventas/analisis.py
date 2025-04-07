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
def ingresar_venta():
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio unitario: "))
    cantidad = int(input("Ingrese la cantidad: "))
    return {"producto": producto, "precio": precio, "cantidad": cantidad}

# Lista para almacenar las ventas
ventas = []

# Pedimos al usuario cuántas ventas va a ingresar
num_ventas = int(input("¿Cuántas ventas desea ingresar? "))

# Ingresamos las ventas
for _ in range(num_ventas):
    venta = ingresar_venta()
    ventas.append(venta)

# 1. Usamos map para calcular el total de cada venta
totales_individuales = list(map(lambda v: v["precio"] * v["cantidad"], ventas))

# 2. Usamos filter para obtener solo las ventas con total mayor a 300
ventas_mayores_300 = list(filter(lambda v: v["precio"] * v["cantidad"] > 300, ventas))

# 3. Usamos reduce para calcular el total general de ventas
total_general = reduce(lambda acc, v: acc + (v["precio"] * v["cantidad"]), ventas, 0)

# 4. Calculamos el promedio de ventas
promedio_ventas = total_general / len(ventas) if ventas else 0

# Resultados
print("\nTotales individuales de cada venta:", totales_individuales)
print("Ventas con total mayor a $300:", [v["producto"] for v in ventas_mayores_300])
print("Total general de ventas:", total_general)
print("Promedio de ventas:", promedio_ventas)


