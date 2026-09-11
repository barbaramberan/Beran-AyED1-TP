# TP01 - Ejercicio 02
# Función que recibe tres números enteros positivos correspondientes al día, mes, año de una fecha y verifica si corresponden a una fecha válida.

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
    """ Contrato: 
            Recibe tres números enteros y valida si los tres valores día, mes y año, representan una fecha válida. 

        Precondiciones: 
            dia, mes y anio deben ser números enteros.

        Postcondiciones: 
            - Retorna True si la fecha es biológicamente y cronológicamente válida.
            - Retorna False si el mes está fuera del rango 1-12, si el año excede los límites (-9999 A.C a 9999 D.C),
                o si el día no se corresponde con los días máximos que posee ese mes en particular (contando bisiestos).
    """
    # Validar rangos generales de las variables independientes
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

        
def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    dia = int(input("Ingrese un día: "))
    mes = int(input("Ingrese un número de mes: "))
    anio = int(input("Ingrese un año: "))

    if _validar_fecha(dia, mes, anio):
        print("La fecha ingresada es válida.")
    else:
        print("La fecha ingresada no es válida")


if __name__ == "__main__":
    assert _validar_fecha(31, 1, 2026) == True
    assert _validar_fecha(29, 2, 2024) == True
    assert _validar_fecha(30, 4, 2005) == True
    assert _validar_fecha(31, 6, 2047) == False
    assert _validar_fecha(29, 2, 2025) == False
    assert _validar_fecha(30, 2, 2000) == False

    main()