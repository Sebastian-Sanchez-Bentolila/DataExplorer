# Definir un número complejo
z <- complex(real = 3, imaginary = 4)

# Operaciones básicas
Re(z)  # Parte real
Im(z)  # Parte imaginaria
Mod(z) # Módulo
Conj(z) # Conjugado

# Graficar en el plano complejo
library(ggplot2)

graficar_complejo <- function(z) {
df <- data.frame(x = c(0, Re(z)), y = c(0, Im(z)))
        
ggplot(df, aes(x, y)) +
    geom_segment(aes(xend = Re(z), yend = Im(z)), arrow = arrow(type="closed", length = unit(0.2, "inches")), color="red") +
    geom_hline(yintercept = 0, linetype="dashed") +
    geom_vline(xintercept = 0, linetype="dashed") +
    theme_minimal() +
    labs(title = paste("Número Complejo:", z), x = "Parte Real", y = "Parte Imaginaria")
}

# Ejemplo de graficado
graficar_complejo(z)