# TP02 - Ejercicio 04
# Eliminar de una lista de números enteros aquellos valores que se encuentren en una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista resultante. La función debe modificar la lista original sin crear una copia modificada.

from random import randint

def crear_lista() -> list[int]:
    """
    Contrato:
        Función para crear una lista con una cantidad de lementos al azar entre 10 y 20, cuyos elementos tambíen son al azar, entre 1 y 50.
    Precondiciones:
        No tiene.
    Postcondiciones:
        La función devuelve una lista de enteros positivos.
    """
    
    return [randint(1, 50) for i in range(randint(10, 20))]



def eliminar_valores(lista1: list[int], lista2: list[int]) -> None:
    """
    Contrato:
        Compara los elementos de dos listas, guarda la posición de los elementos repetidos en ambas, y luego elimina esos elementos repetidos, desde el final hacia el principio de la primer lista.
    Precondiciones:
        Recibe como parámetros dos listas de enteros.
    Postcondiciones:
        Muestra en pantalla las dos listas con las que trabajaremos, la lista de elementos a eliminar y como queda la lista luego de eliminarlos.
    """
    print(f"Vamos a trabajar con la siguiente lista:\n{lista1}\n")
    print(f"Verificaremos, y eliminaremos los elementos de nuestra lista, que se encuentren también en la siguiente lista:\n{lista2}\n")
    indices_eliminar = [indice for indice, elemento in enumerate(lista1) if elemento in lista2]
    indices_eliminar.sort(reverse=True)
    eliminados = [lista1.pop(i) for i in indices_eliminar]
    print(f"Esta es la lista de valores que vamos a eliminar:\n{eliminados}\n")
    print(f"Así quedó la lista despúes de eliminar los valores:\n{lista1}\n")

def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Crea dos listas aleatorias con la función crear_lista y llama a la función eliminar_valores.
    Precondiciones:
        El archivo debe ejecutarse como programa principal. No recibe parámetros.
    Postcondiciones:
        No retorna nada, pero muestra en pantalla las listas con las q trabajamos en la función eliminar_valores.
    """
    lista1 = crear_lista()
    lista2 = crear_lista()
    eliminar_valores(lista1, lista2)

if __name__ == "__main__":
    main()
        