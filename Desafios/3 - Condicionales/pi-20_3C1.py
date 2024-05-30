
# CODE:15
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada numero_1
  para almacenar el primer número entero que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número entero que usted
  debe ingresar por consola con la función input

- Calcular la diferencia entre ambos números
  y almacenar el resultado en una variable

- Utilizando if elif y else compare el resutaldo
-> Si el resultado es positivo, almacenar 1 en res_1
-> Si el resultado es negativo, almacenar 2 en res_1
-> Si el resultado es cero, almacenar 3 en res_1

- Al final imprimir en pantalla la variable res_1
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = int(input("ingrese un numero entero:\n"))
numero_2 = int(input("ingrese otro numero entero:\n"))
diferencia_resultado = numero_1 - numero_2
res_1 = 0

if diferencia_resultado > 0:
  res_1 = 1
elif diferencia_resultado < 0:
  res_1 = 2
else:
  res_1 = 3

print(res_1)