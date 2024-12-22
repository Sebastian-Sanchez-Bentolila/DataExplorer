# Ejemplo de manejo de excepciones
try:
    numero = int(input("Ingresa un número: "))
    print(f"El número ingresado es {numero}")
except ValueError:
    print("Eso no es un número válido")
finally:
    print("Fin del programa")