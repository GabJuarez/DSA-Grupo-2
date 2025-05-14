'''
Simule el funcionamiento de una cola de impresión en una oficina donde varios empleados envían documentos para ser impresos. 
Cada documento tiene un nombre, el usuario que lo envió y el número de páginas. El sistema debe permitir agregar documentos 
a la cola, procesarlos en orden de llegada y mostrar cuál es el documento que se está imprimiendo actualmente. Analice con los 
estudiantes cómo se evita el desorden en el uso compartido de un recurso limitado.
'''

from collections import deque

cola_documentos = deque()

def agregar_documento():
    seq = int(input('Cuantos documentos desea agregar? '))
    for i in range(seq):
        nombre_documento = input('Ingrese el nombre del documento: ')
        usuario_envio = input('Quien envio el documento: ')
        numero_pag = int(input('Ingrese el numero de paginas del documento: '))
        agregar = f'Documento {nombre_documento} numero {i} enviado por: {usuario_envio} con {numero_pag} pagina/s'
        cola_documentos.append(agregar)
        
def procesar():
    seq = int(input('Cuantos documentos desea procesar: '))
    for i in range(seq):
        print('Procesando')
        print(f'{cola_documentos[0]}')
        cola_documentos.popleft()
    
def mostrar_cola(agregar):
    for i in range(len(cola_documentos)):
        print(agregar)
        
    
agregar_documento()
procesar()
