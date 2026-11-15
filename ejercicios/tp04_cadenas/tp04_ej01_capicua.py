# TP04 - EJERCICIO 01
# Desarrollar una función que determine si una cadena de caracteres es capicúa


def _leer_cadena() -> str:
    """
    Contrato:
        Función para leer la cadena de caracteres.
    Precondiciones:
        No recibe parámetros. Se debe ingresar una cadena de strings.
    Postcondiciones:
        Retorna la cadena de caracteres ingresada por el usuario.
    """
    cadena = input("Ingrese la oración que desea evaluar: ")
    return cadena


# capicúa según palabras de una oración.
"""
def capicua0(cadena: str) -> bool:
    
    Contrato:
        Función que coniverte una cadena de str en una lista de str, y la compara con la misma 
        lista invertida para saber si es capicúa. (Ignora los signos de pregunta)
    Precondiciones:
        Recibe como parámetro una cadena de caracteres.
    Postcondiciones:
        Retorna True si la oración es capicúa y False si no lo es.
    
    cadena = cadena.strip("¿?").split()
    return cadena == list(reversed(cadena))
"""


def capicua(cadena: str) -> bool:
    """
    Contrato:
        Recibe una cadena como parámetro y la recorre comparando sus elementos de afuera hacia 
        adentro, el primero con el último progresivamente.
    Precondiciones:
        Cadena debe ser un string.
    Postcondiciones:
        Retorna un booleano. True si la comparación de los caracteres es verdadera (si es capicúa),
        o si la cadena tiene un solo elemento.
        False si algúna de las letras comparadas no coincide.
    """
    largo = len(cadena) // 2
    for i in range(largo):
        if cadena[i] != cadena[-1 - i]:
            return False
    return True


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """

    # if capicua0(_leer_cadena()):

    #    print("La oración ingresada es capicúa.")
    # else:
    #    print("La oración ingresada no es capicúa.")

    if capicua(_leer_cadena()):
        print("La oración ingresada es capicúa.")
    else:
        print("La oración ingresada no es capicúa.")


if __name__ == "__main__":
    # assert capicua0("hola mundo hola") == True
    # assert capicua0("probando este programa") == False
    assert capicua("") == True
    assert capicua("perro") == False
    main()
