'''
Simule el funcionamiento de una cola de impresión en una oficina donde varios empleados envían documentos para ser impresos. 
Cada documento tiene un nombre, el usuario que lo envió y el número de páginas. El sistema debe permitir agregar documentos 
a la cola, procesarlos en orden de llegada y mostrar cuál es el documento que se está imprimiendo actualmente. Analice con los 
estudiantes cómo se evita el desorden en el uso compartido de un recurso limitado.
'''

from collections import deque

cola_documentos = deque()
documento_actual = None  #para el documento que se esta imprimiendo actualmenete

def agregar_documento():
    try:
        cantidad = int(input('Ingrese la cantidad de documentos que quiere enviar a la cola de impresión: '))
        for i in range(cantidad):
            print(f'\nDocumento {i+1}:')
            nombre_documento = input('Ingrese el nombre del documento: ')
            usuario_envio = input('quien envio el documento?: ')
            numero_pag = int(input('Ingrese el número de páginas del documento: '))

            documento = {
                'nombre': nombre_documento,
                'usuario': usuario_envio,
                'paginas': numero_pag
            }

            cola_documentos.append(documento)
            print('documento agregado a la cola correctamente')
    except ValueError:
        print("ingresar un numero valido")

def procesar():
    global documento_actual
    if not cola_documentos:
        print("No hay documentos en la cola para procesar")
        documento_actual = None
        return

    try:
        cantidad = int(input('Ingrese la cantidad de documentos que desea procesar: '))
        for i in range(cantidad):
            if cola_documentos:
                documento_actual = cola_documentos.popleft()
                print(f'\nImprimiendo documento: "{documento_actual["nombre"]}"')
                print(f'Enviado por: {documento_actual["usuario"]}')
                print(f'Número de páginas: {documento_actual["paginas"]}')
            else:
                print("\nNo hay más documentos en la cola.")
                documento_actual = None
                break
    except ValueError:
        print("Ingrese un numero valido")

def mostrar_cola():
    if not cola_documentos:
        print("la cola de impresion esta vacia")
    else:
        print("\nDocumentos en la cola de impresión:")
        for i, doc in enumerate(cola_documentos, start=1):
            print(f'{i}. Documento: "{doc["nombre"]}", enviado por: {doc["usuario"]}, {doc["paginas"]} página(s)')

def ver_documento_actual():
    if documento_actual:
        print("\nDocumento que se está imprimiendo actualmente:")
        print(f'Documento: "{documento_actual["nombre"]}", enviado por: {documento_actual["usuario"]}, {documento_actual["paginas"]} página(s)')
    else:
        print("No se está imprimiendo ningún documento en este momento.")

#simulando
agregar_documento()
mostrar_cola()
procesar()
ver_documento_actual()
mostrar_cola()

