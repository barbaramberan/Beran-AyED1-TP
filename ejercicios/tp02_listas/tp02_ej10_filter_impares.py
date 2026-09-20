# TP02 - Ejercicio 10
# Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los elementos de la primera que sean impares. El proceso deberá realizarse utilizando la función filter(). Imprimir las dos listas por pantalla.

from random import randint

def crear_lista() -> list[int]:
    """
    Contrato:
        Función para crear una lista con una cantidad de lementos al azar entre 10 y 30, cuyos elementos tambíen son al azar, entre 1 y 100.
    Precondiciones:
        No tiene.
    Postcondiciones:
        La función devuelve una lista de enteros positivos.
    """
    
    return [randint(1, 100) for i in range(randint(10, 20))]

def lista_impares(lista: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 != 0, lista ))
    

def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Crea una lista con crear_lista, luego crea una nueva lista con sus impares cono lista_impares.
    Precondiciones:
        Debe ejecutarse como programa principal. No recibe parámetros.
    Postcondiciones:
        No retorna nada, pero muestra en pantalla la lista principal y la nueva lista de impares.
    """
    lista = crear_lista()
    print(f"Esta es la lista original:\n{lista}\nY esta es la misma lista unicamente con los impares:\n{lista_impares(lista)}")

if __name__ == "__main__":
    main()