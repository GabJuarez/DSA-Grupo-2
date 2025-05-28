import tkinter as tk
from tkinter import messagebox
import math

class NodoServidor:
    def __init__(self, nombre, x, y):
        self.nombre = nombre  # Nombre del servidor 
        self.x = x            # Coordenada X
        self.y = y            # Coordenada Y
        self.izquierdo = None 
        self.centro = None   
        self.derecho = None   

# Este árbol representa la jerarquía de servidores en una CDN.
# Se parte de un nodo raíz (servidor principal), y se extiende agregando servidores hijos.
class ArbolCDN:
    def __init__(self, raiz):
        self.raiz = raiz  # Nodo raíz del árbol

    def buscar_servidor_mas_cercano(self, nodo, x_usuario, y_usuario, mejor=None, mejor_distancia=float('inf')):
        """
        Esta función recorre el árbol recursivamente para encontrar el servidor más cercano
        al usuario, según sus coordenadas (x_usuario, y_usuario)
        """
        if nodo is None:
            return mejor

        # Se calcula la distancia entre el usuario y el nodo actual
        distancia = math.sqrt((nodo.x - x_usuario)**2 + (nodo.y - y_usuario)**2)

        # Si es el nodo más cercano hasta ahora, lo guardamos
        if distancia < mejor_distancia:
            mejor = nodo
            mejor_distancia = distancia

        # Recorremos recursivamente los tres hijos del nodo actual
        for hijo in [nodo.izquierdo, nodo.centro, nodo.derecho]:
            mejor = self.buscar_servidor_mas_cercano(hijo, x_usuario, y_usuario, mejor, mejor_distancia)

        return mejor

    def agregar_servidor(self, padre_nombre, nuevo_nombre, x, y):
        """
        Agrega un nuevo servidor como hijo del servidor con nombre 'padre_nombre'.
        """
        padre = self.buscar_nodo(self.raiz, padre_nombre)  # Buscamos al padre
        if padre:
            # Se agrega el nuevo servidor en la primera posición vacía
            if padre.izquierdo is None:
                padre.izquierdo = NodoServidor(nuevo_nombre, x, y)
                return True
            elif padre.centro is None:
                padre.centro = NodoServidor(nuevo_nombre, x, y)
                return True
            elif padre.derecho is None:
                padre.derecho = NodoServidor(nuevo_nombre, x, y)
                return True
            else:
                # Si ya tiene 3 hijos, mostramos un mensaje de error
                messagebox.showerror("Error", f"El servidor '{padre_nombre}' ya tiene 3 hijos.")
                return False
        else:
            messagebox.showerror("Error", f"No se encontró el servidor '{padre_nombre}'.")
            return False

    def buscar_nodo(self, nodo, nombre):
        """
        Búsqueda recursiva en el árbol. Retorna el nodo cuyo nombre coincida.
        """
        if nodo is None:
            return None
        if nodo.nombre == nombre:
            return nodo
        for hijo in [nodo.izquierdo, nodo.centro, nodo.derecho]:
            encontrado = self.buscar_nodo(hijo, nombre)
            if encontrado:
                return encontrado
        return None

    def obtener_texto_arbol(self):
        """
        Devuelve una cadena de texto que representa visualmente la jerarquía del árbol,
        usando indentaciones para simular los niveles del árbol.
        """
        def recorrer(nodo, nivel=0):
            if nodo is None:
                return ""
            espacio = "   " * nivel
            texto = f"{espacio}- {nodo.nombre}\n"
            texto += recorrer(nodo.izquierdo, nivel + 1)
            texto += recorrer(nodo.centro, nivel + 1)
            texto += recorrer(nodo.derecho, nivel + 1)
            return texto

        return recorrer(self.raiz)

# Muestra una ventana emergente con la estructura jerárquica del árbol
def mostrar_servidores():
    texto = arbol.obtener_texto_arbol()
    ventana = tk.Toplevel(root)
    ventana.title("Árbol de Servidores")
    text_area = tk.Text(ventana, width=40, height=20)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, texto)
    text_area.config(state=tk.DISABLED)

# Agrega un nuevo servidor como hijo del indicado por el usuario
def agregar_servidor():
    padre = entrada_padre.get()
    nombre = entrada_nombre.get()
    try:
        x = float(entrada_x.get())
        y = float(entrada_y.get())
        agregado = arbol.agregar_servidor(padre, nombre, x, y)
        if agregado:
            messagebox.showinfo("Éxito", f"Servidor '{nombre}' agregado como hijo de '{padre}'.")
    except ValueError:
        messagebox.showerror("Error", "Coordenadas inválidas. Usa números.")

# Busca el servidor más cercano al usuario según las coordenadas dadas
def buscar_servidor():
    try:
        x = float(entrada_usuario_x.get())
        y = float(entrada_usuario_y.get())
        mas_cercano = arbol.buscar_servidor_mas_cercano(arbol.raiz, x, y)
        if mas_cercano:
            messagebox.showinfo("Servidor más cercano", f"El servidor más cercano es: {mas_cercano.nombre}")
    except ValueError:
        messagebox.showerror("Error", "Coordenadas inválidas. Usa números.")

# Creamos el servidor raíz (servidor central)
raiz = NodoServidor("Managua", 100, 100)
arbol = ArbolCDN(raiz)

# Agregamos algunos servidores iniciales para ejemplificar la estructura
arbol.agregar_servidor("Managua", "León", 80, 80)
arbol.agregar_servidor("Managua", "Granada", 120, 90)
arbol.agregar_servidor("León", "Estelí", 60, 60)
arbol.agregar_servidor("Granada", "Masaya", 130, 85)

# Creamos la ventana principal
root = tk.Tk()
root.title("Red CDN Nicaragua")

# Sección para agregar servidor
tk.Label(root, text="Agregar Servidor").grid(row=0, column=0, columnspan=2)

tk.Label(root, text="Padre:").grid(row=1, column=0)
entrada_padre = tk.Entry(root)
entrada_padre.grid(row=1, column=1)

tk.Label(root, text="Nombre:").grid(row=2, column=0)
entrada_nombre = tk.Entry(root)
entrada_nombre.grid(row=2, column=1)

tk.Label(root, text="X:").grid(row=3, column=0)
entrada_x = tk.Entry(root)
entrada_x.grid(row=3, column=1)

tk.Label(root, text="Y:").grid(row=4, column=0)
entrada_y = tk.Entry(root)
entrada_y.grid(row=4, column=1)

tk.Button(root, text="Agregar", command=agregar_servidor).grid(row=5, column=0, columnspan=2, pady=5)

# Sección para buscar servidor más cercano
tk.Label(root, text="Buscar servidor más cercano").grid(row=6, column=0, columnspan=2)

tk.Label(root, text="Usuario X:").grid(row=7, column=0)
entrada_usuario_x = tk.Entry(root)
entrada_usuario_x.grid(row=7, column=1)

tk.Label(root, text="Usuario Y:").grid(row=8, column=0)
entrada_usuario_y = tk.Entry(root)
entrada_usuario_y.grid(row=8, column=1)

tk.Button(root, text="Buscar", command=buscar_servidor).grid(row=9, column=0, columnspan=2, pady=5)

# Botón para mostrar la jerarquía completa del árbol
tk.Button(root, text="Ver Árbol de Servidores", command=mostrar_servidores).grid(row=10, column=0, columnspan=2, pady=10)

# Iniciamos el bucle principal de la interfaz
root.mainloop()