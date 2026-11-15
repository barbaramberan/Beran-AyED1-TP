# TP04 - EJERCICIO 08
# Desarrollar una función que devuelva una subcadena con los últimos N caracteres
# de una cadena dada. La cadena y el valor de N se pasan como parámetros.


def ultimos(cadena: str, num: int) -> str:
    """
    Contrato:
        Dada una cadena y un entero (num), devuelve los úlimos (num) caracteres de la cadena.
    Precondiciones:
        Cadena debe ser un string no vacío.
        num debe ser un entero mayor a 0, e igual o menor al largo de la cadena.
    Postcondiciones:
        Devuelve un string con los num últimos caracteres de la cadena.
    """
    return cadena[-num:]


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar una cadena y un entero (cantidad de
        caracteres).

    Postcondiciones:
        Pide la cadena hasta que no esté vacía, y pide la cantidad hasta que
        sea mayor a 0 y no supere el largo de la cadena. Muestra por pantalla
        los últimos caracteres de la cadena, según la cantidad indicada.
    """
    while True:
        cadena = input("Ingrese una oración: ")
        if cadena:
            break
    while True:
        num = int(
            input(
                "Ingrese el número de cuántos caracteres del final "
                "de la oración quiere ver: "
            )
        )
        if num > 0 and num <= len(cadena):
            break

    print(ultimos(cadena, num))


if __name__ == "__main__":
    assert ultimos("hola profe", 5) == "profe"
    assert ultimos("hola profe", 10) == "hola profe"
    assert ultimos("hola profe", 1) == "e"
    main()
