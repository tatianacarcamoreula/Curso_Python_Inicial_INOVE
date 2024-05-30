
# CODE:25
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada suma_total
  para almacenar la suma de todas las temperatruas
  que se encuentran en la lista.
  Utilice un bucle y el operador incremento en cada
  iteración para lograr calcular la suma

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

- Al final imprimir en pantalla todas las variables
'''

print('Estado del clima')
# Empezar aquí la resolución del ejercicio
temperaturas = [12.8, 18.6, 14.5, 27.8, 12.1, 26.2, 13.5, 18.6,
                  14.7, 19.6, 21.2, 31.4]


suma_total = 0
for temperatura in temperaturas:
    suma_total += temperatura
    
cantidad_temperaturas = len(temperaturas)

promedio = suma_total / cantidad_temperaturas

print(suma_total, cantidad_temperaturas, promedio)