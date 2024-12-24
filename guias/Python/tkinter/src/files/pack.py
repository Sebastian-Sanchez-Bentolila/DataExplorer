import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Método pack()
etiqueta1 = tk.Label(ventana, text="Etiqueta 1")
etiqueta1.pack(side=tk.TOP)

etiqueta2 = tk.Label(ventana, text="Etiqueta 2")
etiqueta2.pack(side=tk.LEFT)

etiqueta3 = tk.Label(ventana, text="Etiqueta 3")
etiqueta3.pack(side=tk.BOTTOM)

etiqueta4 = tk.Label(ventana, text="Etiqueta 4")
etiqueta4.pack(side=tk.RIGHT)

# Iniciar el bucle principal
ventana.mainloop()

