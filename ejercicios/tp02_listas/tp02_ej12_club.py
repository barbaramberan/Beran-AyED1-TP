# TP02 - Ejercicio 12
#


def registrar_socio(lista: list[int]) -> None:
    """
    Lee el número de socio, y lo agrega a la lista de ingresos.
    Precondiciones:
        Recibe como parámetros una lista de enteros. El número de socio debe ser un entero positivo de 5 dígitos.
    Postcondiciones:
        No retorna nada, pero agrega los valores de num_socio a la lista que se recibió como parámetro y la muestra en pantalla.
    """
    while True:
        num_socio = int(input("Ingrese su número de socio. (Ingrese 0 para salir): "))
        if num_socio == 0:
            break
        while num_socio < 10000 or num_socio > 99999:
            num_socio = int(
                input(
                    "Número de socio incorrecto. Debe ingresar un número de 5 dígitos: "
                )
            )
        lista.append(num_socio)
    print(f"\nEsta es la lista de socios que ingresaron al club hoy:\n\n{lista}\n")


def lista_unicos(lista: list[int]) -> list[int]:
    """
    Contrato:
        Funcion que recibe una lista, la recorre y agrega sus valores no repetidos a otra lista.
    Precondiciones:
        Recibe como parámetrto una lista de enteros.
    Postcondiciones:
        Retorna una lista de enteros no repetidos.
    """
    lista1 = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)
    return lista1


def informar_cantidad(lista: list[int], lista1: list[int]) -> list[int]:
    """
    Contrato:
        Funcion que recibe dos listas y se fija cuántas veces aparece cada valor de la lista1 en lista y agrega esas cantidades en una nueva lista.
    Precondiciones:
        lista y lista1 deben ser listas de enteros.
    Postcondiciones:
        Retorna la nueva lista con las cantidades de veeces q aparecen los elementos de lista1 en lista.
    """
    lista_cantidad = []
    for i in lista1:
        lista_cantidad.append(lista.count(i))
    return lista_cantidad


def num_eliminar() -> int:
    """
    Contraro:
        Pide al usuario ingresar el número de socio cuyos ingresos desea eliminar.
    Precondiciones:
        El número ingresado por el usuario debe ser un entero positivo de 5 dígitos.
    Postcondiciones:
        Retorna el número entero ingresado por el usuario.
    """
    num_eliminar = int(
        input(
            "\nIngrese el número de socio que se dio de baja y se desea borrar de los ingresos: "
        )
    )
    while num_eliminar < 10000 or num_eliminar > 99999:
        num_eliminar = int(
            input(
                "\nNúmero de socio incorrecto. Debe ingresar un número de 5 dígitos: "
            )
        )
    return num_eliminar


def eliminar_socio(lista: list[int], numero: int) -> int:
    """
    Contrato:
        Función que recibe como parámetros una lista y un número. Muestra la lista en pantalla, luego recorre la lista y agrega a una nueva lista todos los valores que no sean iguales al número recibido. Muestra en pantalla la nueva lista actualizada.
    Precondiciones:
        Los parámetros recibidos deben ser una lista de enteros y un número entero.
    Postcondiciones:
        Retorna un entero que representa la cantidad de ingresos que fueron eliminados.
    """
    print(f"\nLa siguiente lista muestra los ingresos actuales:\n{lista}")
    lista_actualizada = []
    for i in lista:
        if i != numero:
            lista_actualizada.append(i)
    print(
        f"\nLa lista de ingresos actualizada tras eliminar los ingresos del socio es:\n{lista_actualizada}"
    )
    eliminados = len(lista) - len(lista_actualizada)
    return eliminados


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Crea una lista vacía y llama a las funciones del programa.
    Precondiciones:
        No recibe parámetros.
    Postcondiciones:
        No retorna nada, pero muestra en pantalla listas de socios a treves de las funciones.
    """
    lista_socios = []
    registrar_socio(lista_socios)
    socios = lista_unicos(lista_socios)
    cantidades = informar_cantidad(lista_socios, socios)
    for s, c in zip(socios, cantidades, strict=True):
        print(f"El socio n°: {s} ingresó {c} veces al club hoy.")
    eliminar = num_eliminar()
    eliminados = eliminar_socio(lista_socios, eliminar)
    print(f"\nLa cantidad de ingresos que fueron eliminados es {eliminados}.")


if __name__ == "__main__":
    main()
