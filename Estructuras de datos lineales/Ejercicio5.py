"""Ejercicio #5: Búsqueda en una lista enlazada. 
Cree una función que busque un valor específico en una lista 
enlazada. La función debe devolver la posición del valor si se 
encuentra, o un mensaje indicando que el valor no está en la lista.
"""
import tkinter as tk
from tkinter import messagebox

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertar_inicio(self, nuevoDato):
        nuevoNodo = Nodo(nuevoDato)
        nuevoNodo.siguiente = self.head
        self.head = nuevoNodo

    def insertar_final(self, nuevoDato):
        nuevoNodo = Nodo(nuevoDato)
        if self.head is None:
            self.head = nuevoNodo
            return
        else:
            ultimo = self.head
            while ultimo.siguiente is not None:
               ultimo = ultimo.siguiente
            ultimo.siguiente = nuevoNodo

    def buscar_valor(self, valor):
        if self.head is None:
            return "La lista esta vacia"
        
        nodo = self.head
        contador = 0

        if self.head.dato == valor:
            return "El valor buscado esta en la posicion 0, al inicio de la lista enlazada"
        
        else:
            contador = 1
            nodo = self.head.siguiente

            while nodo is not None:
                if nodo.dato == valor:
                    return f"el valor {valor}, se ha encontrado en la posicion {contador}"
                nodo = nodo.siguiente
                contador += 1
            return f"el valor {valor}, no se ha encontrado en la lista enlazada"
    
    def mostrar_lista(self):
        if self.head is None:
            return "La lista esta vacia"
        
        elementos = []
        nodo = self.head
        while nodo:
            elementos.append(str(nodo.dato))
            nodo = nodo.siguiente
        return " -> ".join(elementos)
    

#crear lista enlazada
lista = LinkedList()

def insertar_inicio():
    valor = entrada.get()
    if valor:
        lista.insertar_inicio(valor)
        messagebox.showinfo("Insertar al inicio", f"Se insertó {valor}")
        entrada.delete(0, tk.END)
        actualizar_lista()

def insertar_final():
    valor = entrada.get()
    if valor:
        lista.insertar_final(valor)
        messagebox.showinfo("Insertar al final", f"Se insertó '{valor}' al final.")
        entrada.delete(0, tk.END)
        actualizar_lista()

def buscar():
    valor = entrada.get()
    if valor:
        resultado = lista.buscar_valor(valor)
        messagebox.showinfo("Buscar valor", resultado)
        entrada.delete(0, tk.END)

def actualizar_lista():
    texto = lista.mostrar_lista()
    etiqueta_lista.config(text=texto)


# interfaz con tkinter
ventana = tk.Tk()
ventana.title("Linked List con interfaz")
ventana.geometry("600x400")
ventana.minsize(400, 300)
ventana.config(bg="#adc9e6")

#frame central, ocupa 80% de la ventana y esta centrado
frame_central = tk.Frame(ventana, bg="#f0f0f0", bd=2, relief="ridge")
frame_central.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.8, relheight=0.8)

#widgets dentro del frame
entrada = tk.Entry(frame_central, font=("Arial", 14))
entrada.pack(pady=10, padx=10, fill='x', expand=True)

btn_inicio = tk.Button(frame_central, text="Inserta al inicio", command=insertar_inicio, font=("Arial", 12))
btn_inicio.pack(pady=5)

btn_final = tk.Button(frame_central, text="Inserta al final", command=insertar_final, font=("Arial", 12))
btn_final.pack(pady=5)

btn_buscar = tk.Button(frame_central, text="Buscar en la lista enlazada", command=buscar, font=("Arial", 12))
btn_buscar.pack(pady=5)

etiqueta_lista = tk.Label(frame_central, text="La lista se mostrará aquí", bg="#f0f0f0", font=("Arial", 12))
etiqueta_lista.pack(pady=10, padx=10, fill='both', expand=True)

ventana.mainloop()