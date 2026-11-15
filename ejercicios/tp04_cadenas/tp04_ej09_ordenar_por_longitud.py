# TP04 - EJERCICIO 09
# Escribir una función que reciba como parámetro una cadena de caracteres en la que
# las palabras se encuentran separadas por uno o más espacios. Devolver otra
# cadena con las palabras ordenadas según su longitud, dejando un espacio entre
# cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
# longitud de las palabras, pero deberán conservarse en la cadena final.


def ordenar_cadena(cadena: str) -> str:
    """
    Contrato:
        Ordena de menor a mayor las palabras de una cadena según su
        longitud, sin contar las comas al medirla.

    Precondiciones:
        cadena debe ser un string no vacío, con palabras separadas por uno o más
        espacios.

    Postcondiciones:
        Devuelve un string con las palabras ordenadas por longitud,
        separadas por un solo espacio y convertidas a minúsculas.
        Las comas se conservan pegadas a su palabra, aunque no cuentan
        para medir la longitud.
        Se ignoran los signos de pregunta y los espacios de los extremos
        de la cadena.
        Las palabras con la misma longitud conservan su orden relativo.
        Si la cadena está vacía, devuelve una cadena vacía.
    """
    cadena = cadena.strip("¿ ?").lower().split()
    ordenada = sorted(cadena, key=lambda elemento: len(elemento.strip(" ,")))
    return " ".join(ordenada)


assert (
    ordenar_cadena(
        "El filtro de aire debe limpiarse cada vez que volves de andar en bimbim"
    )
    == "el de de en vez que aire debe cada andar filtro volves bimbim limpiarse"
)
assert (
    ordenar_cadena("El pistón debe cambiarse a las 40 horas de uso")
    == "a el 40 de las uso debe horas pistón cambiarse"
)

cadena = input("Ingrese una cadena para ordenarla según la longitud de sus palabras: ")
print(ordenar_cadena(cadena))
