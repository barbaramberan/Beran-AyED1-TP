# TP01 - Ejercicio 07
# Función que devuelva el día siguiente a una fecha recibida. Cálculo de sumar días a una fecha. Y diferencia de días entre fechas
# Yo voy a reciclar mis funciones de validar fecha del ejercicio 2.


def _es_bisiesto(anio: int) -> bool:
    """Contrato: Recibe un número entero como "anio" y verifica si un año es biciesto.

    Precondiciones:
         anio debe ser un número entero.

    Postcondiciones:
         Devuelve True solo si anio es divisible por 4, pero no por 100,
         a menos que también sea divisible por 400. En cualquier otro caso devuelve False.
    """
    assert isinstance(anio, int), "anio debe ser un entero"

    if anio % 4 == 0:
        if anio % 100 != 0:
            return True
        elif anio % 400 == 0:
            return True
        return False
    return False


def _validar_fecha(dia: int, mes: int, anio: int) -> bool:
    """Contrato:
        Recibe tres números enteros y valida si los tres valores día, mes y año, representan una fecha válida.

    Precondiciones:
        dia, mes y anio deben ser números enteros.

    Postcondiciones:
        - Retorna True si la fecha es biológicamente y cronológicamente válida.
        - Retorna False si el mes está fuera del rango 1-12, si el año excede los límites (-9999 A.C a 9999 D.C),
            o si el día no se corresponde con los días máximos que posee ese mes en particular (contando bisiestos).
    """
    # Validar rangos generales de las variables
    if dia > 31 or dia < 1:
        return False
    if mes > 12 or mes < 1:
        return False
    if anio > 9999 or anio < -9999:
        return False

    # Validar meses con 30 días
    meses_30 = (4, 6, 9, 11)

    if mes in meses_30 and dia > 30:
        return False

    # Validar el caso especial de Febrero
    if mes == 2:
        if _es_bisiesto(anio):
            if dia > 29:
                return False
        elif dia > 28:
            return False
    return True


# def _calcular_dia_siguiente(dia: int, mes: int, anio: int) -> None:
#     """
#     contrato:
#         Utiliza la función de validar fecha para calcular el día siguiente al ingresado
#     Precondiciones:
#         dia, mes y anio deben ser enteros positivos.
#     Postcondiciones:
#         Muestra en pantalla tres enteros correspondientes a la fecha del día siguiente según corresponda. No retorna nada.

#     """
#     if _validar_fecha(dia + 1, mes, anio):
#         print(f"El día siguiente es: {dia + 1}/{mes}/{anio}")
#     elif _validar_fecha(1, mes + 1, anio):
#         print(f"El día siguiente es: 1/{mes + 1}/{anio}")
#     elif _validar_fecha(1, 1, anio +1):
#         print(f"El día siguiente es: 1/1/{anio + 1}")
#     else:
#         print("La fecha ingresada no puede ser calculada")


def calcular_dia_siguiente(dia: int, mes: int, anio: int) -> tuple:
    """
    contrato:
        Utiliza la función de validar fecha para calcular el día siguiente al ingresado
    Precondiciones:
        dia, mes y anio deben ser enteros positivos.
    Postcondiciones:
        Muestra en pantalla tres enteros correspondientes a la fecha del día siguiente según corresponda. No retorna nada.

    """
    if _validar_fecha(dia + 1, mes, anio):
        dia += 1
        fecha_actualizada = (anio, mes, dia)
    elif _validar_fecha(1, mes + 1, anio):
        dia = 1
        mes += 1
        fecha_actualizada = (anio, mes, dia)
    elif _validar_fecha(1, 1, anio + 1):
        dia = 1
        mes = 1
        anio += 1
        fecha_actualizada = (anio, mes, dia)
    else:
        print("La fecha ingresada no puede ser calculada")
        return None

    return fecha_actualizada


def opciones() -> None:
    """
    Contrato:
        Función para mostrar un menú de opciones, iterando y printeando una lista.
    Precondiciones: no tiene
    Postcondiciones: Muestra en pantalla los índices de una lista con prints.
    """
    opciones = [
        "\na: Calcular el día siguiente.",
        "b: Sumar días a esa fecha.",
        "c: Calcular cuántos días hay entre esa fecha y otra.",
        "d: SALIR\n",
    ]
    for i in range(4):
        print(opciones[i])


def calcular_fechas(fecha1: tuple, fecha2: tuple) -> int:
    """
    Contrato:
        funcion para calcular cuántos días hay entre dos fechas usando la función _calcular_dia_siguiente.
    Precondiciones:
        fecha1 y fecha2 deben ser tuplas
    Postcondiciones:
        La función devuelve un entero.
    """
    if fecha1 == fecha2:
        return 0
    elif fecha1 < fecha2:
        fecha_menor = fecha1
        fecha_mayor = fecha2
    else:
        fecha_menor = fecha2
        fecha_mayor = fecha1
    contador = 0
    while fecha_menor != fecha_mayor:
        anio1, mes1, dia1 = fecha_menor
        fecha_menor = calcular_dia_siguiente(dia1, mes1, anio1)
        if fecha_menor is None:
            break
        contador += 1
    return contador


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio. Pide el ingreso de tres enteros para dia, mes y anio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal. Las variables dia, mes y anio deben ser enteros.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """

    dia = int(input("\nIngrese un día: "))
    mes = int(input("Ingrese un número de mes: "))
    anio = int(input("Ingrese un año: "))
    opciones()
    op = input(f"\n¿Qué opción desea realizar?: ")
    if op == "a":
        nueva_fecha = calcular_dia_siguiente(dia, mes, anio)
        if nueva_fecha is not None:
            anio, mes, dia = nueva_fecha
            print(f"\nEl día siguiente es: {dia}/{mes}/{anio}\n")
    elif op == "b":
        aux = int(input("\n¿Cuántos días queres sumar?: "))
        for i in range(aux):
            nueva_fecha = calcular_dia_siguiente(dia, mes, anio)
            if nueva_fecha is not None:
                anio, mes, dia = nueva_fecha
            else:
                break
        print(f"\nLa fecha resultante de sumar esos días es: {dia}/{mes}/{anio}\n")
    elif op == "c":
        print("¿Cuál es la otra fecha?")
        dia2 = int(input("\nIngrese un día: "))
        mes2 = int(input("Ingrese un número de mes: "))
        anio2 = int(input("Ingrese un año: "))
        fecha1 = (anio, mes, dia)
        fecha2 = (anio2, mes2, dia2)
        cantidad_dias = calcular_fechas(fecha1, fecha2)
        print(
            f"\nLa cantidad de días que hay entre esas dos fechas es: {cantidad_dias}."
        )

    elif op == "d":
        print("\nSALIENDO..\n")
    else:
        print("\nLa opción ingresada es inválida.\n")


if __name__ == "__main__":
    main()
