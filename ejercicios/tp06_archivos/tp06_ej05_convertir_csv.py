# TP06 - EJERCICIO 05
# Desarrollar un programa para convertir cada uno de los formatos suministrados,
# grabando los datos obtenidos en otro archivo con formato CSV. Los archivos de
# entrada pueden generarse con Block de Notas o cualquier otro editor, copiando y
# pegando los ejemplos proporcionados.
# Ambos archivos tienen tres campos por registro: Apellido y Nombre, Fecha de alta
# y Domicilio

import csv


def separar_formato1(linea: str, anchos: tuple[int, ...]) -> list[str]:
    """
    Contrato:
        Separa un registro de longitud fija en sus campos.

    Precondiciones:
        Recibe la línea (sin salto de línea) y una tupla con el ancho de cada
        campo, excepto el último, que ocupa el resto de la línea. Los campos
        están separados por un espacio.

    Postcondiciones:
        Retorna una lista de strings, uno por campo, sin espacios en los extremos.
    """
    campos = []
    pos = 0
    for ancho in anchos:
        campos.append(linea[pos : pos + ancho].strip())
        pos += ancho + 1
    campos.append(linea[pos:].strip())
    return campos


def separar_formato2(linea: str) -> list[str]:
    """
    Contrato:
        Separa un registro en el que cada campo está precedido por un número
        de dos dígitos que indica su longitud.

    Precondiciones:
        Recibe la línea (sin salto de línea). Puede tener cualquier cantidad
        de campos.

    Postcondiciones:
        Retorna una lista de strings, uno por campo. Lanza ValueError si el
        prefijo no son dos dígitos o si el campo es más corto que lo indicado.
    """
    campos = []
    pos = 0
    while pos < len(linea):
        prefijo = linea[pos : pos + 2]
        if len(prefijo) < 2 or not prefijo.isdigit():
            raise ValueError(f"longitud inválida en la posición {pos}")
        largo = int(prefijo)
        pos += 2
        if pos + largo > len(linea):
            raise ValueError(
                f"el campo que empieza en {pos} es más corto de lo indicado"
            )
        campos.append(linea[pos : pos + largo])
        pos += largo
    return campos


def convertir_a_csv(
    ruta_entrada: str, ruta_salida: str, separar, encabezado: list[str]
) -> int:
    """
    Contrato:
        Lee un archivo de texto, separa los campos de cada registro con la
        función recibida y los graba en un archivo CSV.

    Precondiciones:
        Recibe la ruta de entrada, la ruta de salida, una función que recibe
        una línea y devuelve la lista de campos, y la lista con el encabezado.

    Postcondiciones:
        Retorna la cantidad de registros convertidos. Lanza FileNotFoundError
        si no existe el archivo de entrada y ValueError (indicando el número
        de línea) si algún registro es inválido.
    """
    cantidad = 0
    with open(ruta_entrada, "rt", encoding="utf-8-sig") as arch:
        with open(ruta_salida, "wt", encoding="utf-8-sig", newline="") as salida:
            escritor = csv.writer(salida)
            escritor.writerow(encabezado)
            for numero, linea in enumerate(arch, start=1):
                linea = linea.rstrip("\r\n")
                if not linea.strip():
                    continue
                try:
                    escritor.writerow(separar(linea))
                except ValueError as msg:
                    raise ValueError(f"línea {numero}: {msg}")
                cantidad += 1
    return cantidad


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Convierte los archivos de empleados
        de los formatos 1 y 2 a archivos CSV.

    Precondiciones:
        No recibe parámetros. Deben existir 'empleados1.txt' y 'empleados2.txt'.

    Postcondiciones:
        No retorna nada. Muestra en pantalla el resultado de cada conversión.
    """
    encabezado = ["Apellido y Nombre", "Fecha de alta", "Domicilio"]
    anchos = (16, 8)

    conversiones = [
        (
            "empleados1.txt",
            "empleados1.csv",
            lambda linea: separar_formato1(linea, anchos),
        ),
        ("empleados2.txt", "empleados2.csv", separar_formato2),
    ]

    for entrada, salida, separar in conversiones:
        try:
            cantidad = convertir_a_csv(entrada, salida, separar, encabezado)

        except FileNotFoundError as msg:
            print(f"1001: No se encuentra el archivo: {msg}")

        except OSError as msg:
            print(f"1002: No se puede leer o escribir el archivo: {msg}")

        except ValueError as msg:
            print(f"1003: Error en los datos de '{entrada}': {msg}")

        else:
            print(f"Se convirtieron {cantidad} registros de '{entrada}' a '{salida}'.")


if __name__ == "__main__":
    main()
