
# CODE:30
# IMPORTANTE: NO borrar los comentarios

def promedio(numeros):
    print("Funcion promedio")
    resultado = 0
    if numeros == []:
        return resultado
    else:
        sumatoria_numeros = sum(numeros)
        cantidad_numeros = len(numeros)
        promedio = sumatoria_numeros / cantidad_numeros
        return promedio
    # La función promedio recibe como parámetro una
    # lista de números. Con ella calcule el promedio como:

    # promedio = sumatoria_numeros / cantidad_numeros

    # Resuelva la sumatoria y la cantidad con las herramientas
    # que desee, recomendamos usar las funciones disponibles
    # de Python para ello:    
    # sum --> obtener la sumatoria de números
    # len --> obtener la cantidad de números

    # La función debe retornar (return) el promedio calculado
    # La función debe contemplar si se le pasa una lista vacia
    # (es decir, de "0" elementos), en ese caso se debe
    # retornar como promedio 0 y evitar que explote el programa

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    numeros = [2, 4, 6, 8, 10, 12]
    
    # Alumno:
    # Llamar a la función en este lugar y capturar el valor del retorno
    # en una variable llamada resultado_promedio
    resultado_promedio = promedio(numeros)
    # Luego imprimir en pantalla el valor resultante:
    # print(....)
    print(f"El promedio de la lista {numeros} es {resultado_promedio}")
    print("terminamos")
