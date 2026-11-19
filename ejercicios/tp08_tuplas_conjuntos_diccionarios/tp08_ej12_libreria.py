# TP08 - EJERCICIO 12
# Una librería almacena su lista de precios en un diccionario. Diseñar un programa
# para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
# listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
# costoso que venden en el comercio.


def _ingresar_lista_precios() -> dict[str, float]:
    """
    Contrato:
        Crea el diccionario con la lista de precios de la librería, que ya
        incluye tres cuadernos, y le permite al usuario agregar más artículos.
    Precondiciones:
        No recibe parámetros. El usuario debe ingresar el nombre de cada artículo
        (los cuadernos deben incluir la palabra 'cuaderno') y su precio como un
        número mayor a 0. Para terminar la carga, debe dejar el nombre vacío.
    Postcondiciones:
        Retorna un diccionario con clave: nombre del artículo (str) y
        valor: precio (float). Siempre contiene los cuadernos iniciales, salvo
        que el usuario ingrese un artículo con el mismo nombre: en ese caso se
        conserva el último precio ingresado.
    """
    precios = {
        "cuaderno rayado": 8500.0,
        "cuaderno cuadriculado": 8600.0,
        "cuaderno universitario": 9800.0,
    }

    print("\nLa librería ya tiene cargados estos artículos:\n")
    for articulo, precio in precios.items():
        print(f"{articulo:<25} $ {precio:>10.2f}")
    print("\nPuede agregar más artículos.\n")

    while True:
        articulo = (
            input("Ingrese el nombre del artículo (Enter para terminar): ")
            .strip()
            .lower()
        )
        if not articulo:
            break
        while True:
            try:
                precio = float(input(f"Ingrese el precio de '{articulo}': "))
                if precio > 0:
                    break
                print("El precio debe ser mayor a 0.")
            except ValueError:
                print("Debe ingresar un número.")
        precios[articulo] = precio
    return precios


def _aumentar_cuadernos(
    precios: dict[str, float], porcentaje: float
) -> dict[str, float]:
    """
    Contrato:
        Incrementa en un porcentaje el precio de los artículos cuyo nombre
        contiene la palabra 'cuaderno'.
    Precondiciones:
        Recibe un diccionario con nombres (str) y precios (float), y un porcentaje
        numérico. Los nombres de los cuadernos deben incluir la palabra 'cuaderno'
        (se ignoran mayúsculas y minúsculas).
    Postcondiciones:
        Retorna el mismo diccionario modificado, con los precios de los cuadernos
        incrementados y redondeados a 2 decimales. El resto no se modifica.
    """
    for articulo in precios:
        if "cuaderno" in articulo.lower():
            precios[articulo] = round(precios[articulo] * (1 + porcentaje / 100), 2)
    return precios


def _item_mas_costoso(precios: dict[str, float]) -> tuple[str, float]:
    """
    Contrato:
        Busca el artículo más costoso de la lista de precios.
    Precondiciones:
        Recibe un diccionario no vacío con nombres (str) y precios (float).
    Postcondiciones:
        Retorna una tupla con el nombre y el precio del artículo más costoso.
        Si hay varios con el mismo precio máximo, retorna el primero.
    """
    articulo = max(precios, key=precios.get)
    return (articulo, precios[articulo])


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Crea la lista de precios (con tres cuadernos
        precargados y los artículos que ingrese el usuario), aumenta los cuadernos
        un 15%, imprime el listado e indica el ítem más costoso.
    Precondiciones:
        No recibe parámetros. Pide al usuario que ingrese artículos y sus precios.
    Postcondiciones:
        Muestra en pantalla los resultados de las funciones.
    """
    precios = _ingresar_lista_precios()

    print("\nLista de precios original:\n")
    for articulo, precio in precios.items():
        print(f"{articulo:<25} $ {precio:>10.2f}")

    precios = _aumentar_cuadernos(precios, 15)

    print("\nLista de precios con los cuadernos incrementados un 15%:\n")
    for articulo, precio in precios.items():
        print(f"{articulo:<25} $ {precio:>10.2f}")

    nombre, precio = _item_mas_costoso(precios)
    print(f"\nEl ítem más costoso es '{nombre}' y cuesta $ {precio:.2f}.\n")


if __name__ == "__main__":
    main()
