# TP03 - Ejercicio 01
#

from tabulate import tabulate

# A:
def crear_matriz() -> list[list]:
    """
    Contrato:
        Función para crear una matriz con las proporciones ingresadas por el usuario.
    Precondiciones:
        No recibe parámetros. n debe ser un entero positivo.
    Postcondiciones:
        Retorna una matriz (una lista de listas).
    """
    n = int(input("Ingrese cuántas filas y columnas desea que tenga la matriz: "))
    matriz = [[0] * n for i in range(n)]
    for f in range (len(matriz)):
        for c in range(len(matriz[f])):
            num = int(input("Ingrese un número para agregar a la matriz: "))
            matriz[f][c] = num
    return matriz

# B:
def ordenar_matriz(matriz: list[list]) -> list[list]:
    """
    Contrato:
        Función que recorre una lista de listas, ordenando cada sublista de forma ascendente.
    Precondiciones:
        matriz debe ser una lista de listas con elementos enteros.
    Postcondiciones:
        Retorna la lista de listas ordenadas.
    """
    for f in range (len(matriz)):
        matriz[f].sort()
    return matriz

# C:
def intercambiar_filas(a: int, b: int, matriz: list[list]) -> list[list]:
    """
    Contrato:
        Función que recibe dos enteros y una lista de listas, intercambia dos sublistas según los parámetros enteros recibidos.
    Precondiciones:
        c, d deben ser enteros positivos. matriz debe ser una lista de lista de enteros.
    Postcondiciones:
        Retorna la lista de listas con las modificaciones.
    """
    matriz[a - 1], matriz[b - 1] = matriz[b - 1], matriz[a - 1]
    return matriz

# D
def intercambiar_columnas(c:int, d: int, matriz: list[list]) -> list[list]:
    """
    Contrato:
        Función que recibe dos enteros y una lista de listas, recorre la lista de listas e intercambia dos elementos (los parámetros enteros recibidos) de la sublista en cada iteración.
    Precondiciones:
        c, d deben ser enteros positivos. matriz debe ser una lista de lista de enteros.
    Postcondiciones:
        Retorna la lista de listas con las modificaciones.
    """
    
    for i in range(len(matriz)):
        matriz[i][c - 1], matriz[i][d - 1] = matriz[i][d - 1], matriz[i][c - 1]
    return matriz

# E
def trasponer_matriz(matriz: list[list]) -> list[list]:
    """
    Contrato:
        Función que recibe como parámetro una matriz(lista de listas) e intercambia sobre si misma todos sus elementos.
    Precontrato:
        matriz debe ser una lista de listas de elmentos enteros.
    Postcondiciones:
        Retorna la matriz original, modificada.
    """
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

# F
def promedio_fila(f: int, matriz: list[list]) -> float:
    """
    Contrato:
        Función que recibe un número de fila y una matriz, y calcula el promedio de los elementos de esa fila.
    Precondiciones:
        f debe ser un entero positivo. matriz debe ser una lista de listas de enteros.
    Postcondiciones:
        Retorna un número real con el promedio de los elementos de la fila indicada.
    """
    fila = matriz[f - 1]
    return sum(fila) / len(fila)

# G
def porcentaje_impares_columna(c: int, matriz: list[list]) -> float:
    """
    Contrato:
        Función que recibe un número de columna y una matriz, y calcula el porcentaje de elementos impares en esa columna.
    Precondiciones:
        c debe ser un entero positivo. matriz debe ser una lista de listas de enteros.
    Postcondiciones:
        Retorna un número real con el porcentaje de elementos impares de la columna indicada.
    """
    cantidad_impares = 0
    for f in range(len(matriz)):
        if matriz[f][c - 1] % 2 != 0:
            cantidad_impares += 1
    return (cantidad_impares / len(matriz)) * 100

# H
def es_simetrica_principal(matriz: list[list]) -> bool:
    """
    Contrato:
        Función que recibe una matriz y determina si es simétrica respecto a su diagonal principal.
    Precondiciones:
        matriz debe ser una lista de listas de enteros, cuadrada (N x N).
    Postcondiciones:
        Retorna True si matriz[i][j] es igual a matriz[j][i] para todo par de índices, False en caso contrario.
    """
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


# I
def es_simetrica_secundaria(matriz: list[list]) -> bool:
    """
    Contrato:
        Función que recibe una matriz y determina si es simétrica respecto a su diagonal secundaria.
    Precondiciones:
        matriz debe ser una lista de listas de enteros, cuadrada (N x N).
    Postcondiciones:
        Retorna True si matriz[i][j] es igual a matriz[n-1-j][n-1-i] para todo par de índices, False en caso contrario.
    """
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - 1 - j][n - 1 - i]:
                return False
    return True



# J
def columnas_palindromas(matriz: list[list]) -> list[int]:
    """
    Contrato:
        Función que recibe una matriz y determina cuáles de sus columnas son palíndromas.
    Precondiciones:
        matriz debe ser una lista de listas de enteros, cuadrada (N x N).
    Postcondiciones:
        Retorna una lista con los números de columna (empezando en 1) cuyos elementos forman un palíndromo.
    """
    n = len(matriz)
    columnas = []
    for c in range(n):
        columna = []
        for f in range(n):
            columna.append(matriz[f][c])
        if columna == columna[::-1]:
            columnas.append(c + 1)
    return columnas


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Llama a las funciones, pide alusuario el ingreso de datos, e imprime en pantalla las matrices retornadas.
    Precondiciones:
        No recibe parámetros, todos los datos ingresados por el usuario deben ser enteros positivos.
    Postcondiciones:
        No retorna ningún dato pero si muestra en pantalla las matrices en repetidas ocaciones.
    """
    matriz = crear_matriz()
    print(tabulate(matriz))
    ordenar_matriz(matriz)
    print(tabulate(matriz))
    print("\nVamos a intercambiar dos filas de la matriz.")
    a = int(input("\nIngrese la primer fila: "))
    b = int(input("\nIngrese la segunda fila: "))
    intercambiar_filas(a, b, matriz)
    print(tabulate(matriz))
    print("\nAhora vamos a intercambiar dos columnas de la matriz.")
    c = int(input("\nIngrese la primer columna: "))
    d = int(input("\nIngrese la segunda columna: "))
    intercambiar_columnas(c, d, matriz)
    print(tabulate(matriz))
    print("La matriz luego de trasponerla, quedaría de la siguiente forma:\n")
    print(tabulate(trasponer_matriz(matriz)))
    f = int(input("Para calcular el promedio de los elementos de una fila ingrese un número de fila: "))
    print(f"El promedio de los elementos de esa fila es:{promedio_fila(f, matriz)}")
    c = int(input("Para calcular el porcentaje de numeros impares en una columna ingrese un número de columna: "))
    print(f"El porcentaje de numeros impares en esa columna es:{porcentaje_impares_columna(c, matriz)}")
    print(f"La matriz es simétrica con respecto a su diagonal principal?\n {es_simetrica_principal(matriz)}")
    print(f"La matriz es simétrica con respecto a su diagonal secundaria?\n {es_simetrica_secundaria(matriz)}")
    print("\nEstas son las columnas palíndromas de la matriz:")
    resultado = columnas_palindromas(matriz)
    if resultado:
        print(resultado)
    else:
        print("Ninguna columna es palíndroma.")

if __name__ == "__main__":
    main()