
# CODE:33
# IMPORTANTE: NO borrar los comentarios

# --------------------------------
# Alumno:
# Aquí copiar la función "generar_invitados"
# ya elaborada
def generar_invitados():
    lista_invitados = []
    for i in range(3):
        invitado = str(input("Ingrese el nombre del invitado:\n"))
        lista_invitados.append(invitado)
    return lista_invitados
# --------------------------------

# --------------------------------
# Alumno:
# Aquí copiar la función "ordenar"
# ya elaborada
def ordenar(numeros):
    orden = sorted(numeros)
    return orden
# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: 
    # Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bloque "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenarla

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el retorno en "lista_invitados"

    # lista_invitados = generar_invitados()
    lista_invitados = generar_invitados()
    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada
    #    --> Almacenar el retorno en "lista_invidatos_ordenada"

    # lista_invidatos_ordenada = ordenar(lista_invitados)
    lista_invidatos_ordenada = ordenar(lista_invitados)
    # Imprimir en pantalla "lista_invidatos_ordenada":
    print(f"La lista de invitados ordenada es: {lista_invidatos_ordenada}")
    print("terminamos")
