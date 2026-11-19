# TP06 - Ejercicio 01
# Hecho en grupo en clase

"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con la cadena "IAN", en el archivo
ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los terminados en "EZ". Descartar el resto.
Ejemplo:
    - Arslanian, Gustavo -----> ARMENIA.TXT
    - Rossini, Guiseppe -----> ITALIA.TXT
    - Pérez, Juan -----> ESPAÑA.TXT
    - Smith, John -----> Descartado
El archivo puede ser creado mediante block de notas o en ualquier otro editor.
"""


def leer_archivo() -> None:
    """
    Contrato:
        - Lee un archivo csv de personas y clasifica según su apellido, su origen.

    Precondiciones:
        - No recibe parámetros.

    Precondiciones:
        - No retorna parámetros.
    """

    paises = {"IAN": "ARMENIA.TXT", "INI": "ITALIA.TXT", "EZ": "ESPANIA.TXT"}

    try:
        with open("nombres.txt", "rt", encoding="utf-8-sig") as arch:
            encabezado = arch.readline()

            for linea in arch:
                apellido = linea.split(",")[0].upper().strip()

                for key, value in paises.items():
                    if apellido.endswith(key):
                        with open(value, "at", encoding="utf-8") as es:
                            es.write(linea)

    except FileNotFoundError as msg:
        print(f"1001: No se encuentra el archivo: {msg}")

    except OSError as msg:
        print(f"1002: No se puede leer el archivo: {msg}")

    except:
        print("1003: Error en los datos.")

    else:
        print(f"\nArchivo leído correctamente.")


def main() -> None:
    """ "Programa principal."""
    leer_archivo()


if __name__ == "__main__":
    main()
 