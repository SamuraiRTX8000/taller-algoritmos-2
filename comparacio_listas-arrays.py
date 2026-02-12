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

#ANÁLISIS DE RENDIMIENTO: LISTAS VS ARRAYS

# 1) Diferencias en tiempo de ejecución
# Se observó que el array fue considerablemente más rápido que la lista.
# Tiempo lista: 0.1098 segundos
# Tiempo array: 0.0166 segundos
# El array ejecutó la operación aproximadamente 6 a 7 veces más rápido.
# Esto se debe a que los arrays (como los de NumPy) están optimizados
# para operaciones matemáticas y trabajan con código compilado en C,
# mientras que las listas ejecutan las operaciones elemento por elemento
# mediante el intérprete de Python.

# 2) Influencia del almacenamiento en memoria
# Las listas almacenan referencias a objetos en memoria, lo que implica
# mayor uso de memoria y más pasos para acceder a cada valor.
# En cambio, los arrays almacenan los datos de forma contigua y homogénea
# en memoria, lo que mejora la localidad de referencia y permite que
# el procesador acceda a los datos de manera más eficiente.
# Esta organización reduce el tiempo de acceso y procesamiento.

# 3) Elección para grandes volúmenes de datos
# Para procesar grandes volúmenes de datos numéricos, elegiría arrays.
# Son más eficientes en tiempo de ejecución, consumen menos memoria
# y están diseñados específicamente para cálculos matemáticos masivos.
# En aplicaciones donde el rendimiento es crítico, los arrays son
# la opción más adecuada.