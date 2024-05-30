
# CODE:38
# IMPORTANTE: NO borrar los comentarios

import csv


def desafio():
    print('Ejercicio de archivos')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Al final de esta función retornar (return) el stock total de tornillos
    # Comenzar aquí, recuerde el identado dentro de esta funcion
    with open ('stock.csv') as csvfile:
        stock = list(csv.DictReader(csvfile))
        
    cantidad_de_tornillos = 0
    
    for i in range(len(stock)):
        cantidad_tornillos  = int(stock[i]["tornillos"])
        cantidad_de_tornillos += cantidad_tornillos
    print(f"La cantidad total de tornillos es: {cantidad_de_tornillos}")
    return cantidad_de_tornillos

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()
