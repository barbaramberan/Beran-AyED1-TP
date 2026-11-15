# TP03 - EJERCICIO 05
# Desarrollar un programa que permita realizar reservas en una sala de cine de N
# filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
# en un mismo programa:
# mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
# del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
# se volverá a invocar luego de la misma con los estados actualizados.
# reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
# sala en caso de estar disponible dicha butaca. La función devolverá True/False
# si logró o no reservar la butaca.
# cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
# aleatorios para simular una sala con butacas ya reservadas.
# butacas_libres: Recibirá como parámetro la matriz y retornará cuántas butacas
# desocupadas hay en la sala.
# butacas_contiguas: Buscará la secuencia más larga de butacas libres contiguas
# en una misma fila y devolverá las coordenadas de inicio de la misma.

import random

LIBRE = 0
OCUPADA = 1


def _crear_sala(filas: int, butacas: int) -> list[list[int]]:
    """
    Contrato:
        Crea una sala de filas x butacas con todas las butacas libres.

    Precondiciones:
        filas y butacas deben ser enteros mayores o iguales a 1.

    Postcondiciones:
        Devuelve una matriz nueva con todos los elementos en LIBRE.
        Cada fila es una lista distinta.
    """
    sala = []
    for _ in range(filas):
        sala.append([LIBRE] * butacas)
    return sala


def _cargar_sala(sala: list[list[int]]) -> None:
    """
    Contrato:
        Carga la sala con valores al azar para simular butacas ya reservadas.

    Precondiciones:
        sala debe ser una matriz con al menos una fila.

    Postcondiciones:
        No retorna nada, pero modifica la sala recibida.
        Cada butaca queda LIBRE u OCUPADA al azar.
    """
    for fila in range(len(sala)):
        for butaca in range(len(sala[fila])):
            sala[fila][butaca] = random.randint(LIBRE, OCUPADA)


def _mostrar_butacas(sala: list[list[int]]) -> None:
    """
    Contrato:
        Muestra por pantalla el estado de cada butaca de la sala
        (0 libre, X ocupada).

    Precondiciones:
        sala debe ser una matriz de LIBRE y OCUPADA con al menos una fila.

    Postcondiciones:
        No retorna nada, pero imprime una fila de la sala por renglón.
        No modifica la sala.
    """
    for fila in range(len(sala)):
        renglon = ""
        for butaca in range(len(sala[fila])):
            if sala[fila][butaca] == LIBRE:
                renglon += "0 "
            else:
                renglon += "X "
        print(renglon)


def _reservar(sala: list[list[int]], fila: int, butaca: int) -> bool:
    """
    Contrato:
        Reserva la butaca elegida si está disponible.

    Precondiciones:
        sala debe ser una matriz de LIBRE y OCUPADA.
        fila y butaca deben ser posiciones válidas de la sala (empiezan en 0).

    Postcondiciones:
        Si la butaca estaba libre, la marca como OCUPADA y devuelve True.
        Si ya estaba ocupada, no modifica la sala y devuelve False.
    """
    if sala[fila][butaca] == OCUPADA:
        return False
    sala[fila][butaca] = OCUPADA
    return True


def _butacas_libres(sala: list[list[int]]) -> int:
    """
    Contrato:
        Cuenta cuántas butacas desocupadas hay en la sala.

    Precondiciones:
        sala debe ser una matriz de LIBRE y OCUPADA.

    Postcondiciones:
        Devuelve un entero con la cantidad de butacas libres.
        No modifica la sala.
    """
    libres = 0
    for fila in sala:
        for estado in fila:
            if estado == LIBRE:
                libres += 1
    return libres


def _butacas_contiguas(sala: list[list[int]]) -> tuple:
    """
    Contrato:
        Busca la secuencia más larga de butacas libres contiguas en una misma
        fila. El contador vuelve a 0 cada vez que aparece una butaca ocupada.

    Precondiciones:
        sala debe ser una matriz de LIBRE y OCUPADA con al menos una butaca libre.

    Postcondiciones:
        Devuelve una tupla (fila, butaca) con las coordenadas de inicio de la
        secuencia (empiezan en 0).
        Si hay empate devuelve la primera encontrada. No modifica la sala.
    """
    mejor_largo = 0
    mejor_fila = 0
    mejor_butaca = 0

    for fila in range(len(sala)):
        largo = 0
        for butaca in range(len(sala[fila])):
            if sala[fila][butaca] == LIBRE:
                largo += 1
                if largo > mejor_largo:
                    mejor_largo = largo
                    mejor_fila = fila
                    mejor_butaca = butaca - largo + 1
            else:
                largo = 0
    return (mejor_fila, mejor_butaca)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar enteros (filas, butacas por fila y la butaca a
        reservar).

    Postcondiciones:
        Pide N y M hasta que sean mayores o iguales a 1. Permite reservar butacas
        hasta que el usuario ingrese 0 como fila o la sala se llene. Muestra la
        sala antes y después de cada reserva.
    """
    while True:
        filas = int(input("Ingrese la cantidad de filas de las butacas del cine: "))
        if filas >= 1:
            break
    while True:
        butacas = int(input("Ingrese la cantidad de butacas por fila: "))
        if butacas >= 1:
            break

    sala = _crear_sala(filas, butacas)
    _cargar_sala(sala)

    print("\nEstado de la sala (0 libre, X ocupada):")
    _mostrar_butacas(sala)

    while _butacas_libres(sala) > 0:
        print(f"\nButacas libres: {_butacas_libres(sala)}")
        inicio_fila, inicio_butaca = _butacas_contiguas(sala)
        print(
            "La secuencia más larga de butacas libres contiguas empieza en la "
            f"fila {inicio_fila + 1}, butaca {inicio_butaca + 1}."
        )

        while True:
            fila = int(input("\nFila a reservar (0 para salir): "))
            if 0 <= fila <= filas:
                break
            print("Esa fila no existe.")
        if fila == 0:
            return

        while True:
            butaca = int(input("Butaca a reservar: "))
            if 1 <= butaca <= butacas:
                break
            print("Esa butaca no existe.")

        if _reservar(sala, fila - 1, butaca - 1):
            print("Reserva realizada.")
        else:
            print("Esa butaca está ocupada, elija otra.")

        print("\nSala actualizada:")
        _mostrar_butacas(sala)

    print("\nLa sala está completa, no quedan butacas libres.")


if __name__ == "__main__":
    main()