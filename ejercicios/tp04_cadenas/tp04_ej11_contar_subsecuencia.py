# TP04 - EJERCICIO 11
# Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
# de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los
# caracteres de la subcadena no necesariamente deben estar en forma consecutiva
# dentro de la cadena, pero sí respetando el orden de los mismos.


def contar(cadena: str, subcadena: str) -> int:
    """
    Contrato:
        Cuenta cuántas veces se puede formar la subcadena dentro de la
        cadena, sin diferenciar mayúsculas de minúsculas. Los caracteres
        de la subcadena no tienen que ser consecutivos, pero sí respetar
        su orden.

    Precondiciones:
        cadena debe ser un string.
        subcadena debe ser un string no vacío.

    Postcondiciones:
        Devuelve un entero mayor o igual a 0 con la cantidad de veces que
        la subcadena aparece en la cadena.
        Cada caracter de la cadena se usa a lo sumo una vez, por lo que
        las apariciones no se superponen.
        No modifica la cadena ni la subcadena.
    """
    contador = 0
    comparar = 0
    for c in cadena.lower():
        if c == subcadena[comparar].lower():
            if comparar < len(subcadena) - 1:
                comparar += 1
            else:
                comparar = 0
                contador += 1
    return contador


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar una cadena y una subcadena.

    Postcondiciones:
        Pide cada dato hasta que no esté vacío ni formado solo por
        espacios. Muestra por pantalla cuántas veces se encuentra la
        subcadena en la cadena, o un aviso si no se encuentra.
    """
    while True:
        cadena = input("Ingrese una cadena de caracteres: ")
        if cadena.strip():
            break
    while True:
        subcadena = input(
            "Ingrese la subcadena que desea encontrar en la cadena anterior: "
        )
        if subcadena.strip():
            break
    contador = contar(cadena, subcadena)
    if contador:
        print(f"La subcadena se encuentra {contador} veces en la cadena.")
    else:
        print("La subcadena no se encuentra en la cadena.")


if __name__ == "__main__":
    assert (
        contar(
            "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva "
            "huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro.",
            "uade",
        )
        == 4
    )
    assert contar("ojalá funcione este programa profe", "feo") == 1
    assert contar("esta cadena no tendrá la subcadena", "bien") == 0
    assert contar("HOLA", "hola") == 1
    assert contar("abc", "abcd") == 0
    main()
