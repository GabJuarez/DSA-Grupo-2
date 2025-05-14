from collections import deque

class ServidorArchivos:
    def __init__(self):
        self.cola_solicitudes = deque()

    def registrar_solicitud(self, usuario, archivo):
        self.cola_solicitudes.append((usuario, archivo))
        print(f"Solicitud registrada: {usuario} - {archivo}")

    def atender_solicitud(self):
        if self.cola_solicitudes:
            usuario, archivo = self.cola_solicitudes.popleft()
            print(f"Atendiendo solicitud: {usuario} está accediendo a '{archivo}'")
        else:
            print("No hay solicitudes pendientes.")

    def mostrar_solicitudes_pendientes(self):
        if not self.cola_solicitudes:
            print("No hay solicitudes pendientes.")
        else:
            print("Solicitudes pendientes:")
            for i, (usuario, archivo) in enumerate(self.cola_solicitudes, 1):
                print(f"  {i}. {usuario} - {archivo}")

def main():
    servidor = ServidorArchivos()
    while True:
        print("\n--- Gestión de Acceso a Archivos ---")
        print("1. Registrar nueva solicitud")
        print("2. Atender la siguiente solicitud")
        print("3. Ver solicitudes pendientes")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            usuario = input("Nombre del usuario: ")
            archivo = input("Nombre del archivo: ")
            servidor.registrar_solicitud(usuario, archivo)
        elif opcion == '2':
            servidor.atender_solicitud()
        elif opcion == '3':
            servidor.mostrar_solicitudes_pendientes()
        elif opcion == '4':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

main()
