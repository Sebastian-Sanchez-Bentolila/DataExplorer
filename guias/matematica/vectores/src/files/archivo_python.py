# Importamos las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Vectores en R2
v1 = np.array([2, 3])
v2 = np.array([-1, 4])

# Graficar vectores
plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='v1')
plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='v2')
plt.xlim(-2, 5)
plt.ylim(-1, 5)
plt.grid()
plt.legend()
plt.show()

# Definimos el vector en R3
vector = np.array([3, 4, 5])  # Cambia estos valores para otros vectores

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origen del vector
origin = np.array([0, 0, 0])

# Graficar el vector
ax.quiver(origin[0], origin[1], origin[2], 
          vector[0], vector[1], vector[2], 
          color='dodgerblue', arrow_length_ratio=0.1, linewidth=2)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Configuración de límites
ax.set_xlim([0, max(vector[0], 1)])
ax.set_ylim([0, max(vector[1], 1)])
ax.set_zlim([0, max(vector[2], 1)])

# Título
ax.set_title('Vector en R³')

# Mostrar el gráfico
plt.show()