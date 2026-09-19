# TP01 - Ejercicio 08
# Este ejercicio pide que se arme un programa para imprimir el calendario de un mes, utilizando una función dada (_dia_de_semana).
# Yo nuevamente reutilicé mis funciones de validar fecha.


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


def _dias_en_mes(mes: int, anio: int) -> int:
    dia = 28
    while _validar_fecha(dia, mes, anio):
        dia += 1
    dia -= 1
    return dia


def _dia_de_semana(
    dia: int, mes: int, anio: int
) -> int:  # Función sacada del enunciado del ejercicio.
    """
    Contrato: Función que recibe 3 parámetros enteros y devuelve un entero según qué día de la semana sea.
    Precondiciones: Los parámetros dia, mes y anio deben ser enteros y valores válidos para una fecha.
    Postcondiciones: La función retorna enteros del 0 al 6, para cada día de la semana empezando en Domingo.
    """
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (
        ((26 * mes - 2) // 10) + dia + anio2 + (anio2 // 4) + (siglo // 4) - (2 * siglo)
    ) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem


def imprimir_calendario(mes: int, anio: int) -> None:
    """
    contrato:
        Función que recorre todos los días de un mes, y los imprime para formar un calendario.
    Precondiciones:
        mes y anio tienen que ser enteros positivos.
    Postcondiciones:
        Se muestra en pantalla un calendario distribuido según corresponde.
    """
    letras = ("D", "L", "M", "X", "J", "V", "S")
    for letra in letras:
        print(f"{letra:>2}", end=" ")
        if letra == "S":
            print()
    columna = _dia_de_semana(1, mes, anio)
    dias_mes = _dias_en_mes(mes, anio)
    for _ in range(columna):
        print(f"{'':2}", end=" ")
    for dia_actual in range(1, dias_mes + 1):
        print(f"{dia_actual:2}", end=" ")
        columna += 1
        if columna == 7:
            columna = 0
            print()


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio. Pide el ingreso de mes y anio que deben ser enteros.

    Precondiciones:
        El archivo debe ejecutarse como programa principal. No recibe parámetros.

    Postcondiciones:
        No retorna nada, pero muestra en pantalla el calendario del mes y año ingresados, a través de la función _imprimir_calendario.
    """
    mes = int(input("¿De qué mes te gustaria imprimir el calendario?: "))
    anio = int(input("¿De qué año?: "))
    imprimir_calendario(mes, anio)


if __name__ == "__main__":
    main()
