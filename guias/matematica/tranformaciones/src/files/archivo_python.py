import numpy as np
import matplotlib.pyplot as plt

# Definimos los puntos
points = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
transform = np.array([[2, 0], [0, 1]])
transformed_points = points @ transform.T

# Graficamos
plt.scatter(points[:, 0], points[:, 1], color='blue', label='Original')
plt.scatter(transformed_points[:, 0], transformed_points[:, 1], color='red', label='Transformado')
plt.legend()
plt.grid(True)
plt.show()