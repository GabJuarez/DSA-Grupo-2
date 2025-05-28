import tkinter as tk
from tkinter import messagebox

# Clase para representar una etiqueta HTML como nodo del árbol
class NodoHTML:
    def __init__(self, nombre, atributos=None):
        self.nombre = nombre
        self.atributos = atributos or {}
        self.hijos = []

# Clase del árbol HTML
class ArbolHTML:
    def __init__(self, raiz):
        self.raiz = raiz  # Etiqueta <html>

    # Buscar todos los nodos con cierto nombre de etiqueta
    def buscar_todos(self, nodo, nombre_busqueda, resultados=None):
        if resultados is None:
            resultados = []

        if nodo.nombre == nombre_busqueda:
            resultados.append(nodo)

        for hijo in nodo.hijos:
            self.buscar_todos(hijo, nombre_busqueda, resultados)

        return resultados

    # Agregar un nuevo nodo hijo a un nodo padre específico
    def agregar_nodo(self, padre, nombre_hijo, atributos=None):
        nuevo = NodoHTML(nombre_hijo, atributos)
        padre.hijos.append(nuevo)

    # Obtener texto con indentación para mostrar la jerarquía
    def obtener_texto_arbol(self):
        def recorrer(nodo, nivel=0):
            texto = "   " * nivel + f"<{nodo.nombre}>\n"
            for hijo in nodo.hijos:
                texto += recorrer(hijo, nivel + 1)
            return texto

        return recorrer(self.raiz)

# Interfaz gráfica
root = tk.Tk()
root.title("Estructura HTML")
root.geometry("500x600")

# Crear árbol con raíz <html>
raiz = NodoHTML("html")
arbol = ArbolHTML(raiz)

# Función para mostrar la jerarquía en una nueva ventana
def mostrar_estructura():
    texto = arbol.obtener_texto_arbol()
    ventana = tk.Toplevel(root)
    ventana.title("Estructura del Documento")
    text_area = tk.Text(ventana, width=50, height=25)
    text_area.pack(padx=10, pady=10)
    text_area.insert(tk.END, texto)
    text_area.config(state=tk.DISABLED)

def buscar_padres():
    nombre = entrada_padre.get().strip()
    if not nombre:
        messagebox.showerror("Error", "Ingresa una etiqueta padre.")
        return

    coincidencias = arbol.buscar_todos(arbol.raiz, nombre)
    if not coincidencias:
        messagebox.showinfo("Sin resultados", f"No se encontraron etiquetas <{nombre}>.")
        return

    opciones_listbox.delete(0, tk.END)  # Limpiar listbox

    for i, nodo in enumerate(coincidencias):
        resumen = f"{i+1}. <{nodo.nombre}> con {len(nodo.hijos)} hijos"
        opciones_listbox.insert(tk.END, resumen)

    # Guardamos los nodos encontrados para usar luego al agregar
    opciones_listbox.coincidencias = coincidencias

# Función para agregar nueva etiqueta a una de las coincidencias seleccionadas
def agregar_etiqueta():
    try:
        indice = opciones_listbox.curselection()[0]
        nodo_padre = opciones_listbox.coincidencias[indice]
    except IndexError:
        messagebox.showerror("Error", "Selecciona una coincidencia válida.")
        return

    nombre_hijo = entrada_nueva_etiqueta.get().strip()
    if not nombre_hijo:
        messagebox.showerror("Error", "Ingresa el nombre de la nueva etiqueta.")
        return

    arbol.agregar_nodo(nodo_padre, nombre_hijo)
    messagebox.showinfo("Éxito", f"Etiqueta <{nombre_hijo}> agregada correctamente.")

# Campos de entrada
tk.Label(root, text="Nombre de etiqueta padre:").pack(pady=(10, 0))
entrada_padre = tk.Entry(root)
entrada_padre.pack()

tk.Button(root, text="Buscar padre", command=buscar_padres).pack(pady=5)

tk.Label(root, text="Coincidencias encontradas:").pack()
opciones_listbox = tk.Listbox(root, height=6)
opciones_listbox.pack(pady=5)

tk.Label(root, text="Nueva etiqueta a agregar:").pack(pady=(10, 0))
entrada_nueva_etiqueta = tk.Entry(root)
entrada_nueva_etiqueta.pack()

tk.Button(root, text="Agregar etiqueta", command=agregar_etiqueta).pack(pady=10)

tk.Button(root, text="Ver Documento", command=mostrar_estructura).pack(pady=10)

# Inicializamos el árbol con etiquetas ejemplo
body = NodoHTML("body")
raiz.hijos.append(body)
div1 = NodoHTML("div")
div2 = NodoHTML("div")
body.hijos.extend([div1, div2])
div1.hijos.append(NodoHTML("p"))

# Iniciar interfaz
root.mainloop()