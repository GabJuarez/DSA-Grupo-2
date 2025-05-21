"""
Ejercicio #2: Verificación de paréntesis balanceados.
Escriba un programa que determine si una cadena de texto dada tiene los paréntesis ( ), { }, y [ ]
balanceados. Use una pila para realizar el seguimiento de los paréntesis abiertos.
"""

from tkinter import *

class TextosGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Verificación de Paréntesis Balanceados")
        self.master.geometry("700x450")
        self.master.configure(bg="black")

        self.parentesis = []
        self.resultados = []

        self.etiqueta = Label(master, text="Ingrese un texto con paréntesis:", 
                              font=("Times", 12), bg="black", fg="white")
        self.etiqueta.pack(pady=10)

        self.entradaTexto = Entry(master, font=("Times", 12), width=70)
        self.entradaTexto.pack(pady=10)

        self.botonAgregar = Button(master, text="Agregar Texto", command=self.agregarTexto, 
                                   font=("Times", 12), bg="black", fg="white")
        self.botonAgregar.pack(pady=5)

        self.botonValidar = Button(master, text="Validar Paréntesis", command=self.validarParentesis, 
                                   font=("Times", 12), bg="black", fg="white")
        self.botonValidar.pack(pady=5)

        self.resultadosArea = Text(master, height=10, width=70, font=("Times", 12), bg="gray")
        self.resultadosArea.pack(pady=10)

    def agregarTexto(self):
        TextoIngresado = self.entradaTexto.get()
        if any(p in TextoIngresado for p in '(){}[]'):
            self.parentesis.append(TextoIngresado)
            self.resultadosArea.insert(END, "Texto Agregado: \n" + TextoIngresado + "\n")
            self.entradaTexto.delete(0, END)
        else:
            self.resultadosArea.insert(END, "El texto no contiene paréntesis...\n")

    def validarParentesis(self):
        pares = {')': '(', '}': '{', ']': '['}
        self.resultados.clear()
        self.resultadosArea.insert(END, "\nValidación de Paréntesis\n")

        for i, TextoActual in enumerate(self.parentesis):
            pila = []
            balanceado = True

            for caracter in TextoActual:
                if caracter in '({[':
                    pila.append(caracter)
                elif caracter in ')}]':
                    if not pila or pila[-1] != pares[caracter]:
                        balanceado = False
                        break
                    pila.pop()
            
            if pila:
                balanceado = False
            
            estado = "Balanceado\n" if balanceado else "No Balanceado\n"
            self.resultadosArea.insert(END, "Texto No.{0}: {1} = {2}\n".format(i + 1, TextoActual, estado))

ventana = Tk()
app = TextosGUI(ventana)
ventana.mainloop()