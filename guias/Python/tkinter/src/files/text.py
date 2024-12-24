import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Text
# Crear un widget Text
texto = tk.Text(ventana, height=10, width=30)
texto.pack()

# Insertar texto inicial
texto.insert(tk.END, "Escribe algo aquí...")

# Iniciar el bucle principal
ventana.mainloop()

