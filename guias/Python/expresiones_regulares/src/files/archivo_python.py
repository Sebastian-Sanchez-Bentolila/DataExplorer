import re
    
# Patrón y cadena
patron = r"hola"
cadena = "hola mundo"
    
# Comprobar coincidencia al inicio de la cadena
coincidencia = re.match(patron, cadena)
    
if coincidencia:
    print("¡Coincidencia encontrada!")
else:
    print("No se encontró coincidencia.")
    
    
import re
    
# Patrón y cadena
patron = r"mundo"
cadena = "hola mundo"
    
# Buscar primera coincidencia en la cadena
coincidencia = re.search(patron, cadena)
    
if coincidencia:
    print("¡Coincidencia encontrada!")
else:
    print("No se encontró coincidencia.")
    
    
import re
    
# Patrón y cadena
patron = r"\d+"
cadena = "Los números son 123, 456 y 789."
    
# Encontrar todas las coincidencias en la cadena
coincidencias = re.findall(patron, cadena)
    
print("Coincidencias encontradas:", coincidencias)


import re
    
# Patrón y cadena
patron = r"\b\w+\b"
cadena = "Este es un ejemplo."
    
# Iterar sobre todas las coincidencias en la cadena
for coincidencia in re.finditer(patron, cadena):
    print("Coincidencia encontrada:", coincidencia.group())
    

import re
    
# Patrón y cadena
patron = r"\d+"
cadena = "Los números son 123, 456 y 789."
reemplazo = "#"
    
# Reemplazar todas las coincidencias en la cadena
resultado = re.sub(patron, reemplazo, cadena)
    
print("Resultado:", resultado)