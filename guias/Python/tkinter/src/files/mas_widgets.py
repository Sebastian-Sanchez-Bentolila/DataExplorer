import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Checkbuttons
var1 = tk.IntVar()
var2 = tk.IntVar()

check1 = tk.Checkbutton(ventana, text="Opción 1", variable=var1)
check2 = tk.Checkbutton(ventana, text="Opción 2", variable=var2)

check1.pack()
check2.pack()

# Radiobuttons
def seleccionar():
    print(f"Seleccionaste la opción {opcion.get()}")

opcion = tk.StringVar()
opcion.set("1")

radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value="1", command=seleccionar)
radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=opcion, value="2", command=seleccionar)

radio1.pack()
radio2.pack()

# Listbox
listbox = tk.Listbox(ventana)
listbox.insert(1, "Elemento 1")
listbox.insert(2, "Elemento 2")
listbox.insert(3, "Elemento 3")

listbox.pack()

# Iniciar el bucle principal
ventana.mainloop()

