
# CODE:10
# IMPORTANTE: NO borrar los comentarios

numero_1 = int(input('Ingrese el primer número:\n'))
numero_2 = int(input('Ingrese el segundo número:\n'))

# Alumno
# En cada desafio se le indicará que dada cierta condición
# modifique el valor de una variable

# Compare los dos números y entre sí 
# utilizando if y else.
# - Si numero_1 es mayor a numero_2, almacenar 1 en res_1
# - De lo contrario, almacenar 2 en res_1
res_1 = 0

if numero_1 > numero_2:
    res_1 = 1
else:
    res_1 = 2

# Imprimir en pantalla la variable res_1
print(res_1)

# Verifique si el numero_1 positivo, negativo o cero
# Utilice if, elif y else
# - Si numero_1 es positivo, almacenar 1 en res_2
# - Si numero_1 es negativo, almacenar 2 en res_2
# - Si numero_1 es cero, almacenar 3 en res_2
res_2 = 0

if numero_1 > 0:
    res_2 = 1
elif numero_1 < 0:
    res_2 = 2
else:
    res_2 = 3
    
# Imprimir en pantalla la variable res_2
print(res_2)

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Utilice un if con un condicional compuesto
# - Si se cumple la condición, almacenar 1 en res_3
# - De lo contrario, almacenar 2 en res_3
res_3 = 0

if numero_1 > 0 and numero_1 < 100:
    res_3 = 1
else:
    res_3 = 2
# Imprimir en pantalla la variable res_3
print(res_3)

# Verifique si:
# el numero_1 es menor a 10 o el numero_2 es mayor a -2
# Utilice un if con un condicional compuesto
# - Si se cumple la condición, almacenar 1 en res_4
# - De lo contrario, almacenar 2 en res_4
res_4 = 0

if numero_1 < 10 or numero_2 > -2:
    res_4 = 1
else:
    res_4 = 2

# Imprimir en pantalla la variable res_4
print(res_4)

