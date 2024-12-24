# Ejemplo de diferentes tipos de datos
entero = 10
flotante = 3.14
cadena = "Hola, Python!"
booleano = True
lista = [1, 2, 3]
tupla = (1, 2, 3)
diccionario = {"clave": "valor"}
conjunto = {1, 2, 3}

print(entero, flotante, cadena, booleano)
print(lista, tupla, diccionario, conjunto)


# Ejemplo de condicional
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
    
# Ejemplo de bucle for
for i in range(5):
    print(i)

# Ejemplo de bucle while
contador = 0
while contador < 5:
    print(contador)
    contador += 1


# Ejemplo de función   
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Python"))


# Ejemplo de manejo de excepciones
try:
    numero = int(input("Ingresa un número: "))
    print(f"El número ingresado es {numero}")
except ValueError:
    print("Eso no es un número válido")
finally:
    print("Fin del programa")