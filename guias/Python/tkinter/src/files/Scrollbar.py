import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Establecer el título de la ventana
ventana.title("Mi primera aplicación")

# Establecer el tamaño de la ventana
ventana.geometry("400x300")

# Scrollbar
scrollbar = tk.Scrollbar(ventana)
listbox = tk.Listbox(ventana, yscrollcommand=scrollbar.set)

for i in range(100):
    listbox.insert(tk.END, f"Elemento {i+1}")

scrollbar.config(command=listbox.yview)

listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

ventana.mainloop()

# Iniciar el bucle principal
ventana.mainloop()

