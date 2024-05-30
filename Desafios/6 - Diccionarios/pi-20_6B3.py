
# CODE:57
# IMPORTANTE: NO borrar los comentarios

# La función consultar_stock recibe
# por parámetro el stock de materiales existente
def consultar_stock(stock):
    print('Ejercicios con diccionarios')
    # Deberá consultar al usuario por "input"
    # de que material desea obtener el stock
    
    # El usuario ingresará un texto (ej: tornillos)
    # y usted deberá utilizar un condicional y el operdor "in"
    # para verificar si ese material está dentro del stock

    # Si el material está dentro del stock, se debe
    # retornar la cantidad de stock almacenado en
    # el diccionario para esa key

    # Si el material no está dentro dle stock, se debe
    # retornar 0

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    material = str(input("Ingrese el material del que desea obtener el stock: "))
    material_1 = material.lower()
    
    if material_1 in stock:
        for k, v in stock.items():
            if material_1 == k:
                print("El stock de", k, "es:", v)
                break
        return v
    else:
        print("No existe ese material. Intenta con otro")
        return 0
        
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Comenzamos con un diccioario creado de stock
    # de materiales:    
    stock = {'tornillos': 100, 'tuercas': 150, 'arandelas': 300}

    consultar_stock(stock)
