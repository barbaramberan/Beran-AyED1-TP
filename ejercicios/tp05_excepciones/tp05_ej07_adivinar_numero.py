# TP05 - EJERCICIO 07
# Escribir un programa que juegue con el usuario a adivinar un número. El programa
# debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para
# eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número
# que tiene que adivinar es mayor o menor que el ingresado. Cuando consiga
# adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar
# el número. Si el usuario introduce algo que no sea un número se mostrará un
# mensaje en pantalla y se lo contará como un intento más.

import random
def adivinanza() -> str:
    """
    Contrato:
        Función que genera un número al azar. Luego pide al usuario que ingrese por
        teclado números para intentar adivinarlo. 
        Lleva la cuenta de cuántos intentos se ingresaron.
        Los datos inválidos cuentan como intentos.
    Precondiciones:
        Esta función no recibe parámetros. El usuario debe ingresar números enteros.
    Postcondiciones:
        Retorna un mensaje con la cantidad de intentos que al usuario le llevó 
        adivinar el número. También muestra por pantalla si el número ingresado es mayor o menor
        que el que hay que adivinar después de cada intento.
    """
    intentos = 0
    numero = random.randint(1, 500)
    print("El sistema genera un número al azar entre 1 y 500. Usted tiene que adivinar cuál es.")
    while True:
        try:
            adivinado = int(input("Ingrese que número cree que es: "))
            if adivinado == numero:
                intentos += 1
                print("¡¡FELICITACIONES, LO HAS ADIVINADO!!")
                break
            elif adivinado > 500:
                raise ValueError
            elif adivinado < numero:
                intentos += 1
                print("El número que buscas es mayor que el que ingresaste.")
            elif adivinado > numero:
                intentos += 1
                print("El número que buscas es menor que el que ingresaste.")
        except ValueError:
            intentos += 1 
            print("Debe ingresar un número entero entre 1 y 500")
    resultado = f"Adivinar el número misterioso te ha llevado {intentos} intentos."
    return resultado


print(adivinanza())
