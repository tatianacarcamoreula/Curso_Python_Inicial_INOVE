
# CODE:23
# IMPORTANTE: NO borrar los comentarios

# Alumno:
# Usted ya cuenta con la lista temperaturas
# Crear una variable llamada mayores_25
# inicializada en cero
# Realiza un bucle que recorra cada elemento
# En cada iteración incrementar el valor de mayores_25
# en 1 (con el operador incremento) por cada
# temperatura mayor a 25 en la lista

# TIP
# Utilice el debugger para ver como avanza
# el programa paso a paso
temperaturas = [12.8, 18.6, 14.5, 27.8, 12.1, 26.2, 13.5, 18.6,
                  14.7, 19.6, 21.2, 31.4,]

# Imprimir en pantalla la variable mayores_25
# La cantidad de temperaturas mayores a 25 deberá ser 3

mayores_25 = 0
for temperatura in temperaturas:
    if temperatura > 25:
        mayores_25 += 1
print(mayores_25)