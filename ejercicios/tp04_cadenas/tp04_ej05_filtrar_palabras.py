# TP04 - EJERCICIO 05
# Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo
# una frase y un entero N, y devuelva otra cadena con las palabras que tengan
# N o más caracteres de la cadena original.


# a) utilizando sólo ciclos normales.
def filtrar_palabras_a(cadena: str, num: int) -> str:
    """
    Contrato:
        Filtra las palabras de una frase que tengan al menos num caracteres,
        recorriendo las palabras con un ciclo normal.

    Precondiciones:
        cadena debe ser un string con una frase.
        num debe ser un entero.

    Postcondiciones:
        Devuelve un string con las palabras de la frase original que tienen
        num o más caracteres, separadas por un espacio y sin comas pegadas.
        Se ignoran los signos de pregunta y los espacios de los extremos de
        la frase. Si ninguna palabra cumple, devuelve una cadena vacía.
    """
    palabras = ""
    cadena = cadena.strip("¿ ?").split()
    for element in cadena:
        element = element.strip(" ,")
        if len(element) >= num:
            palabras += element
            palabras += " "
    return palabras.strip()


# b) Utilizando listas por comprensión.
def filtrar_palabras_b(cadena: str, num: int) -> str:
    """
    Contrato:
        Filtra las palabras de una frase que tengan al menos num caracteres,
        utilizando una lista por comprensión.

    Precondiciones:
        cadena debe ser un string con una frase.
        num debe ser un entero.

    Postcondiciones:
        Devuelve un string con las palabras de la frase original que tienen
        num o más caracteres, separadas por un espacio y sin comas pegadas.
        Se ignoran los signos de pregunta y los espacios de los extremos de
        la frase. Si ninguna palabra cumple, devuelve una cadena vacía.
    """
    palabras = [
        element.strip(" ,")
        for element in cadena.strip("¿ ?").split()
        if len(element.strip(" ,")) >= num
    ]
    return " ".join(palabras)


# c) Utilizando la función filter.
def filtrar_palabras_c(cadena: str, num: int) -> str:
    """
    Contrato:
        Filtra las palabras de una frase que tengan al menos num caracteres,
        utilizando la función filter.

    Precondiciones:
        cadena debe ser un string con una frase, sin comas.
        num debe ser un entero.

    Postcondiciones:
        Devuelve un string con las palabras de la frase original que tienen
        num o más caracteres, separadas por un espacio.
        Se ignoran los signos de pregunta y los espacios de los extremos de
        la frase. Si ninguna palabra cumple, devuelve una cadena vacía.
    """
    palabras = list(
        filter(
            lambda elemento: len(elemento) >= num,
            cadena.strip("¿ ?").split(),
        )
    )
    return " ".join(palabras)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    cadena = input("Ingrese una frase: ")
    num = int(input("Ingrese un número entero: "))
    print(filtrar_palabras_a(cadena, num))
    print(filtrar_palabras_b(cadena, num))
    print(filtrar_palabras_c(cadena, num))


if __name__ == "__main__":
    assert (
        filtrar_palabras_a("había una vez, un ave grande", 3)
    ) == "había una vez ave grande"

    assert (
        filtrar_palabras_b("había una vez, un ave grande", 3)
    ) == "había una vez ave grande"

    assert (
        filtrar_palabras_c("había una vez un ave grande", 3)
    ) == "había una vez ave grande"
    main()
