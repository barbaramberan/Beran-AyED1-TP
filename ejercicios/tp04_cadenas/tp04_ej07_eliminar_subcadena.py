# TP04 - EJERCICIO 07
# Escribir una función para eliminar una subcadena de una cadena de caracteres, a
# partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
# Reciclo el main del ejercicio anterior, por la similitud de las consignas.


# A) Utilizando rebanadas:
def eliminar_a(cadena: str, posicion: int, cant: int) -> str:
    """
    Contrato:
        Elimina una subcadena de una cadena, a partir de una posición y con
        una cantidad de caracteres dada, utilizando rebanadas.

    Precondiciones:
        cadena debe ser un string.
        posicion y cant deben ser enteros mayores o iguales a 0.
        posicion + cant no debe superar el largo de cadena.

    Postcondiciones:
        Devuelve un string nuevo sin la cantidad de caracteres que empiezan en la
        posición indicada (la primera posición es la 0).
        No modifica la cadena original.
    """
    return cadena[:posicion] + cadena[posicion + cant :]


# B) Sin utilizar rebanadas:
def eliminar_b(cadena: str, posicion: int, cant: int) -> str:
    """
    Contrato:
        Elimina una subcadena de una cadena, a partir de una posición y con
        una cantidad de caracteres dada, sin utilizar rebanadas.

    Precondiciones:
        Cadena debe ser un string.
        posicion y cant deben ser enteros mayores o iguales a 0.
        posicion + cant no debe superar el largo de cadena.

    Postcondiciones:
        Devuelve un string nuevo sin la cantidad de caracteres que empiezan en la
        posición indicada (la primera posición es la 0).
        No modifica la cadena original.
    """
    resultado = ""
    for i in range(len(cadena)):
        if i not in range(posicion, posicion + cant):
            resultado += cadena[i]
    return resultado


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar una cadena y dos enteros (posición y
        cantidad).

    Postcondiciones:
        Pide posición y cantidad hasta que su suma no supere el largo de la
        cadena. Muestra por pantalla la cadena resultante de eliminar la
        subcadena con cada una de las dos versiones.
    """

    cadena = input("Ingrese una cadena de caracteres: ")
    while True:
        posicion = int(
            input("En qué posición desea que empiece la subcadena a eliminar?: ")
        )
        cant = int(
            input(
                "Cuántos caracteres quiere que tenga la subcadena que desea eliminar?: "
            )
        )
        if posicion + cant <= len(cadena) and cant >= 0 and posicion >= 0:
            break
    print(eliminar_a(cadena, posicion, cant))
    print(eliminar_b(cadena, posicion, cant))


if __name__ == "__main__":
    assert (
        eliminar_a("El número de teléfono es 4356-7890", 25, 9)
        == "El número de teléfono es "
    )
    assert (
        eliminar_b("El número de teléfono es 4356-7890", 25, 9)
        == "El número de teléfono es "
    )
    main()
