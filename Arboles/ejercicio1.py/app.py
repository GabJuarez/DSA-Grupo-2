from flask import Flask, render_template, request
from impresion_arbol import obtener_jerarquia_html

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class NodoEmpleado:
    def __init__(self, empleado):
        self.subordinados = []
        self.empleado = empleado
    
    def buscar_nodo(self, nombre_objetivo):
        if self.empleado.nombre == nombre_objetivo:
            return self
        for sub in self.subordinados:
            resultado = sub.buscar_nodo(nombre_objetivo)
            if resultado:
                return resultado
        return None
    
    def agregar_subordinado(self, nombre_jefe, nombre_subordinado):
        jefe = self.buscar_nodo(nombre_jefe)
        if jefe:
         nuevo_subordinado = NodoEmpleado(Empleado(nombre_subordinado))
         jefe.subordinados.append(nuevo_subordinado)
         return True  
        else:
            print(f"No se encontró al jefe {nombre_jefe} en la jerarquía.")
        return False  

    
    
def calcular_profundidad(nodo):
    if nodo is None:
        return 0
    
    if not nodo.subordinados:
        return 1
    
    return 1 + max(calcular_profundidad(hijo) for hijo in nodo.subordinados)

app = Flask(__name__)

ceo = None #la raiz

@app.route("/", methods = ['GET', 'POST'])
def index():
    global ceo
    mensaje = ""

    if request.method == 'POST':
        if not ceo:
            nombre_ceo = request.form.get('nombre_ceo')
            ceo = NodoEmpleado(Empleado(nombre_ceo))
            mensaje = f"CEO {nombre_ceo} agregado correctamente"
        else:
            nombre_jefe = request.form.get('nombre_jefe')
            nombre_sub = request.form.get('nombre_sub')
            if ceo.agregar_subordinado(nombre_jefe, nombre_sub):
                mensaje =  "empleado agregado"
            else:
                mensaje = f"Error, jefe {nombre_jefe} no fue encontrado"

    jerarquia = obtener_jerarquia_html(ceo) if ceo else ""
    profundidad = calcular_profundidad(ceo) if ceo else 0

    return render_template(
        "index.html",
        ceo = ceo,
        jerarquia = jerarquia,
        profundidad = profundidad,
        mensaje = mensaje
    )
        
   
if __name__ == '__main__':
    app.run(debug=True)
   