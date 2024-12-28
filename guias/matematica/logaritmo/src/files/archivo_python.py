# Importar bibliotecas
import math
import numpy as np
import matplotlib.pyplot as plt

# Cálculo de logaritmos
base_10 = math.log10(1000)  # Logaritmo base 10
base_e = math.log(10)       # Logaritmo natural (base e)
base_2 = math.log2(32)      # Logaritmo base 2
print(f"Log base 10: {base_10}, Log natural: {base_e}, Log base 2: {base_2}")

# Graficar logaritmos
x = np.linspace(1, 100, 100)
y_base_10 = np.log10(x)
y_natural = np.log(x)

plt.plot(x, y_base_10, label="Log Base 10")
plt.plot(x, y_natural, label="Log Natural")
plt.title("Logaritmos en Python")
plt.xlabel("x")
plt.ylabel("log(x)")
plt.legend()
plt.grid()
plt.show()