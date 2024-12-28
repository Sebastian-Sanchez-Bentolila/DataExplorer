# Cálculo de logaritmos
log_base_10 <- log10(1000)  # Logaritmo base 10
log_base_e <- log(10)       # Logaritmo natural (base e)
log_base_2 <- log(32, base = 2)  # Logaritmo base 2
print(paste("Log base 10:", log_base_10))
print(paste("Log natural:", log_base_e))
print(paste("Log base 2:", log_base_2))

# Graficar logaritmos
x <- seq(1, 100, length.out = 100)
y_base_10 <- log10(x)
y_natural <- log(x)

plot(x, y_base_10, type = "l", col = "blue", lwd = 2, 
     xlab = "x", ylab = "log(x)", main = "Logaritmos en R")
lines(x, y_natural, col = "red", lwd = 2)
legend("topright", legend = c("Log Base 10", "Log Natural"), 
       col = c("blue", "red"), lwd = 2)