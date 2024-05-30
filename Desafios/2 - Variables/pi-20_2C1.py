
# CODE:6
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Almacenar el valor de cada operación realizada en las
  variables que usted creará con los siguientes nombres:
  suma, resta, multiplicacion, division, potencia

- Al final imprimir todos los resultados almacenados
  en esas variables
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input("Ingrese el primer número decimal: "))
numero_2 = float(input("ingrese el segundo número decimal: "))

suma = numero_1 + numero_2
print("La suma de estos dos números es: ",suma)

resta = numero_1 - numero_2
print("La resta de estos dos números es: ",resta)

division = numero_1 / numero_2
print("La división de estos dos números es: ",division)

multiplicacion = numero_1 * numero_2
print("La multiplicación de estos dos números es: ",multiplicacion)

potencia = numero_1 ** numero_2
print("La potencia de estos dos números es: ",potencia)
