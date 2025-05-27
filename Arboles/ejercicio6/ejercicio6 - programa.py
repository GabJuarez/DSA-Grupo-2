"""
Ejercicio #6
Tarea (Conceptual): Describe cómo se podría utilizar un árbol para representar la expresión matemática
(3 + 4) * 2. ¿Cuáles serían los nodos y cómo se relacionarían? (No se requiere implementación completa,
solo la conceptualización de la estructura del árbol).
"""

from impresion_arbol import imprimir_arbol
import tkinter as tk
import sys

class Expresión:
    def __init__(expresión, nombre):
        expresión.nombre = nombre

class NodoElementos:
    def __init__(nodo, expresión):
        nodo.empleado = expresión
        nodo.subordinados = []

valores = {"A": "", "B": "", "C": ""}

def InsertarElementos(letra):
    valor = entrada.get()

    if valor.isdigit():
        valores[letra] = valor
        entrada.delete(0, tk.END)
        resultados.insert(tk.END, "Elemento {0} = {1}\n".format(letra, valores[letra]))
    else:
        resultados.insert(tk.END, "Ingrese un valor y número entero...\n")

class RedirigirSalida:
    def __init__(self, widget):
        self.widget = widget

    def write(self, texto):
        self.widget.insert(tk.END, texto)

def MostrarResultado():
    if not all(valores.values()):
        resultados.insert(tk.END, "Ingrese los elementos A, B y C...\n")
        return

    NodoA = NodoElementos(Expresión(valores["A"]))
    NodoB = NodoElementos(Expresión(valores["B"]))
    NodoC = NodoElementos(Expresión(valores["C"]))

    NodoSuma = NodoElementos(Expresión("+"))
    NodoSuma.subordinados.append(NodoA)
    NodoSuma.subordinados.append(NodoB)

    NodoMultiplicación = NodoElementos(Expresión("*"))
    NodoMultiplicación.subordinados.append(NodoSuma)
    NodoMultiplicación.subordinados.append(NodoC)

    resultados.insert(tk.END, "\nJerarquía del Árbol:\n")
    salida_original = sys.stdout
    sys.stdout = RedirigirSalida(resultados)
    imprimir_arbol(NodoMultiplicación)
    sys.stdout = salida_original

ventana = tk.Tk()
ventana.title("Expresión Matemática")
ventana.geometry("900x700")
ventana.resizable(False, False)
ventana.configure(bg="black")

tk.Label(ventana, text="Bienvenido, el programa muestra una expresión matemática en jerarquía de árbol", font=("Times", 16), bg="black", fg="white").pack(pady=5)
tk.Label(ventana, text="La expresión matemática es (A + B) * C", font=("Times", 16), bg="black", fg="white").pack(pady=5)
tk.Label(ventana, text="", bg="black").pack(pady=10)

entrada = tk.Entry(ventana, width=55, font=("Times", 12))
entrada.pack()

tk.Button(ventana, text="Insertar/Actualizar Elemento A", command=lambda: InsertarElementos("A"), width=30, font=("Times", 11)).pack(pady=5)
tk.Button(ventana, text="Insertar/Actualizar Elemento B", command=lambda: InsertarElementos("B"), width=30, font=("Times", 11)).pack(pady=5)
tk.Button(ventana, text="Insertar/Actualizar Elemento C", command=lambda: InsertarElementos("C"), width=30, font=("Times", 11)).pack(pady=5)
tk.Button(ventana, text="Mostrar Jerarquía de Árbol", command=MostrarResultado, width=30, font=("Times", 11)).pack(pady=5)

resultados = tk.Text(ventana, height=20, width=70, font=("Times", 14), bg="black", fg="white")
resultados.pack(pady=10)

ventana.mainloop()