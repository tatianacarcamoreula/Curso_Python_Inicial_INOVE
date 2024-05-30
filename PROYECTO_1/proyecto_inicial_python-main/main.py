import random
import interfaz
########################################################################
def leer_palabra_secreta(palabras):
    palabra_secreta = random.choice(palabras)
    return palabra_secreta

def pedir_letra(letras_usadas):
    while True:
        letra = str(input("Ingrese una letra: \n")).lower()
        if letra == "fin":
            return "fin"
        elif len(letra) > 1 or len(letra) < 1:
            print("No se pueden usar esa cantidad de letras. Intenta con una sola.")
        elif letra in letras_usadas:
            print("Esta letra ya ha sido usada, intenta con otra.")
        elif letra.isalpha() == False:
            print("No se permite ese tipo de caracter. Intenta con letras del abecedario.")
        else:
            letras_usadas.append(letra)
            break
    print("--------------------------------- \n")
    return letra
        
def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        print("Letra correcta. Sigue así.\n")
        return True
    elif letra not in palabra_secreta:
        print("Letra incorrecta.\n")
        return False
    
def validar_palabra(letras_usadas, palabra_secreta):
    for i in palabra_secreta:
        if i not in letras_usadas:
            return False
        elif i in letras_usadas:
            True
    return True
####################################################################        
if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    print("Tienes 7 intentos. Sí te equivocas, se te descontará un intento.")
    print("En caso de querer salir del juego, ingrese FIN.")
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False
    salir = False
    
    palabras = ["listas", "bucles", "variables"]
    palabra_secreta = leer_palabra_secreta(palabras)
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra 
        # y verificar sí el jugador quiere salir del juego
        letra = pedir_letra(letras_usadas)
        if letra == "fin":
            salir = True
            break
        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos y muestro
            # cuantos intentos quedan
            intentos += 1
            if intentos == 6:
                print("Tienes un ultimo intento.")
            else:
                print(f"Te quedan {7 - intentos} intentos.")
            
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida! La palabra secreta es: ¡{palabra_secreta.upper()}!\n')
    elif salir:
        print("Ha salido del juego.")
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida! La palabra secreta es: ¡{palabra_secreta.upper()}!\n')
