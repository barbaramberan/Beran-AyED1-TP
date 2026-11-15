# TP04 - EJERCICIO 06
# Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
# indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
# como valor de retorno. Escribir también un programa para verificar el comporta-
# miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
# 7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
# resultando la subcadena "4356-7890".


# a) Utilizando rebanadas:
def subcadena_a(cadena: str, posicion: int, cant: int) -> str:
    """
    Contrato:
        Extrae una subcadena de una cadena, a partir de una posición y con
        una cantidad de caracteres dada, utilizando rebanadas.

    Precondiciones:
        cadena debe ser un string.
        posicion y cant deben ser enteros mayores o iguales a 0.
        posicion + cant no debe superar el largo de cadena.

    Postcondiciones:
        Devuelve un string nuevo con cant caracteres de cadena, empezando
        en la posición indicada (la primera posición es la 0).
        No modifica la cadena original.
    """
    return cadena[posicion : (posicion + cant)]


# b) Sin utilizar rebanadas:
def subcadena_b(cadena: str, posicion: int, cant: int) -> str:
    """
    Contrato:
        Extrae una subcadena de una cadena, a partir de una posición y con
        una cantidad de caracteres dada, sin utilizar rebanadas.

    Precondiciones:
        cadena debe ser un string.
        posicion y cant deben ser enteros mayores o iguales a 0.
        posicion + cant no debe superar el largo de cadena.

    Postcondiciones:
        Devuelve un string nuevo con cant caracteres de cadena, empezando
        en la posición indicada (la primera posición es la 0).
        No modifica la cadena original.
    """
    subcadena = ""
    for i in range(posicion, (posicion + cant)):
        subcadena += cadena[i]
    return subcadena


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar una cadena y dos enteros (posición y
        cantidad).

    Postcondiciones:
        Pide posición y cantidad hasta que ambas sean mayores o iguales a 0
        y su suma no supere el largo de la cadena. Muestra por pantalla la
        subcadena obtenida con cada una de las dos versiones.
    """

    cadena = input("Ingrese una cadena de caracteres: ")
    while True:
        posicion = int(input("En qué posición desea que empiece la subcadena?: "))
        cant = int(input("Cuántos caracteres quiere que tenga la subcadena?: "))
        if posicion + cant <= len(cadena) and cant >= 0 and posicion >= 0:
            break
    print(subcadena_a(cadena, posicion, cant))
    print(subcadena_b(cadena, posicion, cant))


if __name__ == "__main__":
    assert subcadena_a("El número de teléfono es 4356-7890", 25, 9) == "4356-7890"
    assert subcadena_b("El número de teléfono es 4356-7890", 25, 9) == "4356-7890"
    main()
