# TP08 - EJERCICIO 02
# Escribir una función que reciba como parámetro una tupla conteniendo una fecha
# (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
# en formato extendido. La función debe contemplarse que el año se ingrese en dos
# dígitos, los que serán interpretados según un año de corte definido dentro del
# programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
# ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
# para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
# 1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
# cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
# mostrar el resultado.

from tp08_ej01_fechas_horarios import _validar_fecha


def _ingresar_fecha() -> tuple[int]:
    """
    Contrato:
        Pide al usuario que ingrese un dia, un mes y un año y verifica que sean datos
        individualmente válidos.
    Precondiciones:
        No recibe parámetros. El usuario debe ingresar enteros para los tres datos que se le solicitan.
        Se consideran años válidos entre 1000 y 3000 ambos inclusive.
    Postcondiciones:
        Retorna una tupla con día, mes y año dentro de sus rangos.
    """
    while True:
        try:
            dia = int(input("Ingrese un día: "))
            mes = int(input("Ingrese un mes: "))
            if 0 < dia < 32 and 0 < mes < 13:
                break
            else:
                print("Debe ingresar una fecha válida.")
        except ValueError:
            print("Debe ingresar una fecha válida.")
    while True:
        try:
            anio = int(input("Ingrese un año: "))
            if 999 < anio < 3001:
                break
            elif 00 <= anio <= 30:
                anio += 2000
                break
            elif 31 <= anio <= 99:
                anio += 1900
                break
            else:
                print("Debe ingresar una fecha válida.")

        except ValueError:
            print("Debe ingresar una fecha válida.")
    return (dia, mes, anio)


def _extender_fecha(fecha: tuple[int]) -> str:
    """
    Contrato:
        Función que recibe una fecha en formato numérico y lo convierte a formato extendido.(mes en letras).
    Precondiciones:
        fecha debe ser una tupla de enteros correspondiente  a una fecha válida.
        Si anio es menor de
    """
    dia, mes, anio = fecha
    fecha_escrita = [str(dia)]
    meses = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre",
    }
    if len(str(anio)) < 4:
        if anio > 30:
            anio += 1900
        else:
            anio += 2000
    for num, letras in meses.items():
        if mes == num:
            fecha_escrita.append(letras)
    fecha_escrita.append(str(anio))
    return " de ".join(fecha_escrita)


def main() -> None:
    """
    Contrato:
        Ejecuta el principal principal del ejercicio.
        Llama a las funciones del programa.
    Precondiciones:
        No recibe parámetros.
    Postcondiciones:
        Muestra en pantalla los resultados de la función.
    """
    print("Este programa convierte fechas de formato numérico a formato extendido.")
    while True:
        fecha = _ingresar_fecha()
        if _validar_fecha(fecha):
            print(f"La fecha en formato extendido es: {_extender_fecha(fecha)}.")
            break
        else:
            print("La fecha ingresada no corresponde a una fecha válida.\n")


if __name__ == "__main__":
    main()
