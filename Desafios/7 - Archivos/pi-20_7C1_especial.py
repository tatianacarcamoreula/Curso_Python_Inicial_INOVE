
# CODE:38
# IMPORTANTE: NO borrar los comentarios

import csv


def desafio():
    print('Ejercicio de archivos')
    archivo = 'stock.csv'
    
    with open ('stock.csv') as csvfile:
        stock = list(csv.DictReader(csvfile))
    try:
        material = str(input("Ingrese el material del que usted quiera saber el stock total:\n")).lower()
        stock_total = 0
        for i in range(len(stock)):
            cantidad_material = int(stock[i][material])
            stock_total += cantidad_material
        print (f"el stock total de {material} es: {stock_total}")

    except:
        print("El material ingresado no se encuentra en el archivo.")
        
    return stock_total
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
    

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio()
