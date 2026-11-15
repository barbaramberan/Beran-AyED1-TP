# TP04 - EJERCICIO 12
# Escribir un programa para crear una lista por comprensión con los naipes de la
# baraja española. La lista debe contener cadenas de caracteres.


def baraja() -> list[str]:
    """
    Contrato:
        Crea la lista de los naipes de la baraja española de 48 cartas,
        utilizando una lista por comprensión.

    Precondiciones:
        No recibe parámetros.

    Postcondiciones:
        Devuelve una lista de 48 strings con el formato "número palo",
        con los números del 1 al 12 para cada uno
        de los cuatro palos: Oros, Copas, Espadas y Bastos.
    """
    palos = ("Oros", "Copas", "Espadas", "Bastos")
    return [f"{num} {element}" for element in palos for num in range(1, 13)]


print(baraja())
