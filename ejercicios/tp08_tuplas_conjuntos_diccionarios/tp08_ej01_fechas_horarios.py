# TP08 - EJERCICIO 01
# Desarrollar las siguientes funciones utilizando tuplas para representar fechas y
# horarios, y luego escribir un programa que las vincule


# A) Ingresar una fecha desde el teclado, verificando que corresponda a una fecha válida.
def _bisiesto(anio: int) -> bool:
    """
    Contrato:
        Calcula si un año es bisiesto.
    Precondiciones:
        Recibe un año (número entero) como parámetro.
    Postcondiciones:
        Retorna True si el año es bisiesto o False de no serlo.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


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
            anio = int(input("Ingrese un año: "))
            if 0 < dia < 32 and 0 < mes < 13 and 999 < anio < 3001:
                break
            else:
                print("Debe ingresar una fecha válida.")
        except ValueError:
            print("Debe ingresar una fecha válida.")
    return (dia, mes, anio)


def _validar_fecha(fecha: tuple[int, int, int]) -> bool:
    """
    Contrato:
        Recibe una fecha en formato tupla de enteros y valida que
        los datos juntos correspondan a una fecha válida.
    Precondiciones:
        Fecha debe ser una tupla de enteros, cada dato de la tupla debe ser individualmente
        un dato válido según el formato de una fecha.
    Postcondiciones:
        Retorna False para cualquier fecha no válida.
        Retorna True para toda fecha válida.
    """
    dia, mes, anio = fecha
    meses_31 = (1, 3, 5, 7, 8, 10, 12)
    meses_30 = (4, 6, 9, 11)
    es_bisiesto = _bisiesto(anio)
    if mes in meses_30 and dia > 30:
        return False
    elif mes in meses_31 and dia > 31:
        return False
    elif mes == 2:
        dias_febrero = 29 if es_bisiesto else 28
        if dia > dias_febrero:
            return False
    return True


# B) Sumar N días a una fecha.
# Usé Claude para que me ayude a pensar la lógica de como resolver esta función.
# Yo estaba metiendo unos ciclos de if y elif anidados interminables.
def _dias_del_mes(mes: int, anio: int) -> int:
    """
    Contrato:
        Función que recibe mes y anio y retorna cuántos días tiene ese mes en ese año.
    Precondiciones:
        Mes y anio deben ser enteros correspondientes a números válidos según su rango.
    Postcondiciones:
        Retorna un entero (28, 29, 30 o 31) según corresponda a cada mes.
    """
    meses_31 = (1, 3, 5, 7, 8, 10, 12)
    meses_30 = (4, 6, 9, 11)
    es_bisiesto = _bisiesto(anio)
    if mes == 2:
        return 29 if es_bisiesto else 28
    elif mes in meses_30:
        return 30
    elif mes in meses_31:
        return 31


def _sumar_dias(fecha: tuple[int], n: int) -> tuple[int]:
    """
    Contrato:
        Función que recibe una fecha válida como parámetros y le suma n días.
    Precondiciones:
        Fecha debe ser una tupla de enteros, correspondientes a una fecha válida.
    Postcondiciones:
        Retorna una tupla de enteros con la fecha actualizada.
    """
    dia, mes, anio = fecha
    for i in range(n):
        dia += 1
        if dia > _dias_del_mes(mes, anio):
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1
    return (dia, mes, anio)


# C) Ingresar un horario desde teclado, verificando que sea correcto.
def _ingresar_hora() -> tuple[int]:
    """
    Contrato:
        Pide al usuario que ingrese una horario en formato horas y minutos.
        Verifica que sea un horario válido.
    Precondiciones:
        No recibe parámetros. Los datos ingresados por el usuario deben ser
        números enteros.
    Postcondiciones:
        Retorna una tupla correspondiente a (hora, minutos).
    """
    while True:
        try:
            hora = int(input("Ingrese una hora: "))
            minutos = int(input("Ingrese los minutos: "))
            if (minutos >= 0 and minutos < 60) and (hora >= 0 and hora < 24):
                print("\nEl horario ingresado es correcto.\n")
                break
            else:
                print("Debe ingresar una hora entre 0 y 23 y minutos entre 0 y 59.\n")
        except ValueError:
            print("Debe ingresar una hora entre 0 y 23 y minutos entre 0 y 59.\n")
    return (hora, minutos)


# D) Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
# segundo se considerará que el primero corresponde al día anterior. En ningún
# caso la diferencia en horas puede superar las 24 horas.


def _diferencia_horarios(horario1: tuple[int], horario2: tuple[int]) -> tuple[int, int]:
    """
    Contrato:
        Función que recibe dos tuplas de enteros, correspondientes a dos horarios
        y calcula la diferencia de horas y minutos entre ambas.
    Precondiciones:
        Recibe horario1 y horario2 como parámetros. Deben ser tuplas de enteros correspondientes
        a horarios válidos. La diferencia entre ambos horarios no debe ser mayor a 24 horas.
    Postcondiciones:
        Retorna una tupla de enteros correspondiente a las horas y minutos que hay
        de diferencia entre los dos horarios
    """
    hora1, minuto1 = horario1
    hora2, minuto2 = horario2
    minutos1 = (hora1 * 60) + minuto1
    minutos2 = (hora2 * 60) + minuto2
    diferencia = minutos2 - minutos1
    if diferencia < 0:
        diferencia += 24 * 60
    return divmod(diferencia, 60)


def main() -> None:
    """
    Contrato:
        Programa principal que vincula las funciones del ejercicio.
    Precondiciones:
        No recibe parámetros.
        Debe ejecutarse como archivo principal
    Postcondiciones:
        Muestra en pantalla los resultados de las funciones.
    """
    print("Vamos a jugar un poco con las fechas y los horarios.\n")
    while True:
        fecha = _ingresar_fecha()
        if _validar_fecha(fecha):
            print("La fecha ingresada es válida.\n")
            print("Ahora vamos a agregarle días a esa fecha.\n")
            fecha_sumada = _sumar_dias(
                fecha, int(input("¿Cuántos días querés sumarle?: "))
            )
            print(f"\nAl sumarle esos días, la nueva fecha es: {fecha_sumada}.\n")
            break
        else:
            print("La fecha ingresada no corresponde a una fecha válida.\n")
    print(
        "Ahora vamos con los horarios.\nVas a ingresar dos horarios y te voy a calcular la diferencia de horas entre ambos.\n"
    )
    dif_horas, dif_min = _diferencia_horarios(_ingresar_hora(), _ingresar_hora())
    print(
        f"\nLa diferencia de horas entre los dos horarios que ingresaste es de {dif_horas} horas y {dif_min} minutos."
    )


if __name__ == "__main__":
    main()
