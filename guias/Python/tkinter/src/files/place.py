import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Método place()
etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta1.place(x=50, y=50)

# Iniciar el bucle principal
ventana.mainloop()

