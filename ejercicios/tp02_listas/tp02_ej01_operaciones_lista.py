# TP02 - Ejercicio 01
# El ejercicio consta de cuatro funciones de listas y un programa principal para comprobar el funcionamiento de las mismas mostrando la lista en pantalla.

from random import randint
from functools import reduce


def crear_lista() -> list[int]:
    """
    Contrato:
        Función para crear una lista con una cantidad de lementos al azar entre 10 y 99, cuyos elementos tambíen son al azar, entre 1000 y 9999.
    Precondiciones:
        No tiene.
    Postcondiciones:
        La función devuelve una lista de enteros positivos.
    """
    lista = []
    for i in range(randint(10, 99)):
        lista.append(randint(1000, 9999))
    return lista


def calcular_producto(lista: list[int]) -> int:
    """
    Contrato:
        Función para calcular el producto de todos los elementos de una lista.
    Precondiciones:
        Recibe como parámetro una lista de enteros positivos.
    Postcondiciones:
        Devuelve un entero positivo, que es el producto de los elementos de una lista.
    """
    producto = reduce(lambda acumulador, elemento: acumulador * elemento, lista)
    return producto


def eliminar_valor(lista: list[int], valor: int) -> list[int]:
    """
    Contrato:
        Esta función elimina un valor de una lista.
    Precondiciones:
        Recibe comom parámetros una lista de enteros y el valor a eliminar, que debe ser un entero de cuatro dígitos.
    Postcondiciones:
        Devuelve la lista de enteros sin el valor que se eliminó.
    """
    eliminar = list(filter(lambda elemento: elemento != valor, lista))
    return eliminar


def determinar_capicua(lista: list[int]) -> bool:
    lista1 = lista[::-1]
    return lista == lista1


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Crea la lista, llama a las funciones y muestra su resultado en pantalla.
    Precondiciones:
        El archivo debe ejecutarse como programa principal. No recibe parámetros. valor debe ser un entero positivo.
    Postcondiciones:
        Se muestra en pantalla la lista creada, el producto de sus elementos, la nueva lista sin un valor y si es capicúa o no.
    """
    lista = crear_lista()
    print(f"La lista con la que vamos a trabajar es:\n{lista}\n")
    print(
        f"El producto de todos los elementos de la lista es: {calcular_producto(lista)}\n"
    )
    valor = int(input("Ingrese el número entero que desee eliminar de la lista: "))
    print(
        f"\nÉsta es la nueva lista tras eliminar el valor ingresado:\n{eliminar_valor(lista, valor)}"
    )
    if determinar_capicua(lista):
        print("\nLa lista es capicúa.")
    else:
        print("\nLa lista no es capicúa.")


if __name__ == "__main__":
    assert calcular_producto([1, 2, 3, 4]) == 24
    assert calcular_producto([5, 2]) == 10
    assert calcular_producto([7]) == 7
    assert eliminar_valor([1, 2, 3, 2, 1], 2) == [1, 3, 1]
    assert eliminar_valor([5, 5, 5], 5) == []
    assert eliminar_valor([1, 2, 3], 9) == [1, 2, 3]
    assert determinar_capicua([1, 2, 3, 2, 1]) == True
    assert determinar_capicua([1, 2, 3, 4]) == False
    assert determinar_capicua([5]) == True 
    assert determinar_capicua([]) == True 
    main()
