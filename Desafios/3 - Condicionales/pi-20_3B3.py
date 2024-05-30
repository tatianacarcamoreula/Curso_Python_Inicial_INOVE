
# CODE:13
# IMPORTANTE: NO borrar los comentarios

puntaje = int(input("Ingrese un valor entre 0 y 100:\n"))

# Alumno:
# Deberá crear una serie de considiconales
# con if y elif de forma tal de cargar en
# la variable nota la nota del alumno según
# las siguientes condiciones:

nota = ""

# Si el puntaje es mayor igual a 90 --> nota = "A"
# Sino, si el puntaje es mayor igual a 80 --> nota = "B"
# Sino, si el puntaje es mayor igual a 70 --> nota = "C"
# Sino, si el puntaje es mayor igual a 60 --> nota = "D"
# Sino, si el puntaje es menor a  60      --> nota = "F"

# Recuerde utilizar un solo bloque condicional
# armado de if y múltiples elif
# Puede consultar el ejemplo de clase 2 como referencia

if puntaje >= 90:
    nota = "A"
elif puntaje >= 80:
    nota = "B"
elif puntaje >= 70:
    nota = "C"
elif puntaje >= 60:
    nota = "D"
elif puntaje < 60:
    nota = "F"
    
# Imprimir en pantalla la variable nota
print(nota)