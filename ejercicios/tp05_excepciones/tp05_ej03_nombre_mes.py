# TP03 - EJERCICIO 03
# Desarrollar una función que devuelva una cadena de caracteres con el nombre del
# mes cuyo número se recibe como parámetro. Los nombres de los meses deberán
# obtenerse de una lista de cadenas de caracteres inicializada dentro de la función.
# Devolver una cadena vacía si el número de mes es inválido. La detección de meses
# inválidos deberá realizarse a través de excepciones


def meses_escritos(num: int) -> str:
    """
    contrato:
        Función que recibe un número como parámetro y retorna una cadena con el mes equivalente a ese número.
    Precondiciones:
        num debe ser un entero.
    Postconodiciones:
        Retorna una cadena de caracteres con el mes correspondiente a num, o una cadena vacía si el
        número de mes es inválido.
    """
    meses = [
        "ENERO",
        "FEBRERO",
        "MARZO",
        "ABRIL",
        "MAYO",
        "JUNIO",
        "JULIO",
        "AGOSTO",
        "SEPTIEMBRE",
        "OCTUBRE",
        "NOVIEMBRE",
        "DICIEMBRE",
    ]

    try:
        return meses[num - 1]
    except IndexError:
        return ""


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    while True:
        try:
            num = int(input("Ingrese qué número de mes desea convertir: "))
            print(f"El mes ingresado es: {meses_escritos(num)}")
        except ValueError:
            print("Dato inválido. Debe ingresar un número.")
        else:
            break


if __name__ == "__main__":
    assert meses_escritos(1) == "ENERO"
    assert meses_escritos(14) == ""
    main()
