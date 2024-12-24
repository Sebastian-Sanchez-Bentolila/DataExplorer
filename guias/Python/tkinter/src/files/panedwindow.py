import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Panedwindow
# Crear una PanedWindow horizontal
panedwindow = tk.PanedWindow(ventana, orient=tk.HORIZONTAL)
panedwindow.pack(fill=tk.BOTH, expand=True)

# Añadir paneles
left = tk.Label(panedwindow, text="Panel Izquierdo")
panedwindow.add(left)

right = tk.Label(panedwindow, text="Panel Derecho")
panedwindow.add(right)

ventana.mainloop()

# Iniciar el bucle principal
ventana.mainloop()

