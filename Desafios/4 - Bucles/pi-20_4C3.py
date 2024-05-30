
# CODE:27
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada suma_total
  para almacenar la suma de todas las temperatruas
  que se encuentran en la lista.
  Utilice la función de python "sum" para calcular
  el valor de la suma_total

- Crear una una variable llamada cantidad_temperaturas
  para almacenar la cantidad de registros de tempereturas,
  es decir, la cantidad de elementos que hay en la
  variable lista temperaturas.
  Utilice la función len para obtener esta cantidad

- Calcular el promedio de temperatura del día
  realizando la división entre la suma total de
  temperaturas (suma_total) y la cantidad
  de registros de temperetura (cantidad_temperaturas)
  Almacene el resultado del promedio en una variable
  llamada promedio.

- Crear una una variable llamada temperatura_max
  para almacenar la máxima temperatura
  que se encuentran en la lista.
  Utilice la función de python "max" para calcular
  el valor de la temperatura_max

- Crear una una variable llamada temperatura_min
  para almacenar la mínima temperatura
  que se encuentran en la lista.
  Utilice la función de python "min" para calcular
  el valor de la temperatura_min

- Al final imprimir en pantalla todas las variables
'''

print('¡Estado del clima aumentado!')
# Empezar aquí la resolución del ejercicio
temperaturas = [12.8, 18.6, 14.5, 27.8, 12.1, 26.2, 13.5, 18.6,
                  14.7, 19.6, 21.2, 31.4]
suma_total = sum(temperaturas)
cantidad_temperaturas = len(temperaturas)
promedio = suma_total / cantidad_temperaturas
temperatura_max = max(temperaturas)
temperatura_min = min(temperaturas)
print(suma_total, cantidad_temperaturas, temperatura_max, temperatura_min)