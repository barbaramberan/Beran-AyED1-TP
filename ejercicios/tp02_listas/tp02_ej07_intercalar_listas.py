# TP02 - Ejercicio 07
# Intercalar los elementos de una lista entre los elementos de otra. La intercalación deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden tener distintas longitudes.


def intercalar(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Recibe dos listas y las intercala modificando la primer lista, utilizando rebanadas.
    Precondiciones:
        Lista1 y lista2 deben ser listas de enteros.
    Postcondiciones:
        Retorna lista1 modificada, con los elementos de lista 2 intercalados.
    """
    x = len(lista1)
    lista1[x:] = [0] * len(lista2)
    lista1[0::2] = lista1[0:x]
    lista1[1::2] = lista2[::]
    return lista1


def main() -> None:
    """
    Ejecuta el programa principal, muestra en pantalla la lista que retorna la función intercalar.
    Precondiciones:
        No recibe parámetros. Las listas utilizadas deben ser listas de enteros.
    Postcondiciones:
        No retorna nada, pero muestra en pantalla la lista que retorna la función intercalar.
    """
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6, 8]
    print(f"Las listas que vamos a inetrcalar son:\n{lista1}\n{lista2}")
    print(f"La lista intercalada resultante es:\n{intercalar(lista1, lista2)}")


if __name__ == "__main__":
    main()
