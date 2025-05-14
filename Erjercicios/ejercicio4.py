import os

# Función para limpiar la consola, dependiendo del sistema operativo
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función que valida que el usuario ingrese un número entero mayor a 0
def validacionNum():
    while True:
        try:
            num = int(input())  # Intenta convertir la entrada a entero
            if num <= 0:
                print("El número debe ser mayor a cero.")
                continue
            return num  # Retorna el número si es válido
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

# Clase que representa un producto
class Producto:
    def __init__(self, codigo, nombre, precio, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Clase interna que maneja el inventario de productos
    class Inventario:
        def __init__(self):
            self.productos = []  # Lista para almacenar los productos

        # Método para agregar un nuevo producto al inventario
        def agregarProducto(self):
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            print("Ingrese el precio del producto: ", end="")
            precio = validacionNum()
            print("Ingrese la cantidad del producto: ", end="")
            cantidad = validacionNum()
            item = Producto(codigo, nombre, precio, cantidad)  # Crea el producto
            self.productos.append(item)  # Lo agrega a la lista

        # Método para buscar un producto por nombre o por código
        def buscarProducto(self, bool):
            if bool == True:  # Buscar por nombre
                string = input("Ingrese el nombre del producto: ")
                for item in self.productos:
                    if item.nombre == string:
                        # Muestra la información del producto
                        print(f"\nNombre: {item.nombre}")
                        print(f"Precio: {item.precio}")
                        print(f"Cantidad: {item.cantidad}")
                        print(f"Codigo: {item.codigo}")
                        return
                print("Producto no encontrado.")
            else:  # Buscar por código
                string = input("Ingrese el codigo del producto: ")
                for item in self.productos:
                    if item.codigo == string:
                        print(f"\nNombre: {item.nombre}")
                        print(f"Precio: {item.precio}")
                        print(f"Cantidad: {item.cantidad}")
                        print(f"Codigo: {item.codigo}")
                        return
                print("Producto no encontrado.")

        # Método para eliminar un producto
        def eliminarProducto(self, codigo, bool):
            for item in self.productos:
                if item.codigo == codigo:
                    if bool == True:
                        # Elimina completamente el producto del inventario
                        self.productos.remove(item)
                    else:
                        while True:
                            # Disminuye la cantidad del producto
                            print(f"\nNombre: {item.nombre}, \nCantidad: {item.cantidad}")
                            print("Ingrese la cantidad a eliminar: ", end="")
                            cant = validacionNum()
                            if cant > item.cantidad:
                                print("La cantidad a eliminar es mayor a la cantidad actual.")
                                continue
                            else:
                                item.cantidad -= cant
                                break
                    return
            print("Producto no encontrado.")

# Función principal que ejecuta el menú de opciones
def main():
    inventario = Producto.Inventario()  # Crea el inventario
    limpiar()
    print("---REGISTRO DE PRODUCTOS---")

    while True:
        limpiar()
        print("--MENU PRINCIPAL--")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Eliminar producto")
        print("4. Salir")
        print("Seleccione una opción: ", end="")
        opcion = validacionNum()

        match opcion:
            case 1:  # Agregar producto
                while True:
                    limpiar()
                    print("--AGREGAR PRODUCTO--")
                    print("1. Agregar productos")
                    print("2. Volver al menú principal")
                    print("Seleccione una opción: ", end="")
                    agregarOpcion = validacionNum()
                    limpiar()
                    match agregarOpcion:
                        case 1:
                            print("Ingrese la cantidad de productos a agregar: ", end="")
                            cant = validacionNum()
                            for i in range(cant):
                                print(f"\nProducto {i+1}:")
                                inventario.agregarProducto()
                        case 2:
                            break
                        case _:
                            print("Opción no válida. Por favor, seleccione una opción del menú.")

            case 2:  # Buscar producto
                limpiar()
                print("--BUSCAR PRODUCTO--")
                print("1. Buscar producto")
                print("2. Volver al menú principal")
                print("Seleccione una opción: ", end="")
                buscarOpcion = validacionNum()
                limpiar()
                match buscarOpcion:
                    case 1:
                        val = False
                        while True:
                            # Pregunta si conoce el ID del producto
                            respID = input("Conoce el ID del producto? (si/no): ")
                            if respID.lower() not in ["si", "no"]:
                                print("Respuesta Invalidad. Ingrese si o no")
                            else:
                                if respID.lower() == "si":
                                    val = False
                                    break
                                else:
                                    val = True
                                    break
                        inventario.buscarProducto(val)
                        input("Presione enter para continuar...")
                        limpiar()
                    case 2:
                        break
                    case _:
                        print("Opción no válida. Por favor, seleccione una opción del menú.")

            case 3:  # Eliminar producto
                limpiar()
                print("--ELIMINAR PRODUCTO--")
                print("1. Eliminar producto")
                print("2. Volver al menú principal")
                print("Seleccione una opción: ", end="")
                eliminarOpcion = validacionNum()
                limpiar()
                match eliminarOpcion:
                    case 1:
                        while True:
                            val = False
                            print("1. Eliminar el item del inventario")
                            print("2. Disminuir la cantidad del producto")
                            print("Seleccione una opción: ", end="")
                            opc1 = validacionNum()
                            if opc1 == 1:
                                val = True
                            elif opc1 == 2:
                                val = False
                            else:
                                print("Opción no válida. Por favor, seleccione una opción del menú.")
                                continue
                            limpiar()
                            print("Ingrese el código del producto a eliminar: ", end="")
                            id = input()
                            inventario.eliminarProducto(id, val)

                            # Pregunta si desea eliminar otro producto
                            while True:
                                resp = input("Desea eliminar otro producto? (si/no): ")
                                if resp.lower() not in ["si", "no"]:
                                    print("Respuesta Invalida. Ingrese si o no")
                                    continue
                                else:
                                    break
                            if resp.lower() == "si":
                                continue
                            else:
                                break
                    case 2:
                        break
                    case _:
                        print("Opción no válida. Por favor, seleccione una opción del menú.")

            case 4:  # Salir del programa
                limpiar()
                print("Saliendo del programa.")
                break

            case _:  # Opción inválida
                print("Opción no válida. Por favor, seleccione una opción del menú.")

# Llama a la función principal
main()