# TP04 - EJERCICIO 03
# Los números de claves de dos cajas fuertes están intercalados dentro de un número
# entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
# para obtener ambas claves, donde la primera se construye con los dígitos ubicados
# en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
# posiciones pares. Los dígitos se numeran desde la izquierda

import random


def _generar_entero() -> int:
    """
    Contrato:
        función que genera un número aleatorio de entre 4 y 10 dígitos.

    Precondiciones:
        No recibe parámetros.

    Postcondiciones:
        Retorna un número entrero entre 1000 y 9999999999 al azar.
    """
    return random.randint(1000, 9999999999)


def calcular_claves(clave: int) -> tuple:
    """
    Contrato:
        Función que recibe un entero como parámetro y lo convierte a str. Luego, con
        rebanadas, separa los números ubicados en posiciones pares, de los números en posiciones
        impares.

    Precondiciones:
        El parámetro clave debe ser un entero positivo.

    Postcondiciones:
        Devuelve una tupla, el primer elemento es la clave con los números en posiciones impares
        y el segundo elemento es la clave formada por los números en posiciones pares.

    """
    clave_str = str(clave)
    clave1, clave2 = clave_str[::2], clave_str[1::2]
    return (clave1, clave2)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    clave_maestra = _generar_entero()
    print(f"La clave maestra es: {clave_maestra}")
    print(f"La clave de la caja fuerte N° 1 es: {calcular_claves(clave_maestra)[0]}")
    print(f"La clave de la caja fuerte N° 2 es: {calcular_claves(clave_maestra)[1]}")


if __name__ == "__main__":
    main()
