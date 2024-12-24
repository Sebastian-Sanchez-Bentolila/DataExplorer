import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Cuadro de diálogo
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Información", "Esto es un cuadro de diálogo")

boton = tk.Button(ventana, text="Mostrar Mensaje", command=mostrar_mensaje)
boton.pack()

# Iniciar el bucle principal
ventana.mainloop()

