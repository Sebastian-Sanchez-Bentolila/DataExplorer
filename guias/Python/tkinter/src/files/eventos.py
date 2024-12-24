import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Eventos
def cuando_haces_clic():
    print("¡Botón clicado!")

boton = tk.Button(ventana, text="Haz clic aquí", command=cuando_haces_clic)
boton.pack()

def hola():
    print("Hola!")

# Crear una barra de menú
barra_menu = tk.Menu(ventana)

# Crear un menú desplegable
menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=hola)
menu_archivo.add_command(label="Abrir", command=hola)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Añadir el menú desplegable a la barra de menú
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

# Configurar la ventana para usar la barra de menú
ventana.config(menu=barra_menu)

# Iniciar el bucle principal
ventana.mainloop()

