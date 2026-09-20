# TP02 - Ejercicio 02
# En este ejercicio vamos a crear 3 funciones para trabajar con listas.

from random import randint


def crear_lista() -> list[int]:
    """
    Contrato:
        Esta función genera una lista con una cantidad ingresada por el usuario de elementos aleatorios.
    Precondiciones:
        La cantidad de elementos de la lista, ingresada por el usuario debe ser un entero positivo.
    Postcondiciones:
        Devuelve una lista de números enteros aleatorios entre 1 y 100.
    """
    num = int(
        input(
            "Ingrese la cantidad de elementos que tendrá la lista (debe ser un entero positivo): "
        )
    )

    return [randint(1, 100) for x in range(num)]


def encontrar_repetidos(lista: list[int]) -> bool:
    """
    Contrato:
        Esta función compara la cantidad de elementos que tiene una lista, con la cantidad de elementos que quedan al convertir la lista en un conjunto.
    Precondiciones:
        Recibe como parámetro una lista de enteros.
    Postcondiciones:
        Devuelve True cuando la cantidad de elementos en la lista es diferente a la cantidad de elementos en el conjunto.
    """
    return len(lista) != len(set(lista))


def devolver_unicos(lista: list[int]) -> list[int]:
    """
    Contrato:
        Filtra los elementos que aparecen una sola vez, comparando el resultado de contar cuantas veces aparece cada elemento de la lista con 1.
    Precondiciones:
        Recibe una lista de enteros.
    Postcondiciones:
        Devuelve una lista de enteros con los elementos únicos de la lista recibida como parámetro.
    """
    return list(filter(lambda elemento: lista.count(elemento) == 1, lista))


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Crea una lista, llama a funciones para determinar si tiene elementos repetidos y generar una nueva lista sin esos elementos en caso de tenerlos. Muestra todo en pantalla.
    """
    lista = crear_lista()
    print(f"\nLa lista con la que vamos a trabajar es:\n{lista}\n")
    if encontrar_repetidos(lista):
        print("\nLa lista tiene elementos repetidos.\n")
        print(
            f"Ésta es la lista sin los elementos repetidos:\n{devolver_unicos(lista)}"
        )
    else:
        print("La lista no tiene elementos repetidos.")


if __name__ == "__main__":
    assert encontrar_repetidos([1, 2, 3, 2]) == True
    assert encontrar_repetidos([1, 2, 3, 4]) == False
    assert devolver_unicos([1, 2, 2, 3, 4, 4]) == [1, 3]
    assert devolver_unicos([5, 5, 5, 5]) == []
    main()
