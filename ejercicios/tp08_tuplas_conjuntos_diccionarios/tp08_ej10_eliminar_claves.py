# TP08 - EJERCICIO 10
# Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
# y una lista de claves. La función debe eliminar del diccionario todas las claves
# contenidas en la lista, devolviendo el diccionario modificado y un número entero
# que represente la cantidad de claves eliminadas. Desarrollar también un programa
# para verificar su comportamiento.


def _eliminar_claves(diccionario: dict, lista: list) -> tuple[dict, int]:
    """
    Contrato:
        Función que borra de un diccionario las claves pertenecientes a una lista.
        Y cuenta cuántas claves se borraron.
    Precondiciones:
        Recibe como parámetros un diccionario y una lista.
    Postcondiciones:
        Retorna una tupla con el diccionario original modificado, sin las claves pertenecientes a la lista,
        y un entero correspondiente a la cantidad de claves que se han eliminado.
    """
    contador = 0
    for clave in lista:
        if clave in diccionario:
            del diccionario[clave]
            contador += 1
    return (diccionario, contador)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Llama a la función 'eliminar_claves'
        Y muestra los resultados por pantalla
    Precondiciones:
        No recibe parámetros. No pide al usuario ningún dato.
    Postcondiciones:
        Muestra por pantalla los resultados de la función 'eliminar_claves'.
    """
    diccionario = {
        "manzana": 10,
        "banana": 5,
        "naranja": 8,
        "pera": 3,
        "uva": 12,
        "kiwi": 7,
    }

    claves_a_eliminar = ["banana", "uva", "durazno", "kiwi", "sandia"]

    print(f"El diccionario es: \n{diccionario}\n")
    print(f"La lista de claves es: \n{claves_a_eliminar}\n")
    diccionario_reducido, claves_eliminadas = _eliminar_claves(
        diccionario, claves_a_eliminar
    )
    print(
        f"\nEl diccionario tras eliminar las claves pertenecientes a la lista de claves es:\n{diccionario_reducido}\n"
    )
    print(f"Se han eliminado {claves_eliminadas} claves del diccionario.\n")


if __name__ == "__main__":
    assert _eliminar_claves({"lunes": 1, "martes": 2, "miercoles": 3,}, []) == ({"lunes": 1, "martes": 2, "miercoles": 3}, 0)
    assert _eliminar_claves({}, ["juana", "lucia", "pedro"]) == ({}, 0)
    assert _eliminar_claves(
        {"manzana": 10, "banana": 5, "naranja": 8, "pera": 3}, ["banana", "banana"],
        ) == (
            {"manzana": 10, "naranja": 8, "pera": 3}, 1
            )

    main()
