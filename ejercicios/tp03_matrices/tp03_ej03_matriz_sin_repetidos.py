# TP03 - EJERCICIO 03
# Desarrollar un programa para rellenar una matriz de N x N con números enteros al
# azar comprendidos en el intervalo [0,N²), de tal forma que ningún número se repita.
# Imprimir la matriz por pantalla.

import random


def generar_matriz(n: int) -> list[list[int]]:
    """
    Contrato:
        Genera una matriz de n x n con los números enteros de 0 a n² - 1 en orden
        aleatorio. Mezcla una lista con random.shuffle y la corta en filas con
        rebanadas.

    Precondiciones:
        n debe ser un entero mayor o igual a 1.

    Postcondiciones:
        Devuelve una lista de n listas, cada una con n enteros.
        Ningún número se repite en toda la matriz.
    """
    numeros = list(range(n * n))
    random.shuffle(numeros)

    matriz = []
    for fila in range(n):
        inicio = fila * n
        matriz.append(numeros[inicio : inicio + n])
    return matriz


def imprimir_matriz(matriz: list[list[int]]) -> None:
    """
    Contrato:
        Recibe una matriz e imprime una fila por renglón, con cada valor alineado
        a la derecha en un ancho de 6 caracteres.

    Precondiciones:
        matriz debe ser una lista de listas de enteros.

    Postcondiciones:
        No retorna nada, pero muestra la matriz por pantalla.
        No modifica la matriz.
    """
    for fila in matriz:
        renglon = ""
        for valor in fila:
            renglon += f"{valor:>6}"
        print(renglon)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar un entero (tamaño N de la matriz).

    Postcondiciones:
        Pide N hasta que sea mayor o igual a 1. Muestra por pantalla una matriz
        de N x N con los números del 0 al N² - 1 sin repetir.
    """
    while True:
        n = int(input("Ingrese el tamaño N de la matriz: "))
        if n >= 1:
            break

    matriz = generar_matriz(n)
    print(f"\nMatriz de {n} x {n} con los números del 0 al {n * n - 1} sin repetir:")
    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()