
# CODE:34
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Realice una funcion llamada "lista_aleatoria" (fuera del blocke main)
la cual reciba como parámetro el rango de aceptación de la lista
"inicio y fin" y la cantidad de elementos que deseamos que
contenga la lista, es decir, la cantidad de elementos random a generar.

def lista_aleatoria (inicio, fin, cantidad)

- Dentro de la función deberá realizar un bucle que repita "cantidad"
veces esta operacion:
numero = random.randint(inicio, fin)

Cada valor generado lo debe guardar en una lista, recuerde:
1) Iniciar y crear esa lista vacia.
2) Para agregar nuevos elementos en la lista utiliza "append"

Finalmente dicha función debe retornar la lista de elementos random generados.
'''

# --------------------------------
# Aquí dentro definir la función lista_aleatoria
import random
def lista_aleatoria(inicio, fin, cantidad):
    elementos = []
    for i in range(cantidad):
        numero_aleatorio = random.randint(inicio, fin)
        elementos.append(numero_aleatorio)
    return elementos

# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    inicio = 0
    fin = 10
    cantidad = 5

    # Alumno: Luego de crear la función invocarla en este lugar:

    # mi_lista_aleatoria = lista_aleatoria(inicio, fin, cantidad)
    mi_lista_aleatoria = lista_aleatoria(inicio, fin, cantidad)
    # Imprimir en pantalla "mi_lista_aleatoria" que tendrá
    # los valores retornado por la función lista_aleatoria:
    print(f"Esta es la lista aleatoria:{mi_lista_aleatoria}")
    # print(mi_lista_aleatoria)

    print("terminamos")
