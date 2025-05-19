from impresion_arbol import imprimir_arbol

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class NodoEmpleado:
    def __init__(self, empleado):
        self.subordinados = []
        self.empleado = empleado
    
    def buscar_nodo(self, nombre_objetivo):
        if self.empleado.nombre == nombre_objetivo:
            return self
        for sub in self.subordinados:
            resultado = sub.buscar_nodo(nombre_objetivo)
            if resultado:
                return resultado
        return None
    
    def agregar_subordinados(self):
        nombreJefe = input("Ingrese el nombre del jefe al cual le quiere agregar un subordinado: ") 
        jefe = self.buscar_nodo(nombreJefe)
        if jefe:
            subordinado = input(f"Ingrese el nombre del nuevo empleado dirigido por: {nombreJefe}")
            nuevo_nodo = NodoEmpleado(Empleado(subordinado))
            jefe.subordinados.append(nuevo_nodo)
            return True
        return False
    
def calcular_profundidad(nodo):
    if nodo is None:
        return 0
    
    if not nodo.subordinados:
        return 1
    
    return 1 + max(calcular_profundidad(hijo) for hijo in nodo.subordinados)


#creando al ceo de la organizacion
nombreCeo = input("Ingrese el nombre del CEO de la empresa: ")
ceo = NodoEmpleado(Empleado(nombreCeo))


while True:
    print("\nMenú:")
    print("1. Agregar empleado")
    print("2. Ver jerarquía")
    print("3. Calcular profundidad del árbol")
    print("4. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        ceo.agregar_subordinados()
    
    elif opcion == "2":
        print("\nJerarquía organizacional:")
        print("\n")
        imprimir_arbol(ceo)

    elif opcion == "3":
        profundidad = calcular_profundidad(ceo)
        print(f"La profundidad del árbol es: {profundidad}")
        break

    elif opcion == "4":
        print("saliendo del programa")
        break
    else:
        print("opcion no valida, intente de nuevo")