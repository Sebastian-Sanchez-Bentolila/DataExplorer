import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Hola, Tkinter!")
etiqueta.pack()

# Crear un botón
boton = tk.Button(ventana, text="Haz clic aquí")
boton.pack()

# Crear una entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Iniciar el bucle principal
ventana.mainloop()

