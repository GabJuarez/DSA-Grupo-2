'''
Ejercicio 4: Árbol Genealógico
Un árbol genealógico representa las relaciones familiares a lo largo de generaciones.
Tarea: Implementa una clase Persona con atributos para nombre, padre y madre
(que podrían ser otros nodos Persona). Crea un árbol genealógico simple.
Escribe una función que tome un nodo Persona y encuentre a todos sus ancestros
en una generación específica (por ejemplo, todos los bisabuelos).
'''

class Persona:
    def __init__(self, nombre, padre=None, madre=None):
        self.nombre = nombre
        self.padre = padre
        self.madre = madre

    def __str__(self):
        return self.nombre

def crear_persona(nombre, nivel, max_nivel):
    if nivel > max_nivel:
        return None

    print(f'\nDatos de: {nombre} (Nivel {nivel})')

    padre, madre = None, None

    if nivel < max_nivel:  # Solo preguntar por padres si estamos debajo del límite
        if input(f'¿{nombre} tiene padre? (s/n): ').strip().lower() == 's':
            nombre_padre = input(f'Nombre del padre de {nombre}: ').strip()
            padre = crear_persona(nombre_padre, nivel + 1, max_nivel)

        if input(f'¿{nombre} tiene madre? (s/n): ').strip().lower() == 's':
            nombre_madre = input(f'Nombre de la madre de {nombre}: ').strip()
            madre = crear_persona(nombre_madre, nivel + 1, max_nivel)

    return Persona(nombre, padre, madre)

def obtener_ancestros(persona, generacion):
    if persona is None:
        return []
    if generacion == 1:
        return [p for p in [persona.padre, persona.madre] if p]
    
    ancestros = []
    for p in [persona.padre, persona.madre]:
        ancestros += obtener_ancestros(p, generacion - 1)
    return ancestros

def imprimir_arbol(persona, nivel=0):
    if persona is None:
        return
    print('    ' * nivel + persona.nombre)
    if persona.padre:
        imprimir_arbol(persona.padre, nivel + 1)
    if persona.madre:
        imprimir_arbol(persona.madre, nivel + 1)

# === Programa Principal ===
if __name__ == '__main__':
    print('=== Arbol Genealogico con Visualizacion ===')
    nombre = input('Nombre de la persona principal: ').strip()
    
    while True:
        try:
            generaciones = int(input('¿Hasta cuántas generaciones desea registrar? (ej. 2 = padres y abuelos): '))
            if generaciones < 1:
                print('El número de generaciones debe ser al menos 1.')
                continue
            break
        except ValueError:
            print('Por favor, ingresa un número válido.')

    raiz = crear_persona(nombre, 1, generaciones)

    print('\n=== Estructura del Arbol Genealogico ===')
    imprimir_arbol(raiz)

    while True:
        try:
            g = int(input('\nGeneración a consultar (1=padres, 2=abuelos, etc., 0 para salir): '))
            if g == 0:
                print('Fin del programa.')
                break
            resultado = obtener_ancestros(raiz, g)
            if resultado:
                print(f'Ancestros en generación {g}:')
                for p in resultado:
                    print('-', p)
            else:
                print('No hay ancestros registrados en esa generación.')
        except ValueError:
            print('Ingresa un número válido.')

