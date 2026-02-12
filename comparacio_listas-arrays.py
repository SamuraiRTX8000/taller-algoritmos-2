import time
import numpy as np

# cantidad de datos
n = 1000000

# Este es para crear una lista
lista = list(range(n))

# Este es para crear un array
array = np.arange(n)

# Esto es para pedir el tiempo con la ista
inicio_lista = time.time()

resultado_lista = [x * 2 for x in lista]

fin_lista = time.time()

# Esto es para medir el tiempo con el array
inicio_array = time.time()

resultado_array = array * 2

fin_array = time.time()

# Esto es para hacer la comparativa
print("Tiempo lista:", fin_lista - inicio_lista)
print("Tiempo array:", fin_array - inicio_array)

#Datos del codigo:
#Tiempo lista: 0.10985946655273438
#Tiempo array: 0.016683578491210938

