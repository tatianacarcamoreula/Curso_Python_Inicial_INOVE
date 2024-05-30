
# CODE:17
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Crear una variable llamada puntaje inicializada,
  en cero. Esta variable la deberá incrementar en 10
  por cada respuesta correcta.

- Deberá imprimir en consola una pregunta por vez,
  y con la función input en cada caso solicitar una respuesta
  por cada pregunta realizada.

- Utilizar condicionales para evaluar si la respuesta
  ingresada por el usuario coincide con la respuesta
  del programa (las variables).

- Cada respuesta ingresada por el usuario por consola
  la deberá pasar a minúsculas utilizando la función
  lower (cómo se vio los ejemplos de clase)
'''

print('Juego de trivia')
puntaje = 0

pregunta_1 = "¿Cuál es la capital de Argentina?"
respuesta_1 = "buenos aires"

pregunta_2 = "¿Cuál es la capital de Perú?"
respuesta_2 = "lima"

pregunta_3 = "¿Cuál es la capital de Uruguay?"
respuesta_3 = "montevideo"

pregunta_4 = "¿Cuál es la capital de Colombia?"
respuesta_4 = "bogota"

pregunta_5 = "¿Cuál es la capital de Venezuela?"
respuesta_5 = "caracas"

# Empezar aquí la resolución del ejercicio

print(pregunta_1)
respuesta1 = str(input(""))
if respuesta1.lower() == respuesta_1:
    puntaje += 10

print(pregunta_2)
respuesta2 = str(input(""))
if respuesta2.lower() == respuesta_2:
    puntaje += 10
    
print(pregunta_3)
respuesta3 = str(input(""))
if respuesta3.lower() == respuesta_3:
    puntaje += 10

print(pregunta_4)
respuesta4 = str(input(""))
if respuesta4.lower() == respuesta_4:
    puntaje += 10

print(pregunta_5)
respuesta5 = str(input(""))
if respuesta5.lower() == respuesta_5:
    puntaje += 10

print(puntaje)