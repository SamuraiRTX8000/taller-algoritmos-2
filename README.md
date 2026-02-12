# SISTEMA PARA GESTIONAR NOTAS

## DESCRIPCIÓN

Este proyecto es un programa que permite gestionar las calificaciones de un grupo de estudiantes desde la consola.

El sistema permite:

- Ver las notas registradas.
- Modificar una nota existente.
- Agregar nuevas notas.
- Crear una nueva lista de notas.
- Obtener un resumen estadístico (promedio, aprobados y reprobados).

Está diseñado como práctica para el manejo de:

- Listas
- Funciones
- Ciclos `for`
- Condicionales
- Validación de datos
- Estructura `match-case` (Python 3.10+)


## REQUISITOS

- Python 3.10 o superior (usa `match-case`).

Para verificar tu versión:


python --version


## COMO EJECUTAR EL PROGRAMA

1. Guarda el archivo con un nombre.


2. Ejecuta el programa desde la terminal.


3. Sigue las instrucciones del menú en pantalla.


## ESTRUCTURA DEL PROGRAMA

### `ver_notas(notas)`

Muestra en pantalla todas las notas almacenadas junto con su índice (número de estudiante).

### `modificar_notas(notas)`

Permite:

1. Modificar una nota existente validando:
   - Que el índice exista.
   - Que la nueva nota esté entre 1.0 y 5.0.
2. Agregar nuevas notas a la lista.

###  `resumen_notas(notas)`

Calcula y muestra:

- Número de estudiantes aprobados (nota ≥ 3.0)
- Número de estudiantes reprobados
- Promedio del grupo
- Porcentaje de aprobados
- Porcentaje de reprobados

###  `crear_lista()`

 Sepuede crear una nueva lista de notas desde cero, validando que cada nota esté entre 1.0 y 5.0.

Devuelve la nueva lista creada.

##  FUNCIONAMIENTO GENERAL

El programa inicia con una lista de notas predefinida:

    python
notas = [1.6, 3.5, 2.5, 4.0, 5.0]

Luego se ejecuta un menú interactivo dentro de un ciclo `while`, que permite al usuario seleccionar diferentes opciones hasta que decida salir.

##  REGLAS DEL SISTEMA

- Las notas deben estar entre **1.0 y 5.0**.
- Se considera aprobado con nota **mayor o igual a 3.0**.
- Se validan índices para evitar errores.
- Se valida que no se ingresen notas fuera del rango permitido.


## OBJETIVO DEL PROYECTO

Este proyecto tiene como finalidad practicar:

- Manipulación de listas
- Validación de datos
- Estructuras de control
- Funciones
- Cálculos matemáticos básicos
- Programación estructurada

- ## DECISIONES DE DISEÑO DEL PROGRAMA

### Uso de funciones

El programa fue dividido en funciones independientes con el objetivo de organizar mejor el código y separar responsabilidades.

Cada función cumple una tarea específica:

- `ver_notas()` solo muestra información.
- `modificar_notas()` administra cambios y agregados.
- `resumen_notas()` analiza los datos.
- `crear_lista()` construye una nueva colección.

Esta decisión permite:

- Evitar que todo el código esté en un solo bloque.
- Facilitar la lectura.
- Localizar errores más rápido.
- Reutilizar funciones sin repetir código.
- Mantener una estructura clara y ordenada.

Se aplicó el principio de **modularidad**, donde cada parte del sistema es independiente pero trabaja en conjunto.

---

### Uso de listas como estructura principal

Se eligió la lista como estructura de datos porque:

- El problema se basa en una colección de datos numéricos.
- Las listas permiten modificar, agregar y recorrer elementos fácilmente.
- Son dinámicas (pueden crecer o reducirse).

Dado que solo se trabajan datos numéricos (notas), no fue necesario usar estructuras más complejas como diccionarios u objetos.

---

### Uso de `enumerate()` en el recorrido

Se eligió el método `enumerate()` al recorrer las listas porque:

- Permite obtener simultáneamente el índice y el valor.
- El índice se usa como identificador del estudiante.
- Evita tener que crear contadores manuales.
- Reduce código innecesario.
- Hace el programa más claro y eficiente.

Esto permite que el usuario pueda seleccionar qué nota modificar usando el número mostrado en pantalla.

---

### Uso del menú interactivo

Se implementó un menú con ciclo `while` para:

- Permitir que el usuario interactúe continuamente con el sistema.
- Evitar que el programa termine después de una sola operación.
- Simular el comportamiento de una aplicación real.

El uso de `match-case` mejora la claridad en la selección de opciones y hace el flujo más organizado que múltiples `if-elif`.

---

### Validación de datos

Se incluyeron validaciones para:

- Evitar índices fuera del rango de la lista.
- Evitar notas menores a 1.0 o mayores a 5.0.
- Evitar cálculos cuando la lista está vacía.

Esto se hizo para prevenir errores de ejecución como:

- `IndexError`
- División entre cero
- Datos inconsistentes

La validación mejora la estabilidad del sistema.

---

### Decisión de reemplazar la lista en `crear_lista()`

Esta decisión permite:

- Reiniciar completamente los datos cuando sea necesario.
- Mantener independencia entre la lista anterior y la nueva.
- Evitar modificar accidentalmente datos antiguos.
- Simular un cambio de grupo o conjunto de estudiantes.

El reemplazo de la referencia garantiza que todas las funciones trabajen siempre con la lista más actualizada, sin duplicar código ni crear inconsistencias.

---

### Separación entre cálculo y visualización

Aunque las funciones imprimen resultados directamente, el cálculo se realiza antes de mostrar los datos. Esto mantiene una estructura lógica clara:

1. Se procesan los datos.
2. Se almacenan resultados en variables.
3. Se presentan al usuario.

Esto facilita futuras mejoras, como devolver valores en lugar de imprimirlos.

---

## Enfoque general del diseño

El programa sigue un enfoque de **programación estructurada**, utilizando:

- División en funciones.
- Flujo controlado por menú.
- Validación antes de operar.
- Uso eficiente de estructuras básicas.

El objetivo no fue solo que el programa funcione, sino que esté organizado, sea entendible y fácil de mantener.
