import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod
from impresion_arbol import obtener_estructura_arbol

# clase abstracta que sirve como clase padre de directorio y archivo
class ElementoFS(ABC):
    def __init__(self, nombre, padre=None):
        self.nombre = nombre
        self.padre = padre

    def obtener_ruta_completa(self):
        if self.padre is None:
            return "/" + self.nombre
        return self.padre.obtener_ruta_completa() + "/" + self.nombre

    @abstractmethod
    def tipo(self):
        pass

class Directorio(ElementoFS):
    def __init__(self, nombre, padre=None):
        super().__init__(nombre, padre)
        #no se pasa la lista como parametro al constructor para evitar problemas
        self.hijos = []

    def tipo(self):
        return "Directorio"

    def agregar_hijo(self, elemento):
        elemento.padre = self
        self.hijos.append(elemento)

    def buscar_directorio(self, nombre):
        if self.nombre == nombre:
            return self
        for hijo in self.hijos:
            if hijo.tipo() == "Directorio":
                encontrado = hijo.buscar_directorio(nombre)
                if encontrado:
                    return encontrado
        return None

    def buscar_archivo(self, nombre_archivo):
        for hijo in self.hijos:
            if hijo.tipo() == "Archivo" and hijo.nombre == nombre_archivo:
                return hijo.obtener_ruta_completa()
            elif hijo.tipo() == "Directorio":
                resultado = hijo.buscar_archivo(nombre_archivo)
                if resultado:
                    return resultado
        return None

#clase archivos (hojas del arbol)
class Archivo(ElementoFS):
    def tipo(self):
        return "Archivo"

#interfaz
raiz = None  

ventana = tk.Tk()
ventana.title("Sistema de Archivos")
ventana.geometry("420x550")
ventana.configure(bg="#b3c3cb")

estilo_label = {"font": ("Helvetica", 10), "bg": "#f0f4f7"}
estilo_entrada = {"font": ("Helvetica", 10)}
 
 #frame para ver el arbol completo y funcion para actualizarlo cada vez que se modifica
frame_arbol = tk.LabelFrame(ventana, text="Estructura del árbol", bg="#f0f4f7", padx=10, pady=10)
frame_arbol.pack(padx=10, pady=10, fill="both")

#formateando la etiqueta
label_arbol = tk.Label(frame_arbol, text="", **estilo_label, wraplength=380, justify="left")
label_arbol.pack()

def actualizar_arbol():
    global raiz
    if raiz:
        estructura = obtener_estructura_arbol(raiz)
        label_arbol.config(text=estructura)
        ventana.update_idletasks()  # refrescar la interfaz
    else:
        label_arbol.config(text="No hay estructura de archivos disponible.")

#crear la raiz
frame_raiz = tk.Frame(ventana, bg="#f0f4f7")
frame_raiz.pack(pady=10)

label_raiz = tk.Label(frame_raiz, text="Nombre del directorio raiz:", **estilo_label)
label_raiz.pack()
entry_raiz = tk.Entry(frame_raiz, **estilo_entrada)
entry_raiz.pack()

def crear_raiz():
    global raiz
    nombre = entry_raiz.get()
    if nombre:
        raiz = Directorio(nombre)
        messagebox.showinfo("exito", f"Directorio raiz '{nombre}' creado")
        frame_raiz.destroy()  #oculta la entrada para que la raiz no se pueda volver a modificar
    else:
        messagebox.showerror("Error", "ingresa un nombre")
    actualizar_arbol()

tk.Button(frame_raiz, text="Crear raiz", command=crear_raiz, bg="#4caf50", fg="white").pack(pady=5)

# seccion para agregar subdirectorios
frame_sub = tk.LabelFrame(ventana, text="Agregar subdirectorio", bg="#f0f4f7", padx=10, pady=10)
frame_sub.pack(padx=10, pady=10, fill="both")

tk.Label(frame_sub, text="Nombre del subdirectorio:", **estilo_label).pack()
entry_sub = tk.Entry(frame_sub, **estilo_entrada)
entry_sub.pack()

tk.Label(frame_sub, text="Nombre del directorio padre:", **estilo_label).pack()
entry_padre = tk.Entry(frame_sub, **estilo_entrada)
entry_padre.pack()

def agregar_subdirectorio():
    global raiz
    if raiz is None:
        messagebox.showerror("Error", "Primero se debe crear la raiz")
        return
    nombre_sub = entry_sub.get()
    nombre_padre = entry_padre.get()
    padre = raiz.buscar_directorio(nombre_padre)
    if padre:
        nuevo = Directorio(nombre_sub)
        padre.agregar_hijo(nuevo)
        messagebox.showinfo("Éxito", f"Subdirectorio '{nombre_sub}' agregado a '{nombre_padre}'.")
    else:
        messagebox.showerror("Error", f"No se encontro el directorio padre '{nombre_padre}'.")
        actualizar_arbol()


tk.Button(frame_sub, text="Agregar subdirectorio", command=agregar_subdirectorio, bg="#2196f3", fg="white").pack(pady=5)

#seccion para agregar archivos
frame_archivo = tk.LabelFrame(ventana, text="Agregar archivo", bg="#f0f4f7", padx=10, pady=10)
frame_archivo.pack(padx=10, pady=10, fill="both")

tk.Label(frame_archivo, text="Nombre del archivo:", **estilo_label).pack()
entry_archivo = tk.Entry(frame_archivo, **estilo_entrada)
entry_archivo.pack()

tk.Label(frame_archivo, text="Nombre del directorio contenedor:", **estilo_label).pack()
entry_dir_archivo = tk.Entry(frame_archivo, **estilo_entrada)
entry_dir_archivo.pack()

def agregar_archivo():
    global raiz
    if raiz is None:
        messagebox.showerror("Error", "Primero debes crear la raiz")
        return
    nombre_archivo = entry_archivo.get()
    nombre_directorio = entry_dir_archivo.get()
    directorio = raiz.buscar_directorio(nombre_directorio)
    if directorio:
        nuevo = Archivo(nombre_archivo)
        directorio.agregar_hijo(nuevo)
        messagebox.showinfo("exito", f"Archivo '{nombre_archivo}' agregado a '{nombre_directorio}'.")
    else:
        messagebox.showerror("Error", f"No se encontro el directorio '{nombre_directorio}'.")
        actualizar_arbol()


tk.Button(frame_archivo, text="Agregar archivo", command=agregar_archivo, bg="#ff9800", fg="white").pack(pady=5)

# seccion para buscar archivo
frame_buscar = tk.LabelFrame(ventana, text="Buscar archivo", bg="#f0f4f7", padx=10, pady=10)
frame_buscar.pack(padx=10, pady=10, fill="both")

tk.Label(frame_buscar, text="Nombre del archivo a buscar:", **estilo_label).pack()
entry_buscar = tk.Entry(frame_buscar, **estilo_entrada)
entry_buscar.pack()

resultado_var = tk.StringVar()

def buscar_archivo():
    global raiz
    if raiz is None:
        messagebox.showerror("Error", "Primero debés crear la raíz.")
        return
    nombre = entry_buscar.get()
    ruta = raiz.buscar_archivo(nombre)
    if ruta:
        resultado_var.set(f"Ruta completa: {ruta}")
    else:
        resultado_var.set("Archivo no encontrado.")

tk.Button(frame_buscar, text="Buscar archivo", command=buscar_archivo, bg="#9c27b0", fg="white").pack(pady=5)
tk.Label(frame_buscar, textvariable=resultado_var, **estilo_label, wraplength=380).pack()

ventana.mainloop()