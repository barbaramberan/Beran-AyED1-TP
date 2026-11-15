# TP03 - EJERCICIO 04
# Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
# en cada una de sus plantas durante una semana. De este modo, cada columna
# representa el día de la semana y cada fila a una de sus fábricas.
# Se solicita:
# a. Crear una matriz con datos generados al azar para N fábricas durante una
# semana, considerando que la capacidad máxima de fabricación es de 150
# unidades por día y puede suceder que en ciertos días no se fabrique ninguna.
# b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
# c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
# d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
# e. Crear una lista por comprensión que contenga la menor cantidad fabricada
# por cada fábrica

import random

DIAS = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")
MAXIMO_DIARIO = 150


def _cargar_produccion(cantidad_fabricas: int) -> list[list[int]]:
    """
    Contrato:
        Genera al azar la producción de una semana para cada fábrica (punto a).

    Precondiciones:
        cantidad_fabricas debe ser un entero mayor o igual a 1.

    Postcondiciones:
        Devuelve una matriz con una fila por fábrica y una columna por día de DIAS.
        Los valores son enteros entre 0 y MAXIMO_DIARIO. No solicita datos.
    """
    matriz = []
    for _ in range(cantidad_fabricas):
        fila = []
        for _ in range(len(DIAS)):
            fila.append(random.randint(0, MAXIMO_DIARIO))
        matriz.append(fila)
    return matriz


def _mostrar_produccion(matriz: list[list[int]]) -> None:
    """
    Contrato:
        Muestra por pantalla la producción de cada fábrica día por día, con los
        nombres de los días como encabezado.

    Precondiciones:
        matriz debe tener una fila por fábrica y una columna por cada día de DIAS.

    Postcondiciones:
        No retorna nada, pero imprime la tabla de producción.
        No modifica la matriz.
    """
    encabezado = f"{'Fábrica':<10}"
    for dia in DIAS:
        encabezado += f"{dia:>11}"
    print(encabezado)

    for i in range(len(matriz)):
        renglon = f"{i + 1:<10}"
        for valor in matriz[i]:
            renglon += f"{valor:>11}"
        print(renglon)


def _totales_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Contrato:
        Calcula el total de bicicletas fabricadas por cada fábrica en la semana
        (punto b).

    Precondiciones:
        matriz debe tener una fila por fábrica y una columna por día.

    Postcondiciones:
        Devuelve una lista con un total por fábrica, en el mismo orden que las filas.
        No modifica la matriz.
    """
    totales = []
    for fila in matriz:
        total = 0
        for valor in fila:
            total += valor
        totales.append(total)
    return totales


def _mayor_produccion_en_un_dia(matriz: list[list[int]]) -> tuple:
    """
    Contrato:
        Busca la mayor cantidad producida por una fábrica en un solo día (punto c).

    Precondiciones:
        matriz debe tener al menos una fila y una columna por cada día de DIAS.

    Postcondiciones:
        Devuelve una tupla (fabrica, dia, cantidad) con los índices de la fábrica y
        del día (empiezan en 0) y la cantidad producida.
        Si hay empate devuelve el primero encontrado. No modifica la matriz.
    """
    mayor = matriz[0][0]
    fabrica_mayor = 0
    dia_mayor = 0
    for fabrica in range(len(matriz)):
        for dia in range(len(matriz[fabrica])):
            if matriz[fabrica][dia] > mayor:
                mayor = matriz[fabrica][dia]
                fabrica_mayor = fabrica
                dia_mayor = dia
    return (fabrica_mayor, dia_mayor, mayor)


def _totales_por_dia(matriz: list[list[int]]) -> list[int]:
    """
    Contrato:
        Calcula el total de bicicletas fabricadas cada día, sumando todas las
        fábricas.

    Precondiciones:
        matriz debe tener al menos una fila y una columna por cada día de DIAS.

    Postcondiciones:
        Devuelve una lista con un total por día, en el mismo orden que las columnas.
        No modifica la matriz.
    """
    totales = []
    for dia in range(len(DIAS)):
        total = 0
        for fila in matriz:
            total += fila[dia]
        totales.append(total)
    return totales


def _dia_mas_productivo(totales: list[int]) -> int:
    """
    Contrato:
        Determina cuál es el día más productivo considerando todas las fábricas
        (punto d).

    Precondiciones:
        totales debe ser una lista no vacía con el total producido en cada día.

    Postcondiciones:
        Devuelve el índice del día con mayor total (empieza en 0).
        Si hay empate devuelve el primero. No modifica la lista.
    """
    mejor_dia = 0
    for dia in range(len(totales)):
        if totales[dia] > totales[mejor_dia]:
            mejor_dia = dia
    return mejor_dia


def _minimos_por_fabrica(matriz: list[list[int]]) -> list[int]:
    """
    Contrato:
        Arma por comprensión una lista con la menor cantidad fabricada en un día
        por cada fábrica (punto e).

    Precondiciones:
        matriz debe tener una fila por fábrica y ninguna fila vacía.

    Postcondiciones:
        Devuelve una lista con un mínimo por fábrica, en el mismo orden que las filas.
        No modifica la matriz.
    """
    return [min(fila) for fila in matriz]


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar un entero (cantidad de fábricas).

    Postcondiciones:
        Pide la cantidad hasta que sea mayor o igual a 1. Muestra por pantalla la
        producción de la semana y los resultados de los puntos b, c, d y e.
    """
    while True:
        cantidad_fabricas = int(input("Ingrese la cantidad de fábricas: "))
        if cantidad_fabricas >= 1:
            break

    matriz = _cargar_produccion(cantidad_fabricas)
    print("\nProducción de la semana (punto a):")
    _mostrar_produccion(matriz)

    print("\nTotal por fábrica (punto b):")
    totales_fabrica = _totales_por_fabrica(matriz)
    for fabrica in range(len(totales_fabrica)):
        print(f"La fábrica {fabrica + 1} fabricó {totales_fabrica[fabrica]} bicicletas.")

    print("\nMayor producción de una fábrica en un solo día (punto c):")
    fabrica, dia, cantidad = _mayor_produccion_en_un_dia(matriz)
    print(f"La fábrica {fabrica + 1} fabricó {cantidad} bicicletas el día {DIAS[dia]}.")

    print("\nDía más productivo entre todas las fábricas (punto d):")
    totales_dia = _totales_por_dia(matriz)
    mejor_dia = _dia_mas_productivo(totales_dia)
    print(f"El día más productivo fue el {DIAS[mejor_dia]}, con {totales_dia[mejor_dia]} bicicletas.")

    print("\nMenor cantidad fabricada por cada fábrica (punto e):")
    minimos = _minimos_por_fabrica(matriz)
    for fabrica in range(len(minimos)):
        print(f"La fábrica {fabrica + 1} fabricó como mínimo {minimos[fabrica]} bicicletas en un día.")


if __name__ == "__main__":
    main()