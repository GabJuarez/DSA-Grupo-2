'''
Ejercicio 3: Árbol de Decisiones para Diagnóstico
En medicina o en sistemas de soporte técnico, se utilizan árboles de decisiones 
para guiar el proceso de diagnóstico basado en una serie de preguntas.
Tarea: Representa un árbol de decisiones simple para diagnosticar una falla común 
en un dispositivo electrónico. Cada nodo interno representará una pregunta, las 
ramas representarán las posibles respuestas, y las hojas representarán el diagnóstico
final. Escribe una función que recorra el árbol de decisiones basado en las respuestas
del usuario y llegue a un diagnóstico.
'''

class nodo_decision:
    def __init__(self, pregunta=None, diagnostico=None):
        self.pregunta = pregunta            
        self.diagnostico = diagnostico      
        self.si = None                      
        self.no = None                      

def construir_arbol():
    raiz = nodo_decision(pregunta='El dispositivo enciende?')
    
    nodo_si = nodo_decision(pregunta='La pantalla se ve bien?')
    nodo_si.si = nodo_decision(diagnostico='Todo funciona correctamente')
    nodo_si.no = nodo_decision(diagnostico='Pantalla defectuosa')
    
    nodo_no = nodo_decision(pregunta='La bateria esta cargada?')
    nodo_no.si = nodo_decision(diagnostico='Falla interna del hardware')
    nodo_no.no = nodo_decision(diagnostico='Cargar el dispositivo')
    
    raiz.si = nodo_si
    raiz.no = nodo_no
    
    return raiz

def diagnosticar(nodo):
    if nodo.diagnostico is not None:
        print('\nDiagnostico final:', nodo.diagnostico)
        return

    while True:
        respuesta = input(f'\n{nodo.pregunta} (si/no): ').strip().lower()
        if respuesta == 'si':
            diagnosticar(nodo.si)
            break
        elif respuesta == 'no':
            diagnosticar(nodo.no)
            break
        else:
            print('Respuesta no valida. Por favor, escribe "si" o "no".')

def imprimir_arbol(nodo, prefijo='', rama=''):
    if nodo is None:
        return

    if nodo.diagnostico is not None:
        print(f'{prefijo}{rama}→ {nodo.diagnostico}')
    else:
        print(f'{prefijo}{rama}{nodo.pregunta}')
        nuevo_prefijo = prefijo + '│   ' if rama else ''
        imprimir_arbol(nodo.si, nuevo_prefijo, '├── si ')
        imprimir_arbol(nodo.no, nuevo_prefijo, '└── no ')

if __name__ == '__main__':
    arbol = construir_arbol()
    
    print('Estructura del arbol de decisiones:\n')
    imprimir_arbol(arbol)
    
    print('\nIniciando diagnostico...')
    diagnosticar(arbol)
