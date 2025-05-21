import tkinter as tk

def invertir_frase():
    frase = entrada.get()
    palabras = frase.split()
    pila = []

    for palabra in palabras:
        pila.append(palabra)

    invertida = ""
    while pila:
        invertida += pila.pop() + " "

    resultado.config(text=invertida.strip())

# Crear ventana
ventana = tk.Tk()
ventana.title("Inversión de Palabras")
ventana.geometry("400x200")

# Widgets
tk.Label(ventana, text="Escribe una frase:").pack(pady=10)
entrada = tk.Entry(ventana, width=40)
entrada.pack()

tk.Button(ventana, text="Invertir", command=invertir_frase).pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="black")
resultado.pack(pady=10)

# Ejecutar
ventana.mainloop()
