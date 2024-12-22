# R basico

# Asignación de un número a una variable
mi_numero <- 42

# Asignación de una cadena de texto a una variable
mi_texto <- "Hola, mundo!"

# Mostrar los valores de las variables
print(mi_numero)
print(mi_texto)


# Suma
suma <- 5 + 3

# Resta
resta <- 10 - 4

# Multiplicación
multiplicacion <- 7 * 6

# División
division <- 20 / 5

# Mostrar los resultados
print(suma)
print(resta)
print(multiplicacion)
print(division)


# Crear un vector de números
numeros <- c(1, 2, 3, 4, 5)

# Acceder a elementos del vector
primer_elemento <- numeros[1]
tercer_elemento <- numeros[3]

# Mostrar los elementos
print(primer_elemento)
print(tercer_elemento)


# Definir una función
cuadrado <- function(x) {
  return(x^2)
}

# Usar la función
resultado <- cuadrado(4)

# Mostrar el resultado
print(resultado)


# Instalar y cargar ggplot2
install.packages("ggplot2")
library(ggplot2)

# Crear datos de ejemplo
datos <- data.frame(
  x = rnorm(100),
  y = rnorm(100)
)

# Crear gráfico de dispersión
ggplot(datos, aes(x = x, y = y)) +
  geom_point() +
  labs(title = "Gráfico de Dispersión de Datos Aleatorios",
       x = "Eje X",
       y = "Eje Y")


# Crear datos de ejemplo
datos_barras <- data.frame(
  categoria = c("A", "B", "C", "D"),
  valor = c(3, 12, 5, 8)
)

# Crear gráfico de barras
ggplot(datos_barras, aes(x = categoria, y = valor)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "Gráfico de Barras", x = "Categoría", y = "Valor")


# Crear datos de ejemplo
datos_lineas <- data.frame(
  tiempo = 1:10,
  valor = c(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
)

# Crear gráfico de líneas
ggplot(datos_lineas, aes(x = tiempo, y = valor)) +
  geom_line(color = "blue") +
  labs(title = "Gráfico de Líneas", x = "Tiempo", y = "Valor")


# Crear datos de ejemplo
datos_caja <- data.frame(
  grupo = rep(c("A", "B", "C"), each = 20),
  valor = c(rnorm(20, mean = 5), rnorm(20, mean = 10), rnorm(20, mean = 15))
)

# Crear gráfico de caja y bigotes
ggplot(datos_caja, aes(x = grupo, y = valor)) +
  geom_boxplot(fill = "lightgreen") +
  labs(title = "Gráfico de Caja y Bigotes", x = "Grupo", y = "Valor")


# Instalar y cargar dplyr
install.packages("dplyr")
library(dplyr)

# Crear datos de ejemplo
datos <- data.frame(
  nombre = c("Ana", "Luis", "Carla", "Jorge"),
  edad = c(23, 30, 25, 35)
)

# Filtrar datos para edades mayores de 25
datos_filtrados <- filter(datos, edad > 25)

# Mostrar los datos filtrados
print(datos_filtrados)


# Seleccionar la columna 'nombre'
datos_nombres <- select(datos, nombre)

# Mostrar los nombres
print(datos_nombres)


# Agregar una columna 'edad_al_doble'
datos_mutados <- mutate(datos, edad_al_doble = edad * 2)

# Mostrar los datos mutados
print(datos_mutados)


# Crear datos de ejemplo
datos <- data.frame(
  grupo = c("A", "A", "B", "B"),
  valor = c(10, 15, 20, 25)
)

# Calcular la media de 'valor' por grupo
datos_resumidos <- datos %>%
  group_by(grupo) %>%
  summarize(media_valor = mean(valor))

# Mostrar los datos resumidos
print(datos_resumidos)


# Crear datos de ejemplo
grupo_a <- c(10, 12, 14, 16, 18)
grupo_b <- c(20, 22, 24, 26, 28)

# Realizar prueba t
resultado_prueba_t <- t.test(grupo_a, grupo_b)

# Mostrar resultados
print(resultado_prueba_t)


# Crear datos de ejemplo
datos_regresion <- data.frame(
  x = c(1, 2, 3, 4, 5),
  y = c(2, 4, 5, 7, 10)
)

# Ajustar modelo de regresión lineal
modelo <- lm(y ~ x, data = datos_regresion)

# Mostrar resumen del modelo
summary(modelo)
