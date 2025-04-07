import datetime
import random

class Factura:
    idsUsados = set()

    def __init__(self, id, cliente, items: dict[str, dict[str, float]], pymt):
        self.id = id
        self.fecha = datetime.datetime.now()
        self.cliente = cliente
        self.items = items
        self.pymt = pymt
        self._subtotal = 0
        self._total = 0

    """La mayoria de validaciones se hicieron en los setters de los atributos, esto debido a querer practicar
    con los decoradores y a emplear buenas practicas de programacion, para que estas validaciones hayan funcionado
    se crea una instancia de la clase Factura y se le intenta asignar los valores recolectado por los inputs de los usuarios,
    de modo que si se ingresa un dato invalido el setter no deja asignar ese valor a su atributo, generando asi un error"""

    #region access modifiers
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El id debe ser un número entero")
        if valor <= 0:
            raise ValueError("Ingrese un id positivo")
        if valor in Factura.idsUsados:
            raise ValueError("El id no puede ser repetido")
        self._id = valor
        Factura.idsUsados.add(valor)

    @property
    def fecha(self):
        return self._fecha.strftime("%d/%m/%Y %H:%M:%S")
    
    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, valor):
        if not valor:
            raise ValueError("Ingrese un cliente valido")
        self._cliente = valor

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        if value is None or not value:
            raise ValueError("Los artículos no pueden ser None o vacíos.")
        if not isinstance(value, dict):
            raise ValueError("Los artículos deben ser un diccionario. Ejemplo: {'item1': {'precio': 10.0, 'cantidad': 2}}")

        for key, val in value.items():
            # validando que la key del diccionario(el nombre del produtcto), no sea none o un str vacio
            if not key or key is None:
                raise ValueError("El nombre del artículo no puede ser None o estar vacío.")

            # validando que los valores asociados sean un diccionario
            if not isinstance(val, dict):
                raise ValueError(f"Intente ingresar los datos nuevamente, hubo un error en el formato de la entrada de informacion")

            #validando que las claves precio y cantidad se encuentren en el diccionario
            if 'precio' not in val or 'cantidad' not in val:
                raise ValueError(f"El artículo '{key}' debe tener las claves 'precio' y 'cantidad'.")

            #numero valido para el precio
            if not isinstance(val['precio'], (int, float)) or val['precio'] <= 0:
                raise ValueError(f"El precio del artículo '{key}' debe ser un número mayor que 0.")

            # numero valido para la cantidad
            if not isinstance(val['cantidad'], int) or val['cantidad'] <= 0:
                raise ValueError(f"La cantidad del artículo '{key}' debe ser un entero mayor que 0.")

        #el valor se asigna si se logran pasar todas las validaciones anteriores
        self._items = value

    @property
    def pymt(self):
        return self._pymt

    @pymt.setter
    def pymt(self, valor):
        if valor not in ['efectivo', 'tarjeta', 'transferencia']:
            raise ValueError("El metodo de pago debe ser efectivo, tarjeta o transferencia")
        self._pymt = valor

    #endregion



    #region methods

    def calcularSubtotal(self, items):
        subtotal = 0
        for item, valores in items.items():
            subtotal += valores['precio'] * valores['cantidad']
        self._subtotal = subtotal
        return self._subtotal

    def calcularTotal(self):
        self._total = self._subtotal * 1.15
        return self._total

    @staticmethod
    def pedirDatos():
        facturas = []
        idsGenerados = set()

    #validando que la cantidad de facturas a ingresar sea mayor a 0
        while True:
            try:
                cant = int(input("Ingrese la cantidad de facturas a registrar: "))
                if cant <= 0:
                    raise ValueError("La cantidad de facturas debe ser mayor a 0.")
                break
            except ValueError as e:
             print(f"Error: {e}. Por favor, intente de nuevo.")

        for i in range(cant):
            

            while True:

                try:
                    print(f"---------- Factura #{i+1}----------")
                    #reolectando lo datos
                    idFact = random.randint(1, 10000)
                    while idFact in idsGenerados:  # si el id ya se ha generado se vuelve a generar
                        idFact = random.randint(1, 10000)
                    idsGenerados.add(idFact) #se agrega el id  a la lista de los que ya se han generado

                    cliente = input("Ingrese el nombre del cliente: ")

                    #validar que la cantidad de items sea mayor a 0
                    while True:
                        try:
                            numItems = int(input(f"Ingrese el número de ítems de la factura {i + 1}: "))
                            if numItems <= 0:
                                raise ValueError("El numero de articulos debe ser mayor a 0")
                            break
                        except ValueError as e:
                            print(f"Error: {e}. por favor intente de nuevo")

                    #recolectando los items
                    items = {}
                    for j in range(numItems):
                        nombre = input(f"Ingrese el nombre del articulo {j + 1}: ")
                        precio = float(input(f"Ingrese el precio de {nombre}: "))
                        cantidad = int(input(f"Ingrese la cantidad de {nombre}(s): "))
                        items[nombre] = {'precio': precio, 'cantidad': cantidad}

                    pymtMethod = input("Ingrese el método de pago (efectivo, tarjeta o transferencia): ").lower()

                    #activando los setters para que validen los datos de los atributos
                    
                    factura = Factura(idFact, cliente, items, pymtMethod)

                    factura.calcularSubtotal(items)
                    factura.calcularTotal()

                    facturas.append(factura)
                    print(f"Factura {i + 1} registrada correctamente\n")
                    break  
                except ValueError as e:
                    print(f"Error: {e}. Por favor intente de nuevo\n")
                    #se vuelve a pedir factura si los datos no son validos

        return facturas


    @staticmethod
    def generarReporte(facturas):
        print("---- Reporte de las facturas ingresadas ----")
        for factura in facturas:
            print(f"----------------- Factura -----------------")
            print(f"Codigo de factura: {factura.id}")
            print(f"Fecha: {factura.fecha}")
            print(f"Cliente: {factura.cliente}")
            print(f"Articulos comprados:")
            for item, valores in factura.items.items():
                print(f"Articulo: {item}, Precio: {valores['precio']}, Cantidad: {valores['cantidad']} = ${valores['precio'] * valores['cantidad']}")
            print(f"Subtotal: {factura._subtotal}")
            print(f"Total (despues de impuestos): {factura._total:.2f}")
            print(f"Metodo de pago: {factura.pymt}")
            print(f"------------------------------------------")
#endregion


#region main
def main():
    facturas = Factura.pedirDatos()
    Factura.generarReporte(facturas)  

if __name__ == "__main__":
    main()

main()
#end region