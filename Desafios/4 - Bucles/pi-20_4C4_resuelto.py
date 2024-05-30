
# CODE:X
# IMPORTANTE: NO borrar los comentarios

'''
Alumno:
- Comience por generar el bucle While True
- Dentro del bucle imprima con prints el menú
  de opciones en consola.

- Crear una una variable llamada numero_1
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada numero_2
  para almacenar el primer número decimal que usted
  debe ingresar por consola con la función input

- Crear una una variable llamada operacion
  para almacenar la operación que se desea efectuar
  ingresada por consola con la función input
  Los valores que puede tomar la variable operacion van
  del "1" al "5", su programa no debe explotar si se ingresa
  otro texto distinto, como por ejemplo "uno", "hola", etc.

IMPORTANTE: Dentro del bucle primero debe solicitar al usuario
el ingreso de los dos números (numero_1 y numero_2) y luego
debe solicitar el ingreso de la operación a realizar
(debe respetar ese orden)

- Armar una serie de condicionales para evaluar
  que operación efectuar. Deberá guardar el resultado
  de la operación en una variable llamada resultado

- Si el usuario ingresa la operación de SALIR (opcion 5),
  deberá finalizar el bucle con la sentencia break.

- Si el usuario ingresa una opción fuera del rango
  solicitado de opciones, el programa no deberá 
  estallar, no deberá hacer nada permitiendo
  que el bucle While vuelva a realizar la consulta
  en la próxima iteración.
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

while True:

    print('''
    Ingrese la operación a realizar:
    - 1- Suma (+)
    - 2- Resta (-)
    - 3- Multiplicación (*)
    - 4- División (/)
    - 5- SALIR
    ''')

    # Ingreso de los dos números para operar.
    numero_1 = float(input('Ingrese el primer número del cálculo:\n'))
    numero_2 = float(input('Ingrese el segundo número del cálculo:\n'))
    
    # Selección de la operación a realizar
    operacion = input('Ingrese la operación a realizar:\n')    
  
    # Cálculos e impresión de operación y resultados.
    if operacion == '1':
        resultado = numero_1 + numero_2
        print(f'{numero_1} + {numero_2} = {resultado}')

    elif operacion == '2':
        resultado = numero_1 - numero_2
        print(f'{numero_1} - {numero_2} = {resultado}')

    elif operacion == '3':
        resultado = numero_1 * numero_2
        print(f'{numero_1} x {numero_2} = {resultado}')

    elif operacion == '4':
        resultado = numero_1 / numero_2
        print(f'{numero_1} / {numero_2} = {resultado}')

    elif operacion == "5":
        print('¡Gracias por usar esta app!')
        # salir del bucle
        break
    else:
        print('Error en la operación seleccionada.')

