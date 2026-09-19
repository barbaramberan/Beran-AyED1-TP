# TP01 - Ejercicio 09
# programa para ingresar la cantidad de naranjas
# cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
# jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
# reparto. Simular el peso de cada unidad generando un número entero al azar entre
# 150 y 350.
# En un cajón caben 100 naranjas con un peso de entre 200 y 300 gramos cada una.
# Si el peso de alguna naranja se encuentra fuera del rango indicado se la clasifica para procesar como jugo.
# Yo voy a tomar los valores límite de paso inclusive.

from random import randint
import math


def clasificar_naranjas(n: int) -> tuple:
    """
    Contrato:
        La función itera n veces asignando peso al azar a cada naranja, luego la valida según el rango (200, 300) y la clasifica segun esté o no dentro del mismo, si es válida o si es para jugo.
    Precondiciones:
        El parámetro n debe ser un entero positivo.
    Postcondiciones:
        La función retorna una tupla de enteros formada por los dos contadores de la clasificación.
    """
    jugo = 0
    validas = 0
    for i in range(n):
        peso_naranja = randint(150, 350)
        if peso_naranja < 200 or peso_naranja > 300:
            jugo += 1
        else:
            validas += 1
    clasificacion = (validas, jugo)
    return clasificacion


def calcular_cajones(validas: int) -> tuple:
    """
    Contrato:
        Recibe una cantidad de naranjas válidas y calcula cuántos cajones de 100 naranjas se pueden armar y cuántas naranjas sobran.
    Precondiciones:
        validas debe ser un entero positivo.
    Postcondiciones:
        Retorna una tupla de dos enteros, que representan la cantidad de cajones llenos y el sobrante de naranjas validas.
    """
    cajones = validas // 100
    sobrante_naranjas = validas % 100
    return (cajones, sobrante_naranjas)


def calcular_camiones(cajones: int) -> tuple:
    """
    Contrato:
        Función que recibe como parámetro la cantidad de cajones de naranjas y calcula cuántos camiones se necesitan para transportar todos los cajones.
    Precondiciones:
        El parámetro cajones debe ser un entero positivo.
    Postcondiciones:
        Retorna una tupla
    """
    cajones_por_camion = 500 // 30
    camiones_completos = cajones // cajones_por_camion
    cajones_sobrantes = cajones % cajones_por_camion
    minimo_80 = math.ceil(cajones_por_camion * 0.80)
    if cajones_sobrantes >= minimo_80:
        hay_camion_parcial = True
        cajones_sobrantes = 0
    else:
        hay_camion_parcial = False
    return (camiones_completos, hay_camion_parcial, cajones_sobrantes)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Pide el ingrso manual de las naranjas, llama a las funciones necesarias y muestra en pantalla los resultados.
    Precondiciones:
        El archivo debe ejecutarse como programa principal. No recibe parámetros.
    Postcondiciones:
        Se muestran en pantalla las cantidades de naranjas, cajones y camiones según corresponda.

    """
    naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    validas, jugo = clasificar_naranjas(naranjas)
    cajones, sobrante_naranjas = calcular_cajones(validas)
    camiones_completos, hay_camion_parcial, cajones_sobrantes = calcular_camiones(
        cajones
    )
    print(
        f"\nSegún su cosecha, usted tiene {jugo} naranja/s para la producción de jugo.\n"
    )
    print(
        f"El resto de las naranjas caben en {cajones} cajon/es, y queda un sobrante de {sobrante_naranjas} naranja/s para el próximo reparto.\n"
    )
    if camiones_completos == 0:
        print(
            f"La cantidad de cajones de esta cosecha no alcanza para completar 1 camión de traslado. Quedarán los {cajones_sobrantes} cajones pendientes para el próximo reparto."
        )
    elif hay_camion_parcial:
        print(
            f"Para transportar todos los cajones se necesitan {camiones_completos} camion/es completo/s, y 1 camión que no llegará al 100% de su capacidad.\nNo quedan cajones sobrantes para el próximo reparto."
        )
    else:
        print(
            f"Para transportar los cajones de esta cosecha, se necesitan {camiones_completos} camion/es. Y van a quedar {cajones_sobrantes} cajon/es pendiente/s para el próximo reparto."
        )


if __name__ == "__main__":
    main()
