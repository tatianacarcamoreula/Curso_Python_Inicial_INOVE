
# CODE:3
# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ingrese su primer nombre y luego su primer apellido
nombre = str(input('Ingrese por consola su primer nombre:'))

apellido = str(input('Ingrese por consola su primer apellido:'))

# Alumno:
# Imprima en pantalla su nombre y apellido
# utilizando las variables nombre y apellido
print(nombre, apellido)

# Crear una variable llamada nombre_apellido donde se 
# almacene el contenido de las variables nombre y apellido
# separando con un nespacio su nombre de su apellido
nombre_apellido = nombre + (' ') + apellido
# Crear una variable llamada cantidad donde se
# almacene la cantidad de caracteres que posee la variable
# nombre_apellido utilizando la función len
cantidad = len(nombre_apellido)

# Imprimir en pantalla la variable cantidad
print(cantidad)
