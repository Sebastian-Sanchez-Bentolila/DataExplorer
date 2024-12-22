import re
    
# Patrón y cadena
patron = r"\d+"
cadena = "Los números son 123, 456 y 789."
reemplazo = "#"
    
# Reemplazar todas las coincidencias en la cadena
resultado = re.sub(patron, reemplazo, cadena)
    
print("Resultado:", resultado)