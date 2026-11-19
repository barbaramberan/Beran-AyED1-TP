# TP06 - EJERCICIO 06
# Registrar el ingreso de huéspedes al hotel, hasta que se ingrese un número de DNI -1.
# Esta información deberá grabarse en un archivo CSV donde cada registro incluirá todos
# los campos indicados más arriba. Tener en cuenta que los números de DNI no pueden
# repetirse y que la fecha de salida debe ser mayor a la de entrada.

# Finalizado el ingreso de huéspedes se solicita:
# a. Leer el archivo de huéspedes y asignar la habitaciones a cada uno. El piso y
# habitación son asignados arbitrariamente, y no puede asignarse una habitación ya otorgada.
# b. Mostrar el piso con mayor cantidad de habitaciones ocupadas.
# c. Mostrar cuántas habitaciones vacías hay en todo el hotel.
# d. Mostrar el piso con mayor cantidad de personas.
# e. Mostrar cuál será la próxima habitación en desocuparse. La fecha actual se ingresa
# por teclado. Mostrar todas las que correspondan.
# f. Mostrar un listado de todos los huéspedes registrados en el hotel, ordenado por
# cantidad de días de alojamiento


import csv
import os
import random
from datetime import date, datetime


# Registro de ingresos
def _cargar_dnis(ruta: str) -> set[int]:
    """
    Contrato:
        Lee el archivo CSV de huéspedes y devuelve los DNI ya registrados.

    Precondiciones:
        Recibe la ruta del archivo CSV. Si el archivo no existe, se considera
        que todavía no hay huéspedes registrados.

    Postcondiciones:
        Retorna un conjunto de enteros con los DNI registrados. Si el archivo
        no existe, retorna un conjunto vacío.
    """
    dnis = set()
    try:
        with open(ruta, "rt", encoding="utf-8", newline="") as arch:
            lector = csv.reader(arch)
            next(lector, None)
            for fila in lector:
                try:
                    dnis.add(int(fila[0]))
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        pass
    return dnis


def _ingresar_dni(dnis: set[int]) -> int:
    """
    Contrato:
        Pide un DNI por teclado hasta que sea válido y no esté repetido.

    Precondiciones:
        Recibe el conjunto de DNI ya registrados. El usuario debe ingresar
        un número entero.

    Postcondiciones:
        Retorna un entero positivo que no está en 'dnis', o -1 si el usuario
        quiere terminar el ingreso.
    """
    while True:
        try:
            dni = int(input("\nIngrese el DNI del cliente (-1 para terminar): "))
            if dni == -1:
                return dni
            if dni <= 0:
                print("El DNI debe ser un número positivo.")
            elif dni in dnis:
                print("Ese DNI ya está registrado.")
            else:
                return dni
        except ValueError:
            print("Debe ingresar un número entero.")


def _ingresar_nombre() -> str:
    """
    Contrato:
        Pide el apellido y nombre del cliente hasta que no esté vacío.

    Precondiciones:
        No recibe parámetros.

    Postcondiciones:
        Retorna un string sin espacios en los extremos y con al menos un carácter.
    """
    while True:
        nombre = input("Ingrese apellido y nombre: ").strip()
        if nombre:
            return nombre
        print("El apellido y nombre no pueden estar vacíos.")


def _ingresar_fecha(msg: str) -> date:
    """
    Contrato:
        Pide una fecha en formato DDMMAAAA hasta que sea válida.

    Precondiciones:
        Recibe el mensaje a mostrar en el input. El usuario debe ingresar
        8 dígitos con el formato DDMMAAAA. Se aceptan años entre 2000 y 2100.

    Postcondiciones:
        Retorna un objeto date con una fecha existente en el calendario.
    """
    while True:
        texto = input(msg).strip()
        try:
            if len(texto) != 8 or not texto.isdigit():
                raise ValueError
            fecha = datetime.strptime(texto, "%d%m%Y").date()
            if 2000 <= fecha.year <= 2100:
                return fecha
        except ValueError:
            pass
        print("Fecha inválida. Use el formato DDMMAAAA (por ejemplo, 05032026).")


def _ingresar_ocupantes() -> int:
    """
    Contrato:
        Pide la cantidad de ocupantes hasta que sea un entero mayor a 0.

    Precondiciones:
        No recibe parámetros. El usuario debe ingresar un número entero.

    Postcondiciones:
        Retorna un entero mayor a 0.
    """
    while True:
        try:
            ocupantes = int(input("Ingrese la cantidad de ocupantes: "))
            if ocupantes > 0:
                return ocupantes
            print("Debe haber al menos un ocupante.")
        except ValueError:
            print("Debe ingresar un número entero.")


def _registrar_ingresos(ruta: str) -> int:
    """
    Contrato:
        Registra el ingreso de huéspedes y los graba en un archivo CSV, hasta
        que se ingrese el DNI -1. Si el archivo no existe, lo crea con
        encabezado. Si existe, agrega los nuevos registros al final.

    Precondiciones:
        Recibe la ruta del archivo CSV. Los DNI no pueden repetirse (se controla
        contra los ya grabados) y la fecha de egreso debe ser mayor a la de ingreso.

    Postcondiciones:
        Retorna un entero con la cantidad de huéspedes registrados en esta
        ejecución. Las fechas se graban en formato DDMMAAAA.
    """
    dnis = _cargar_dnis(ruta)
    registrados = 0
    es_nuevo = not os.path.exists(ruta) or os.path.getsize(ruta) == 0

    with open(ruta, "at", encoding="utf-8", newline="") as arch:
        escritor = csv.writer(arch)
        if es_nuevo:
            escritor.writerow(
                ["DNI", "Apellido y Nombre", "Ingreso", "Egreso", "Ocupantes"]
            )

        while True:
            dni = _ingresar_dni(dnis)
            if dni == -1:
                break
            nombre = _ingresar_nombre()
            ingreso = _ingresar_fecha("Ingrese la fecha de ingreso (DDMMAAAA): ")
            while True:
                egreso = _ingresar_fecha("Ingrese la fecha de egreso (DDMMAAAA): ")
                if egreso > ingreso:
                    break
                print("La fecha de egreso debe ser posterior a la de ingreso.")
            ocupantes = _ingresar_ocupantes()

            escritor.writerow(
                [
                    dni,
                    nombre,
                    ingreso.strftime("%d%m%Y"),
                    egreso.strftime("%d%m%Y"),
                    ocupantes,
                ]
            )
            dnis.add(dni)
            registrados += 1
    return registrados


# A) Lectura y asignación de habitaciones
def _leer_huespedes(ruta: str) -> list[dict]:
    """
    Contrato:
        Lee el archivo CSV de huéspedes y devuelve sus datos.

    Precondiciones:
        Recibe la ruta de un CSV con encabezado y columnas DNI, Apellido y
        Nombre, Ingreso (DDMMAAAA), Egreso (DDMMAAAA) y Ocupantes.

    Postcondiciones:
        Retorna una lista de diccionarios con las claves 'dni', 'nombre',
        'ingreso' (date), 'egreso' (date) y 'ocupantes'. Si el archivo no
        existe, lanza FileNotFoundError.
    """
    huespedes = []
    with open(ruta, "rt", encoding="utf-8", newline="") as arch:
        lector = csv.reader(arch)
        next(lector, None)
        for fila in lector:
            if not fila:
                continue
            huespedes.append(
                {
                    "dni": int(fila[0]),
                    "nombre": fila[1],
                    "ingreso": datetime.strptime(fila[2], "%d%m%Y").date(),
                    "egreso": datetime.strptime(fila[3], "%d%m%Y").date(),
                    "ocupantes": int(fila[4]),
                }
            )
    return huespedes


def _asignar_habitaciones(
    huespedes: list[dict], pisos: int, por_piso: int
) -> list[dict]:
    """
    Contrato:
        Asigna arbitrariamente una habitación a cada huésped, sin repetir.

    Precondiciones:
        Recibe la lista de huéspedes, la cantidad de pisos y la cantidad de
        habitaciones por piso. No puede haber más huéspedes que habitaciones.

    Postcondiciones:
        Retorna una lista nueva de diccionarios, con los datos originales más
        las claves 'piso' y 'habitacion'. Lanza ValueError si no alcanzan las
        habitaciones.
    """
    habitaciones = [(p, h) for p in range(1, pisos + 1) for h in range(1, por_piso + 1)]
    if len(huespedes) > len(habitaciones):
        raise ValueError(
            f"Hay {len(huespedes)} huéspedes y solo {len(habitaciones)} habitaciones."
        )
    random.shuffle(habitaciones)

    asignados = []
    for huesped, (piso, habitacion) in zip(huespedes, habitaciones):
        asignados.append({**huesped, "piso": piso, "habitacion": habitacion})
    return asignados


# B), C), D) Estadísticas por piso
def _habitaciones_por_piso(huespedes: list[dict], pisos: int) -> dict[int, int]:
    """
    Contrato:
        Cuenta las habitaciones ocupadas en cada piso.

    Precondiciones:
        Recibe la lista de huéspedes con habitación asignada y la cantidad de pisos.

    Postcondiciones:
        Retorna un diccionario piso: cantidad de habitaciones ocupadas, con
        todos los pisos (los vacíos con 0).
    """
    conteo = {piso: 0 for piso in range(1, pisos + 1)}
    for huesped in huespedes:
        conteo[huesped["piso"]] += 1
    return conteo


def _personas_por_piso(huespedes: list[dict], pisos: int) -> dict[int, int]:
    """
    Contrato:
        Suma las personas alojadas en cada piso.

    Precondiciones:
        Recibe la lista de huéspedes con habitación asignada y la cantidad de pisos.

    Postcondiciones:
        Retorna un diccionario piso: cantidad de personas, con todos los
        pisos (los vacíos con 0).
    """
    conteo = {piso: 0 for piso in range(1, pisos + 1)}
    for huesped in huespedes:
        conteo[huesped["piso"]] += huesped["ocupantes"]
    return conteo


def _pisos_con_maximo(conteo: dict[int, int]) -> list[int]:
    """
    Contrato:
        Busca los pisos que tienen el valor máximo de un conteo.

    Precondiciones:
        Recibe un diccionario piso: cantidad, no vacío.

    Postcondiciones:
        Retorna la lista de pisos con el valor máximo (más de uno si hay empate).
    """
    maximo = max(conteo.values())
    return [piso for piso, cantidad in conteo.items() if cantidad == maximo]


# E) Próximas habitaciones en desocuparse


def _proximas_a_desocupar(huespedes: list[dict], hoy: date) -> list[dict]:
    """
    Contrato:
        Busca los huéspedes cuya habitación se desocupa primero a partir de hoy.

    Precondiciones:
        Recibe la lista de huéspedes con habitación asignada y la fecha actual.

    Postcondiciones:
        Retorna la lista de huéspedes con la fecha de egreso más cercana, sin
        contar los que ya se fueron (egreso anterior a hoy). Si hay empate, los
        devuelve a todos. Si no hay ninguno, retorna una lista vacía.
    """
    vigentes = [h for h in huespedes if h["egreso"] >= hoy]
    if not vigentes:
        return []
    proximo = min(h["egreso"] for h in vigentes)
    return [h for h in vigentes if h["egreso"] == proximo]


# F) Listado ordenado por días de alojamiento
def _dias_alojamiento(huesped: dict) -> int:
    """
    Contrato:
        Calcula los días de alojamiento de un huésped.

    Precondiciones:
        Recibe un diccionario de huésped con las claves 'ingreso' y 'egreso'.

    Postcondiciones:
        Retorna un entero con la cantidad de días entre el ingreso y el egreso.
    """
    return (huesped["egreso"] - huesped["ingreso"]).days


def _ordenar_por_dias(huespedes: list[dict]) -> list[dict]:
    """
    Contrato:
        Ordena los huéspedes por cantidad de días de alojamiento.

    Precondiciones:
        Recibe la lista de huéspedes.

    Postcondiciones:
        Retorna una lista nueva, ordenada de menor a mayor cantidad de días.
        No modifica la lista original.
    """
    return sorted(huespedes, key=_dias_alojamiento)


# Programa principal
def _mostrar_informe(huespedes: list[dict], pisos: int, por_piso: int) -> None:
    """
    Contrato:
        Muestra por pantalla los puntos b a f del enunciado.

    Precondiciones:
        Recibe la lista de huéspedes con habitación asignada, la cantidad de
        pisos y la de habitaciones por piso. Pide la fecha actual por teclado.

    Postcondiciones:
        No retorna nada. Muestra en pantalla los resultados.
    """
    if not huespedes:
        print("\nNo hay huéspedes registrados.")
        return

    # B) Piso con más habitaciones ocupadas
    ocupadas = _habitaciones_por_piso(huespedes, pisos)
    pisos_b = _pisos_con_maximo(ocupadas)
    texto = ", ".join(str(p) for p in pisos_b)
    print(
        f"\nPiso(s) con más habitaciones ocupadas: {texto} ({ocupadas[pisos_b[0]]} habitaciones)."
    )

    # C) Habitaciones vacías
    vacias = pisos * por_piso - len(huespedes)
    print(f"Habitaciones vacías en todo el hotel: {vacias}.")

    # D) Piso con más personas
    personas = _personas_por_piso(huespedes, pisos)
    pisos_d = _pisos_con_maximo(personas)
    texto = ", ".join(str(p) for p in pisos_d)
    print(f"Piso(s) con más personas: {texto} ({personas[pisos_d[0]]} personas).")

    # E) Próxima habitación en desocuparse
    hoy = _ingresar_fecha("\nIngrese la fecha actual (DDMMAAAA): ")
    proximas = _proximas_a_desocupar(huespedes, hoy)
    if proximas:
        fecha = proximas[0]["egreso"].strftime("%d/%m/%Y")
        print(f"\nPróxima(s) habitación(es) en desocuparse (el {fecha}):")
        for h in proximas:
            print(f"  Piso {h['piso']}, habitación {h['habitacion']} - {h['nombre']}")
    else:
        print("\nNo hay habitaciones por desocuparse a partir de esa fecha.")

    # F) Listado ordenado por días de alojamiento
    print("\nHuéspedes ordenados por días de alojamiento:\n")
    for h in _ordenar_por_dias(huespedes):
        print(
            f"{h['nombre']:<30} {_dias_alojamiento(h):>4} días  "
            f"({h['ingreso'].strftime('%d/%m/%Y')} al {h['egreso'].strftime('%d/%m/%Y')})  "
            f"Piso {h['piso']}, hab. {h['habitacion']}"
        )


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Registra los ingresos, asigna las
        habitaciones y muestra el informe del hotel.

    Precondiciones:
        No recibe parámetros. Pide datos al usuario por teclado.

    Postcondiciones:
        No retorna nada. Muestra en pantalla los resultados.
    """
    ruta = "huespedes.csv"
    pisos = 10
    por_piso = 6

    print("\nBienvenido al sistema de gestión del hotel.")
    try:
        cantidad = _registrar_ingresos(ruta)
        print(f"\nSe registraron {cantidad} huéspedes en '{ruta}'.")
        huespedes = _leer_huespedes(ruta)
        huespedes = _asignar_habitaciones(huespedes, pisos, por_piso)

    except FileNotFoundError as msg:
        print(f"1001: No se encuentra el archivo: {msg}")

    except OSError as msg:
        print(f"1002: No se puede leer o escribir el archivo: {msg}")

    except ValueError as msg:
        print(f"1003: Error en los datos: {msg}")

    else:
        _mostrar_informe(huespedes, pisos, por_piso)


if __name__ == "__main__":
    main()
