import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Canvas
canvas = tk.Canvas(ventana, width=300, height=200)
canvas.pack()

# Dibujar un rectángulo
canvas.create_rectangle(50, 50, 250, 150, fill="blue")

# Dibujar un óvalo
canvas.create_oval(75, 75, 225, 125, fill="red")

# Iniciar el bucle principal
ventana.mainloop()

