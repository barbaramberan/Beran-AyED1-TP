# TP08 - EJERCICIO 04
# Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
# son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
# o False. Escribir también un programa para verificar su comportamiento. Considerar
# el uso de conjuntos para resolver este ejercicio.


def domino(ficha1: tuple[int], ficha2: tuple[int]) -> bool:
    """
    Contrato:
        Función que recibe dos fichas de dominó y devuelve si encajan o no.
    Precondiciones:
        ficha1 y ficha2 deben ser tuplas.
    Postcondiciones:
        Retorna True si las fichas encajan y False si no.
    """
    set_ficha1 = set(ficha1)
    set_ficha2 = set(ficha2)
    return bool(set_ficha1.intersection(ficha2))


assert domino((3, 4), (5, 4)) == True
assert domino((3, 4), (5, 6)) == False
assert domino((4, 4), (4, 2)) == True
assert domino((0, 0), (1, 2)) == False
assert domino((3, 4), (4, 3)) == True

print(f"Probando el programa.\n¿Las fichas (3, 4) y (5, 4) encajan?\n")
print(domino((3, 4), (5, 4)))
