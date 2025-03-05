# Definir un número complejo
z = complex(3, 4)

# Operaciones básicas
print("Parte real:", z.real)
print("Parte imaginaria:", z.imag)
print("Módulo:", abs(z))
print("Conjugado:", z.conjugate())

# Graficar números complejos
import matplotlib.pyplot as plt

def graficar_complejo(z):
    plt.figure(figsize=(5,5))
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.grid(True, linestyle='--', alpha=0.6)
            
    plt.quiver(0, 0, z.real, z.imag, angles='xy', scale_units='xy', scale=1, color='red')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.title(f'Número complejo {z}')
    plt.show()

# Ejemplo de graficado
graficar_complejo(z)