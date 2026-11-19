# TP06 - EJERCICIO 03
# EMPEZADO EN GRUPO EN CLASE. TERMINADO INDIVIDUALMENTE.

"""
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los próximos juegos panamericanos.
Para eso encargó la realización de un programa que incluya las siguientes funciones:

grabar_rango_alturas(): Graba en un archivo las alturas de los atletas de distintas disciplinas,
los que se ingresan desde el teclado. Cada dato se debe grabar en una linea distinta.

grabar_promedio(): Graba en un archivo los promedios de las alturas de los atletas,
leyendo los datos del archivo generado en el paso anterior. La disciplina y el promedio debe grabarse en lineas diferentes.

mostrar_mas_altos(): Muestra por pantalla las disciplinas deportivas cuyos atletas superan la estatura promedio general.
Obtener los datos del segundo archivo.
"""


def _ingresar_cadena(msg: str) -> str:
    """
    Contrato:
        - Permite ingresar datos por teclado.

    Precondiciones:
        - Recibe un string, mensaje de input.

    Postcondiciones:
        - str; devuelve el dato ingresado por teclado.
    """
    return input(msg)


def grabar_rango_alturas(deportes: set[str]) -> bool:
    """
    Contrato:
        - Graba en un archivo (si no existe, lo crea) las alturas de los distintos atletas de las distintas disciplinas.

    Precondiciones:
        - Un conjunto de str: Conjunto de disciplinas a grabar.

    Postcondiciones:
        - True si se pudo realizar las acciones correctamente.
        - False si hubo error de grabado o no hay acciones a realizar.
    """
    if not deportes:
        return False

    with open("alturas_por_deporte.txt", "at", encoding="utf-8") as arch:

        for deporte in deportes:
            arch.write(deporte + "\n")
            print(f"Deporte: {deporte}")

            while True:
                altura = _ingresar_cadena(
                    "Ingrese la altura del atleta (-1 para salir): "
                )

                if altura == "-1":
                    break

                arch.write(altura + "\n")
    return True


def grabar_promedio(ruta: str, ruta_nueva: str) -> bool:
    """
    Contrato:
        Graba en un archivo (si no existe, lo crea) el promedio de las alturas de los
        atletas de las distintas disciplinas.

    Precondiciones:
        Un conjunto de str: Conjunto de disciplinas a grabar.

    Postcondiciones:
        True si se pudo realizar las acciones correctamente.
        False si hubo error de grabado o no hay acciones a realizar.
    """
    suma = 0.0
    contador = 0
    titulo = None
    if not ruta:
        return False

    with open(ruta, "r", encoding="utf-8-sig") as arch:
        with open(ruta_nueva, "at", encoding="utf-8-sig") as arch_p:
            for linea in arch:
                if not linea.strip():
                    continue
                try:
                    altura = float(linea)
                    suma += altura
                    contador += 1
                except ValueError:
                    if titulo is not None and contador > 0:
                        promedio = suma / contador
                        arch_p.write(f"{titulo}")
                        arch_p.write(f"{promedio}\n")

                    titulo = linea
                    contador = 0
                    suma = 0.0

            if titulo is not None and contador > 0:
                promedio = suma / contador
                arch_p.write(f"{titulo}")
                arch_p.write(f"{promedio}\n")
    return True


def mostrar_mas_Altos(ruta: str) -> list:
    promedio = 0
    suma = 0.0
    contador = 0
    titulo = None
    mas_altos = []
    with open(ruta, "r", encoding="utf-8-sig") as arch_pr:
        for linea in arch_pr:
            if not linea.strip():
                continue
            try:
                altura = float(linea)
                suma += altura
                contador += 1
            except ValueError:
                continue
        try:
            promedio = suma / contador
        except ZeroDivisionError:
            print(
                "El archivo no contiene los datos necesarios para calcular el promedio."
            )
            return mas_altos
        arch_pr.seek(0)
        for linea in arch_pr:
            if not linea.strip():
                continue
            try:
                if float(linea) > promedio:
                    mas_altos.append(titulo.strip())
            except ValueError:
                titulo = linea.strip()

    return mas_altos


def main() -> None:
    """ "Programa principal."""
    deportes = {
        "Fútbol",
        "Básquetbol",
        "Golf",
        "Waterpolo",
        "Judo",
        "Rugby",
        "BMX",
        "Críquet",
    }
    opciones = [
        "1: Grabar alturas de los deportistas",
        "2: Grabar promedio de alturas por disciplina",
        "3: Mostrar qué disciplinas tienen atletas con el promedio "
        "de altura superior al promedio general.",
    ]
    while True:
        for element in opciones:
            print(element)
        op = input("Ingrese qué opción desea realizar: ")
        if op == "1":
            alturas = grabar_rango_alturas(deportes)
            if alturas:
                print(
                    "Las alturas se han guardado correctamente en el archivo 'alturas_por_deporte.txt'."
                )
            else:
                print("Ocurrió un error. Los datos no han sido guardados.")
        if op == "2":
            promedios = grabar_promedio(
                "alturas_por_deporte.txt", "promedio_alturas.txt"
            )
            if promedios:
                print(
                    "El promedio de las alturas de los atletas por disciplina se ha calculado correctamente y guardado en el archivo 'promedio_alturas.txt'."
                )
            else:
                print("Ocurrió un error. No se ha podido calcular el promedio.")
        if op == "3":
            mostrar = mostrar_mas_Altos("promedio_alturas.txt")
            print(
                "Las siguientes disciplinas cuentan con atletas cuyo promedio de alaturas es superior al promedio general:"
            )
            for element in mostrar:
                print(element)


if __name__ == "__main__":
    main()
