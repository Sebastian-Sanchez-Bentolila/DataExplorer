import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Gestión de archivos
from tkinter import filedialog

def abrir_archivo():
    archivo = filedialog.askopenfilename()
    if archivo:
        with open(archivo, "r") as file:
            print(file.read())

boton_abrir = tk.Button(ventana, text="Abrir Archivo", command=abrir_archivo)
boton_abrir.pack()

# Iniciar el bucle principal
ventana.mainloop()

