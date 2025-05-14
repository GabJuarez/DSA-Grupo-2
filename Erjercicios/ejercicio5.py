import os

# Función para limpiar la consola, compatible con Windows ('nt') y Unix/Linux/Mac
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para validar que el usuario ingrese un número entero positivo
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

# Clase que representa un cliente
class Cliente:
    def __init__(self, id, nombre, contacto, vip):
        self.id = id
        self.nombre = nombre
        self.contacto = contacto
        self.vip = vip  # Booleano que indica si es cliente VIP
        self.pedidos = []  # Lista para guardar pedidos asociados al cliente
    
    # Método para ingresar los datos de un nuevo cliente desde la consola
    def agregarCliente(self):
        id = input("Ingrese el ID del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        contacto = input("Ingrese el contacto del cliente: ")
        vip = False
        # Validación de si el cliente es VIP o no
        while True:
            respVip = input("¿Es cliente VIP? (si/no): ")
            if respVip.lower() not in ["si", "no"]:
                print("Respuesta inválida. Ingrese 'si' o 'no'.")
            else:
                if respVip.lower() == "si":
                    vip = True
                break
        # Retorna una nueva instancia del cliente con los datos ingresados
        cliente = Cliente(id, nombre, contacto, vip)
        return cliente  

# Clase que representa un pedido
class Pedido:
    def __init__(self):
        self.cliente = None  # Cliente asociado al pedido
        self.productos = []  # Lista de productos en el pedido (nombre, precio, cantidad)
        self.total = 0       # Total sin descuento
        self.descuento = 0   # Descuento aplicado
    
    # Método para calcular el descuento si el cliente es VIP (10%)
    def calcDescuento(self, cliente):
        if cliente.vip:
            self.descuento = self.total * 0.1
            self.total -= self.descuento

    # Método para agregar un producto al pedido
    def agregarProducto(self):
        producto = input("Ingrese el nombre del producto: ")
        print("Ingrese el precio del producto: ", end="")
        precio = validacionNum()
        print("Ingrese la cantidad del producto: ", end="")
        cantidad = validacionNum()
        # Agrega el producto a la lista
        self.productos.append((producto, precio, cantidad))
        # Actualiza el total del pedido
        self.total += precio * cantidad
            

# Función principal del programa
def main():
    clientes = []  # Lista para almacenar los clientes registrados

    while True:
        limpiar()
        # Menú principal
        print("---REGISTRO DE CLIENTES---")
        print("1. Agregar cliente")
        print("2. Crear pedido")
        print("3. Ver pedidos")
        print("4. Salir")
        print("Seleccione una opción: ", end="")
        opcion = validacionNum()

        # Se utiliza match-case para manejar las opciones del menú
        match opcion:
            case 1:
                # Opción para agregar un nuevo cliente
                limpiar()
                print("--REGISTRO DE CLIENTE--\n")
                instancia = Cliente("", "", "", False)  # Se crea una instancia temporal
                cliente = instancia.agregarCliente()    # Se recoge la información del nuevo cliente
                clientes.append(cliente)                # Se agrega a la lista
                print("Cliente agregado")
                input("Presione Enter para continuar...")
            case 2:
                # Opción para crear un nuevo pedido para un cliente existente
                limpiar()
                print("--CREAR PEDIDO--\n")
                id = input("Ingrese el ID del cliente: ")
                encontrado = False
                # Buscar cliente por ID
                for cliente in clientes:
                    if cliente.id == id:
                        pedido = Pedido()
                        pedido.cliente = cliente
                        print("Ingrese la cantidad de productos a agregar: ", end="")
                        cant = validacionNum()
                        # Agregar los productos al pedido
                        for i in range(cant):
                            print(f"\nProducto {i+1}:")
                            pedido.agregarProducto()
                        pedido.calcDescuento(cliente)  # Aplicar descuento si es VIP
                        cliente.pedidos.append(pedido) # Asociar pedido al cliente
                        encontrado = True
                        break
                if not encontrado:
                    print("Cliente no encontrado. Intente nuevamente.")
                    input("Presione Enter para continuar...")
            case 3:
                # Opción para ver todos los pedidos registrados
                limpiar()
                print("--PEDIDOS--")
                for cliente in clientes:
                    print("\n\n-------------------------------------")
                    print(f"Cliente: {cliente.nombre} \nID: {cliente.id} \nContacto: {cliente.contacto}")
                    cont = 1
                    # Mostrar los pedidos del cliente
                    for pedido in cliente.pedidos:  
                        print(f"\n--Pedido {cont}--")
                        print("\nProductos:")
                        for producto in pedido.productos:
                            print(f"- {producto[0]}: C${producto[1]} x {producto[2]}")
                        if cliente.vip:
                            print(f"\nCliente VIP: Descuento de C${pedido.descuento}")
                        print(f"\nTotal: C${pedido.total}")
                        cont += 1
                    print("-------------------------------------")
                input("Presione Enter para continuar...")
            case 4:
                # Opción para salir del programa
                limpiar()
                print("Saliendo del programa...")
                return
            case _:
                # Caso por defecto: opción no válida
                print("Opción no válida. Intente de nuevo.")

# Llamada al punto de entrada del programa
main()