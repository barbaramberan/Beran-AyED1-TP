# TP04 - EJERCICIO 02
# Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
# misma tiene 80 columnas


def _leer_cadena() -> str:
    """
    Contrato:
        Función para leer la cadena de caracteres.
    Precondiciones:
        No recibe parámetros. Se debe ingresar una cadena de strings.
    Postcondiciones:
        Retorna la cadena de caracteres ingresada por el usuario.
    """
    cadena = input("Ingrese la oración que desea evaluar (máximo 80 caracteres): ")
    while len(cadena) > 80:
        cadena = input("La oración no puede tener más de 80 caracteres: ")
    return cadena


def centrar_texto(cadena: str) -> None:
    """
    Contrato:
        Función que recibe una cadena como parámetro, calcula su largo y la cantidad de espacios
        que debe imprimir antes de la cadena, para que quede centrada en una consola de 80
        caracteres.
    Precondiciones:
        Cadena debe ser una cadena de strings no mayor a 80.
    Postcondiciones:
        No retorna nada, pero muestra en pantalla la oración centrada.
    """
    sobrante = 80 - len(cadena)
    espacios = sobrante // 2
    print(f"{' ' * espacios}{cadena}")


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    centrar_texto(_leer_cadena())


if __name__ == "__main__":
    main()
