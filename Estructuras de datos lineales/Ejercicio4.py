import tkinter as tk
from tkinter import messagebox
from collections import deque

cola = []

def agregar_elemento():
    nombre = entry_nombre.get().strip()
    try:
        prioridad = int(entry_prioridad.get())
    except ValueError:
        messagebox.showerror("Error", "La prioridad debe ser un número entero.")
        return
    
    if not nombre:
        messagebox.showwarning("Advertencia", "El nombre no puede estar vacío.")
        return
    
    cola.append((prioridad, nombre))
    entry_nombre.delete(0, tk.END)
    entry_prioridad.delete(0, tk.END)
    actualizar_lista()

def actualizar_lista():
    lista_cola.delete(0, tk.END)
    cola_ordenada = sorted(cola)
    for prioridad, nombre in cola_ordenada:
        lista_cola.insert(tk.END, f"{nombre} (Prioridad: {prioridad})")

def desencolar_elemento():
    if not cola:
        messagebox.showinfo("Cola vacía", "No hay elementos para desencolar.")
        return
    cola.sort()
    elemento = cola.pop(0)
    messagebox.showinfo("Desencolado", f"Elemento desencolado:\n{elemento[1]} (Prioridad: {elemento[0]})")
    actualizar_lista()

def limpiar_cola():
    cola.clear()
    actualizar_lista()


ventana = tk.Tk()
ventana.title("Cola de Prioridad")
ventana.geometry("400x400")
ventana.resizable(False, False)

tk.Label(ventana, text="Nombre del elemento:").pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Prioridad (entero, menor es más urgente):").pack(pady=5)
entry_prioridad = tk.Entry(ventana)
entry_prioridad.pack()

tk.Button(ventana, text="Agregar a la cola", command=agregar_elemento).pack(pady=10)

tk.Label(ventana, text="Cola actual:").pack()
lista_cola = tk.Listbox(ventana, width=40)
lista_cola.pack(pady=5)

tk.Button(ventana, text="Desencolar", command=desencolar_elemento).pack(pady=5)
tk.Button(ventana, text="Limpiar cola", command=limpiar_cola).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.destroy).pack(pady=10)

ventana.mainloop()
