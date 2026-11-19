# TP04 - EJERCICIO 13
# Muchas aplicaciones financieras requieren que los números sean expresados 
# también en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento
# cincuenta y tres". Escribir un programa que utilice una función para convertir un
# número entero entre 0 y 1 billón (1.000.000.000.000) a letras. 


def _menor_a_mil(n: int) -> str:
    """
    Contrato:
        Convierte a letras un número entero entre 1 y 999.
    Precondiciones:
        Recibe un entero n, con 1 <= n <= 999.
    Postcondiciones:
        Retorna el número escrito en letras. El 1 final se escribe 'uno'
        (por ejemplo, 'ciento uno').
    """
    unidades = (
        "cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho",
        "nueve", "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis",
        "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós",
        "veintitrés", "veinticuatro", "veinticinco", "veintiséis", "veintisiete",
        "veintiocho", "veintinueve",
    )
    decenas = (
        "", "", "", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta",
        "ochenta", "noventa",
    )
    centenas = (
        "", "ciento", "doscientos", "trescientos", "cuatrocientos", "quinientos",
        "seiscientos", "setecientos", "ochocientos", "novecientos",
    )
    if n == 100:
        return "cien"
    centena, resto = divmod(n, 100)
    partes = []
    if centena:
        partes.append(centenas[centena])
    if resto:
        if resto < 30:
            partes.append(unidades[resto])
        else:
            decena, unidad = divmod(resto, 10)
            if unidad:
                partes.append(f"{decenas[decena]} y {unidades[unidad]}")
            else:
                partes.append(decenas[decena])
    return " ".join(partes)


def _acortar_uno(texto: str) -> str:
    """
    Contrato:
        Cambia el 'uno' final por 'un' (y 'veintiuno' por 'veintiún'), como
        corresponde cuando el número va delante de 'mil', 'millón' o 'billón'.
    Precondiciones:
        Recibe un texto con un número escrito en letras.
    Postcondiciones:
        Retorna el texto con el cambio aplicado, si correspondía.
    """
    if texto.endswith("veintiuno"):
        return texto[:-3] + "ún"
    if texto.endswith("uno"):
        return texto[:-1]
    return texto


def _menor_a_millon(n: int) -> str:
    """
    Contrato:
        Convierte a letras un número entero entre 1 y 999.999.
    Precondiciones:
        Recibe un entero n, con 1 <= n <= 999999.
    Postcondiciones:
        Retorna el número escrito en letras.
    """
    miles, resto = divmod(n, 1000)
    partes = []
    if miles == 1:
        partes.append("mil")
    elif miles > 1:
        partes.append(_acortar_uno(_menor_a_mil(miles)) + " mil")
    if resto:
        partes.append(_menor_a_mil(resto))
    return " ".join(partes)


def _numero_a_letras(n: int) -> str:
    """
    Contrato:
        Convierte a letras un número entero entre 0 y 1 billón.
    Precondiciones:
        Recibe un entero n, con 0 <= n <= 1.000.000.000.000.
    Postcondiciones:
        Retorna el número escrito en letras. Se usa la escala larga
        (1 billón = 1.000.000.000.000).
    """
    if n == 0:
        return "cero"
    billones, resto = divmod(n, 10 ** 12)
    millones, unidades = divmod(resto, 10 ** 6)
    partes = []
    if billones == 1:
        partes.append("un billón")
    elif billones > 1:
        partes.append(_acortar_uno(_menor_a_millon(billones)) + " billones")
    if millones == 1:
        partes.append("un millón")
    elif millones > 1:
        partes.append(_acortar_uno(_menor_a_millon(millones)) + " millones")
    if unidades:
        partes.append(_menor_a_millon(unidades))
    return " ".join(partes)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Pide un número entero y lo muestra en letras.
    Precondiciones:
        No recibe parámetros. El usuario debe ingresar un entero entre 0 y
        1.000.000.000.000.
    Postcondiciones:
        Muestra en pantalla el número escrito en letras.
    """
    print("\nEste programa escribe en letras un número entero entre 0 y 1 billón.\n")
    while True:
        try:
            numero = int(input("Ingrese un número: "))
            if 0 <= numero <= 10 ** 12:
                break
            print("El número debe estar entre 0 y 1.000.000.000.000.")
        except ValueError:
            print("Debe ingresar un número entero.")
    print(f"\n{numero:,} se escribe: {_numero_a_letras(numero)}.\n".replace(",", "."))


if __name__ == "__main__":
    main()