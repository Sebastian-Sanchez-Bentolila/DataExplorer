import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Método grid()
etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta1.grid(row=0, column=0)

etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
etiqueta2.grid(row=1, column=1)

# Iniciar el bucle principal
ventana.mainloop()

