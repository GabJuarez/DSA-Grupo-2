import tkinter as tk
from tkinter import messagebox

# Nodo de lista doblemente enlazada
class NodoCancion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        # Puntero a la primera cancion de la lista
        self.primera = None
        # Puntero a la cancion actual en reproducción
        self.actual = None

    def agregar_cancion(self, nombre):
        # Se crea un nuevo nodo con el nombre de la canción
        nueva = NodoCancion(nombre)
        
        # Si la lista está vacía, esta canción será la primera y también la actual
        if not self.primera:
            self.primera = nueva
            self.actual = nueva
        else:
            # Si ya hay canciones, recorremos hasta el final de la lista
            temp = self.primera
            while temp.siguiente:
                temp = temp.siguiente
            # Enlazamos el último nodo con la nueva canción
            temp.siguiente = nueva
            nueva.anterior = temp  # Establecemos el enlace hacia atrás (doble enlace)

    def eliminar_actual(self):
        # Si no hay canción actual no hacemos nada
        if not self.actual:
            return
        
        # Guardamos cual será la siguiente canción despues de eliminar la actual.
        # Si no hay siguiente, usamos la anterior.
        siguiente = self.actual.siguiente or self.actual.anterior

        # Reconectamos los nodos anterior y siguiente para omitir el nodo actual
        if self.actual.anterior:
            self.actual.anterior.siguiente = self.actual.siguiente
        if self.actual.siguiente:
            self.actual.siguiente.anterior = self.actual.anterior

        # Si la canción eliminada era la primera de la lista actualizamos el puntero
        if self.actual == self.primera:
            self.primera = self.actual.siguiente

        # Actualizamos el nodo actual a la canción siguiente o anterior si no hay siguiente
        self.actual = siguiente

    def eliminar_por_nombre(self, nombre):
        # Empezamos desde la primera canción
        temp = self.primera
        while temp:
            # Si encontramos una canción con el nombre
            if temp.nombre == nombre:
                # Reenlazamos los nodos para eliminar este nodo de la lista
                if temp.anterior:
                    temp.anterior.siguiente = temp.siguiente
                if temp.siguiente:
                    temp.siguiente.anterior = temp.anterior

                # Si la canción eliminada era la primera, actualizamos el puntero
                if temp == self.primera:
                    self.primera = temp.siguiente

                # Si la canción eliminada era la actual, actualizamos el puntero actual
                if temp == self.actual:
                    self.actual = temp.siguiente or temp.anterior

                return True  # Se encontró y eliminó
            temp = temp.siguiente

        return False  # No se encontró ninguna canción con ese nombre

    def limpiar_lista(self):
        # Simplemente desconectamos todos los nodos eliminando las referencias
        # Python libera la memoria automaticamente al no haber referencias
        self.primera = None
        self.actual = None

    def siguiente(self):
        # Si existe una canción después de la actual, avanzamos a ella
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente

    def anterior(self):
        # Si existe una canción antes de la actual, retrocedemos a ella
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior

    def obtener_lista(self):
        # Creamos una lista vacía para guardar los nombres de las canciones
        canciones = []
        temp = self.primera
        # Recorremos la lista enlazada desde el inicio hasta el final
        while temp:
            canciones.append(temp.nombre)
            temp = temp.siguiente
        return canciones  # Retornamos la lista de nombres de canciones


def agregar_cancion():
    nombre = entrada.get().strip()  # .get() obtiene el texto actual del textbox
    if nombre:
        lista.agregar_cancion(nombre)
        entrada.delete(0, tk.END)  # .delete(inicio, fin) elimina texto tk.END es el final del texto
        actualizar_etiqueta()

def eliminar_actual():
    lista.eliminar_actual()  
    actualizar_etiqueta()   

def eliminar_por_nombre():
    nombre = entrada.get().strip()  # .strip() remueve espacios extra
    if not nombre:
        return
    exito = lista.eliminar_por_nombre(nombre)  

    if exito:
        # Muestra un messagebox 
        messagebox.showinfo("Éxito", f"La canción '{nombre}' fue eliminada.")
    else:
        messagebox.showwarning("No encontrada", f"No se encontró '{nombre}' en la lista.")

    entrada.delete(0, tk.END)  # Limpia el Entry
    actualizar_etiqueta() 

def limpiar_lista():
    lista.limpiar_lista()
    # Messagebox de confirmación
    messagebox.showinfo("Limpieza", "Lista de reproducción vaciada.")
    actualizar_etiqueta()

def siguiente():
    lista.siguiente()
    actualizar_etiqueta()

def anterior():
    lista.anterior()
    actualizar_etiqueta()

def mostrar_lista():
    canciones = lista.obtener_lista()
    if canciones:
        # Muestra una ventana con la lista separada por saltos de línea
        messagebox.showinfo("Lista de Reproducción", "\n".join(canciones))
    else:
        messagebox.showinfo("Lista de Reproducción", "No hay canciones en la lista.")

def actualizar_etiqueta():
    if lista.actual:
        # .config() permite cambiar propiedades
        etiqueta_actual.config(text=f"Canción actual: {lista.actual.nombre}")
    else:
        etiqueta_actual.config(text="Canción actual: Ninguna")

# Se crea la ventana principal 
ventana = tk.Tk()

# Cambia el título que aparece en la barra de la ventana
ventana.title("Lista de Reproducción")

# Define el tamaño inicial de la ventana en píxeles
ventana.geometry("400x400")

# Label simple para texto
tk.Label(ventana, text="Nombre de la canción:").pack(pady=5)
# .pack() agrega el widget a la ventana y lo organiza automáticamente
# pady agrega espacio vertical (padding) arriba y abajo del widget

# Entry: campo de texto donde el usuario puede escribir
entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=5)

# Botones que cada uno llama a una función cuando se hace click
tk.Button(ventana, text="Agregar", command=agregar_cancion).pack(pady=2)
# command enlaza el botón con la función que se ejecutará al hacer click

tk.Button(ventana, text="Eliminar actual", command=eliminar_actual).pack(pady=2)
tk.Button(ventana, text="Eliminar por nombre", command=eliminar_por_nombre).pack(pady=2)
tk.Button(ventana, text="Anterior", command=anterior).pack(pady=2)
tk.Button(ventana, text="Siguiente", command=siguiente).pack(pady=2)
tk.Button(ventana, text="Mostrar lista", command=mostrar_lista).pack(pady=2)

# Botón con texto rojo, útil para acciones importantes o destructivas
tk.Button(ventana, text="Clear Queue", fg="red", command=limpiar_lista).pack(pady=10)
# fg define el color del texto del botón

# Etiqueta dinámica para mostrar la canción actual
etiqueta_actual = tk.Label(
    ventana,
    text="Canción actual: Ninguna",  # Texto inicial
    fg="blue",                       # Color del texto
    font=("Arial", 11)              # Fuente y tamaño
)
etiqueta_actual.pack(pady=20)


# Se instancia la lista de reproducción
lista = ListaReproduccion()

# Inicia la ventana y la mantiene abierta hasta que el usuario la cierre
ventana.mainloop()