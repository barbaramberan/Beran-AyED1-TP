# TP 05 - EJERCICIO 06
# El método index permite buscar un elemento dentro de una lista, devolviendo la
# posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
# produce una excepción de tipo ValueError. Desarrollar un programa que cargue
# una lista con números enteros ingresados a través del teclado (terminando con -1)
# y permita que el usuario ingrese el valor de algunos elementos para visualizar la
# posición que ocupan, utilizando el método index. Si el número no pertenece a la
# lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
# proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.


def crear_lista() -> list:
    """
    Contrato:
        Función para crear una lista con numeros enteros ingresados por el usuario.
    Precondiciones:
        No recibe parámetros, los números ingresados por el usuario deben ser enteros.
    Postcondiciones:
        Retorna una lista de enteros.
    """
    lista = []
    enteros = 0
    while enteros != -1:
        enteros = int(
            input(
                "Ingrese un número entero para añadir a la lista. Ingrese -1 cuando quiera finalizar la misma:"
            )
        )
        lista.append(enteros)
    print(f"La lista que creó es la siguente:\n{lista}")
    return lista


def buscar_elemento(num: int, lista: list) -> int:
    """
    Contrato:

    Precondiciones:
        Recibe dos parámetros, un entero y una lista de enteros.
    Postcondiciones:

    """
    errores = 1
    while True:
        try:
            return lista.index(num)
        except ValueError:
            if errores < 3:
                print("El número que desea buscar no se encuentra en la lista.")
                num = int(input("Intente con otro número: "))
                errores += 1
            else:
                print("Demasiados intentos fallidos.")
                exit()


def main() -> None:
    """
    Contrato:

    Precondiciones:

    Postcondiciones:

    """
    lista = crear_lista()
    num = int(input("Ingrese qué número desea buscar en la lista: "))
    print(
        f"El número que solicitó buscar, se encuentra en la posición {buscar_elemento(num, lista) +1} de la lista."
    )


if __name__ == "__main__":
    main()
