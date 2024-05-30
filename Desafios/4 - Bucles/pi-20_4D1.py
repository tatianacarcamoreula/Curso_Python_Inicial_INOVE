
# CODE:41
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Comience por crear una variable llamada resultado
  para almacenar la palabra final que usted arme
  segun el criterio establecido en el enunciado.

- Deberá proveer por consola la palabra objetivo a ordenar
  la cual se almacenará en la variable llmada objetivo
- Deberá utilizar bucles para recorrer la palabra objetivo
  y deberá usar listas y todo método de strings a su disposición
  que lo ayude a resolver este desafio.
'''

print("Ordenar caracteres")
objetivo = input("Ingrese palabra de entrada:\n")
# Empezar aquí la resolución del ejercicio

minuscula = []
mayuscula = []
digito = []
digito_par = []
digito_impar = []

for letra in objetivo:
    if letra.islower():
        minuscula.append(letra)
    elif letra.isupper():
        mayuscula.append(letra)
    elif letra.isdigit():
        digito.append(letra)
        
for numero in digito:
    entero = int(numero)
    if entero % 2 == 0:
        digito_par.append(entero)
    else:
        digito_impar.append(entero)
           
orden_minuscula = sorted(minuscula)
orden_mayuscula = sorted(mayuscula)
orden_digito_par = sorted(digito_par)
orden_digito_impar = sorted(digito_impar)

Lista_mayor = orden_minuscula + orden_mayuscula + orden_digito_impar + orden_digito_par
resultado = ''.join(str(i) for i in Lista_mayor)

print(resultado)