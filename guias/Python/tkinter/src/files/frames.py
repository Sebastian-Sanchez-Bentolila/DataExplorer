import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Frames
# Crear un marco
frame = tk.Frame(ventana, bd=2, relief=tk.SUNKEN)
frame.pack(padx=10, pady=10)

# Añadir widgets al marco
etiqueta = tk.Label(frame, text="Dentro del marco")
etiqueta.pack()

boton = tk.Button(frame, text="Botón en el marco")
boton.pack()

# Iniciar el bucle principal
ventana.mainloop()

