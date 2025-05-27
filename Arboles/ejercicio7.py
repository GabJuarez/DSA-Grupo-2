"""
Ejercicio #7
Tarea: Representa una jerarquía de categorías de productos como un árbol. Escribe una función que tome
la raíz del árbol (la categoría principal) y una categoría específica , y devuelva todas las subcategorías
dentro de esa categoría.
"""

from impresion_arbol import imprimir_arbol
import tkinter as tk
import sys

class Categoría:
    def __init__(categoría, NombreCategoria):
        categoría.nombre = NombreCategoria

class NodoCategoría:
    def __init__(nodo, Categoría):
        nodo.empleado = Categoría
        nodo.subordinados = []

raíz = None

class RedirigirSalida:
    def __init__(self, widget):
        self.widget = widget

    def write(self, texto):
        self.widget.insert(tk.END, texto)

def InsertarCategoría():
    global raíz
    NombreCategoria = entrada.get()
    if not NombreCategoria:
        resultados.insert(tk.END, "Ingrese un nombre para la categoría...\n")
        return
    raíz = NodoCategoría(Categoría(NombreCategoria))
    entrada.delete(0, tk.END)
    resultados.insert(tk.END, "Categoría principal establecida: {0}\n".format(NombreCategoria))

def InsertarSubcategoría():
    if raíz is None:
        resultados.insert(tk.END, "Establezca una categoría principal...\n")
        return

    NombreCategoria = entrada.get()
    if not NombreCategoria:
        resultados.insert(tk.END, "Ingrese un nombre para la subcategoría...\n")
        return

    subcategoría = NodoCategoría(Categoría(NombreCategoria))
    raíz.subordinados.append(subcategoría)
    entrada.delete(0, tk.END)
    resultados.insert(tk.END, "Subcategoría agregada: {0}\n".format(NombreCategoria))

def MostrarJerarquía():
    if raíz is None:
        resultados.insert(tk.END, "Establezca una categoría principal...\n")
        return
    resultados.insert(tk.END, "\nJerarquía del Árbol de Categorías:\n")
    salida_original = sys.stdout
    sys.stdout = RedirigirSalida(resultados)
    imprimir_arbol(raíz)
    sys.stdout = salida_original

def ObtenerSubcategorias(nodo, NombreCategoria):
    if nodo.empleado.nombre == NombreCategoria:
        resultado = []
        def RecorrerSubcategorias(n):
            for sub in n.subordinados:
                resultado.append(sub.empleado.nombre)
                RecorrerSubcategorias(sub)
        RecorrerSubcategorias(nodo)
        return resultado
    
    for sub in nodo.subordinados:
        resultado = ObtenerSubcategorias(sub, NombreCategoria)
        if resultado is not None:
            return resultado
    return None

def MostrarSubcategorias():
    if raíz is None:
        resultados.insert(tk.END, "Establezca una categoría principal...\n")
        return
    
    NombreCategoria = entrada.get()
    if not NombreCategoria:
        resultados.insert(tk.END, "Ingrese un nombre para la categoría a buscar...\n")
        return
    
    subcategorias = ObtenerSubcategorias(raíz, NombreCategoria)
    if subcategorias is None:
        resultados.insert(tk.END, "No se encontró la categoría '{0}'...\n".format(NombreCategoria))
    elif len(subcategorias) == 0:
        resultados.insert(tk.END, "La categoría '{0}' no tiene subcategorías...\n".format(NombreCategoria))
    else:
        resultados.insert(tk.END, "Subcategorías dentro de '{0}':\n".format(NombreCategoria))
        for subcat in subcategorias:
            resultados.insert(tk.END, f" - {subcat}\n")

    entrada.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Jerarquía de Categorías")
ventana.geometry("900x700")
ventana.resizable(False, False)
ventana.configure(bg="black")

tk.Label(ventana, text="Bienvenido, el programa se encarga de mostrar categorías en jerarquía de árbol", font=("Times", 16), bg="black", fg="white").pack(pady=10)

entrada = tk.Entry(ventana, width=55, font=("Times", 12))
entrada.pack(pady=5)

tk.Button(ventana, text="Insertar Categoría Principal", command=InsertarCategoría, width=30, font=("Times", 11)).pack(pady=5)
tk.Button(ventana, text="Insertar Subcategoría", command=InsertarSubcategoría, width=30, font=("Times", 11)).pack(pady=5)
tk.Button(ventana, text="Mostrar Jerarquía", command=MostrarJerarquía, width=30, font=("Times", 11)).pack(pady=5)
tk.Button(ventana, text="Mostrar Subcategorías", command=MostrarSubcategorias, width=30, font=("Times", 11)).pack(pady=5)

resultados = tk.Text(ventana, height=20, width=70, font=("Times", 14), bg="black", fg="white")
resultados.pack(pady=10)

ventana.mainloop()