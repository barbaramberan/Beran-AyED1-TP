# TP08 - EJERCICIO 05
# En geometría un vector es un segmento de recta orientado que va desde un punto
# A hasta un punto B.
# Dos vectores son ortogonales cuando son perpendiculares entre sí. Para determinarlo
# basta calcular su producto escalar y verificar si es igual a 0.
# Escribir una función que reciba dos vectores en forma de tuplas y devuelva un valor
# de verdad indicando si son ortogonales o no. Desarrollar también un programa que
# permita verificar el comportamiento de la función.


def _ortogonales(a: tuple[int], b: tuple[int]) -> bool:
    """
    Contrato:
        Función que recibe dos vectores en forma de tupla y devuelve si son ortogonales o no.
    Precondiciones:
        a y b deben ser tuplas de dos enteros.
    Postcondiciones:
        Retorna True si los vectores son ortogonales y False si no lo son.
    """
    return a[0] * b[0] + a[1] * b[1] == 0


def _ingresar_vector(nombre: str) -> tuple[int]:
    """
    Contrato:
        Función que pide dos enteros, los valida y los devuelve en forma de tupla.
    Precondiciones:
        Recibe como parámetros un string.
    Postcondiciones:
        Retorna una tupla de dos enteros.
    """
    while True:
        try:
            x = int(input(f"Ingrese el valor A del {nombre} vector: "))
            y = int(input(f"Ingrese el valor B del {nombre} vector: "))
            return (x, y)
        except ValueError:
            print(
                "El vector ingresado no es válido. Por favor respete el formato e ingrese números enteros."
            )


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Llama a la función 'ortogonales()'.
    Precondiciones:
        No recibe parámetros. Pide al usuario que ingrese enteros para formar dos tuplas de dos enteros cada una.
    Postcondiciones:
        No retorna nada, muestra en pantalla los resultados de la función.
    """
    print(
        "El siguiente programa sirve para comprobar si dos vectores son ortogonales.\n"
    )
    print(
        "En geometría un vector es un segmento de recta orientado que va desde un punto A hasta un punto B.\n"
    )
    print("Dos vectores son ortogonales cuando son perpendiculares entre sí.\n")
    vector_1 = _ingresar_vector("primer")
    vector_2 = _ingresar_vector("segundo")
    son_ortogonales = _ortogonales(vector_1, vector_2)
    if son_ortogonales:
        print("Los vectores ingresados son ortogonales.")
    else:
        print("Los vectores ingresados NO son ortogonales.")


if __name__ == "__main__":
    assert _ortogonales((2, 3), (-3, 2)) == True
    assert _ortogonales((1, 2), (3, 4)) == False
    assert _ortogonales((1, 0), (0, 5)) == True
    assert _ortogonales((0, 0), (7, 9)) == True
    main()
