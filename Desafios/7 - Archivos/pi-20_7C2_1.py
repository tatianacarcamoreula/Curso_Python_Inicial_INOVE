
# CODE:39
# IMPORTANTE: NO borrar los comentarios

import csv


def desafio(ambientes):
    print('Ejercicios con archivos CSV complejos')
    archivo = 'propiedades.csv'
    
    with open ('propiedades.csv') as csvfile:
        propiedades = list(csv.DictReader(csvfile))
        
    cantidad_ambiente_2 = 0
    cantidad_ambiente_3 = 0
    
    
    for i in range(len(propiedades)):
        if propiedades[i].get("ambientes") == "2":
                cantidad_ambiente_2 += 1
        elif propiedades[i].get("ambientes") == "3":
                cantidad_ambiente_3 += 1
                
    if ambientes == "2_ambientes":
        print(f"Hay {cantidad_ambiente_2} departamentos de 2 ambientes")
        return cantidad_ambiente_2
    elif ambientes == "3_ambientes":
        print (f" Hay {cantidad_ambiente_3} departamentos de 3 ambientes")
        return cantidad_ambiente_3
    
def desafio_2(ambientes):
    with open('propiedades.csv') as csvfile:
        propiedades = list(csv.DictReader(csvfile))
    cantidad_ambiente_3 = 0
    cantidad_ambiente_2 = 0
    if ambientes == "2_ambientes":
        for i in range(len(propiedades)):
            if propiedades[i].get("ambientes") == "2":
                cantidad_ambiente_2 += 1
        print(f"Hay {cantidad_ambiente_2} departamentos de 2 ambientes")
        return cantidad_ambiente_2
    
    elif ambientes == "3_ambientes":
        for i in range(len(propiedades)):
            if propiedades[i].get("ambientes") == "3":
                cantidad_ambiente_3 += 1
        print (f" Hay {cantidad_ambiente_3} departamentos de 3 ambientes")
        return cantidad_ambiente_3
            
    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.
    
    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de ddepartamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio("2_ambientes")
    desafio_2("3_ambientes")