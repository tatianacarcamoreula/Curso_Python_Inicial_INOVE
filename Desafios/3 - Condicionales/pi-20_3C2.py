
# CODE:16
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Deberá solicitar tres números decimales por consola,
cada nuḿero de temperatura lo debe almacenar
en variables llamadas:
-> temperatura_1
-> temperatura_2
-> temperatura_3

Luego, mediante el uso de condicionales, deberá determinar
cuales de ellas es la mayor temperatura. Deberá almacenar
el valor de la temperatura más alta en una nueva variable
llamada:
--> temperatura_max

Luego, mediante el uso de condicionales, deberá determinar
cuales de ellas es la menor temperatura. Deberá almacenar
el valor de la temperatura más baja en una nueva variable
llamada:
--> temperatura_min

- Al final imprimir en pantalla la variable temperatura_max
  y temperatura_min
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
temperatura_1 = float(input("Ingrese primera temperatura:\n"))
temperatura_2 = float(input("Ingrese segunda temperatura:\n"))
temperatura_3 = float(input("Ingrese tercera temperatura:\n"))
temperatura_max = float
temperatura_min = float

if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
  temperatura_max = temperatura_1
elif temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
  temperatura_max = temperatura_2
else:
  temperatura_max = temperatura_3
  
if temperatura_1 < temperatura_2 and temperatura_1 < temperatura_3:
  temperatura_min = temperatura_1
elif temperatura_2 < temperatura_1 and temperatura_2 < temperatura_3:
  temperatura_min = temperatura_2
else:
  temperatura_min = temperatura_3
  
print(temperatura_max)
print(temperatura_min)
