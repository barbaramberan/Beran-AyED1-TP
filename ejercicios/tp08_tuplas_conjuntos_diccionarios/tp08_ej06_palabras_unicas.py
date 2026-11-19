# TP08 - EJERCICIO 06
# Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
# repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
# ordenadas según su longitud. Los signos de puntuación no deben afectar el proceso


def _quitar_puntuacion(frase: str) -> str:
    """
    Contrato:
        Función que recibe una frase, y le quita los signos de puntuación, reemplazandolos con espacios.
    Precondiciones:
        Frase debe ser una cadena de strings en minúsculas.
    Postcondiciones:
        Retorna una cadena de strings sin signos de puntuacíon en ningún lado.
    """
    resultado = ""
    for caracter in frase:
        if caracter.isalpha() or caracter.isspace():
            resultado += caracter
        else:
            resultado += " "
    return resultado


def _filtrar_frase(frase: str) -> list[str]:
    """
    Contrato:
        Recibe una frase, elimina las palabras repetidas y devuelve las
        palabras restantes ordenadas según su longitud, de menor a mayor.
    Precondiciones:
        Recibe como parámetro 'frase', una cadena de caracteres que ya debe
        estar en minúscula y sin signos de puntuación, con las palabras
        separadas por espacios.
    Postcondiciones:
        Retorna una lista de cadenas con una sola aparición de cada palabra,
        ordenada por longitud. Las palabras de igual longitud quedan en orden
        arbitrario. Si la frase está vacía, retorna una lista vacía.
    """
    lista_frase = frase.split()
    conjunto = set(lista_frase)
    return sorted(conjunto, key=len)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Pide al usuario el ingreso de una frase y llama a las funciones.
    Precondiciones:
        No recibe parámetros. El usuario debe ingresar una cadena de caracteres.
    Postcondiciones:
        No retorna nada. Muestra en pantalla los resultados de las funciones.
    """
    print(
        "Este programa lee una oración y devuelve una lista con sus palabras ordenadas según longitud, de menos a mayor.\n"
    )
    frase = input("Ingrese una oración: ")
    frase_minuscula = frase.lower()
    frase_sin_puntuacion = _quitar_puntuacion(frase_minuscula)
    palabras = _filtrar_frase(frase_sin_puntuacion)
    if palabras:
        print("La lista de palabras de su oración es:")
        for palabra in palabras:
            print(palabra)
    else:
        print("No se ingresaron palabras en la oración.")


if __name__ == "__main__":
    main()
