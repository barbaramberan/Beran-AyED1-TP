# TP01 - Ejercicio 05
# Creación de funciones lambda para informar si un número es oblongo y triangular.
# Primero voy a crear una función normal y luego crearé una lambda.

# def _es_oblongo(num: int) -> bool:
#     """
#     Recibe un número entero, y evalúa si el producto de dos números consecutivos es igual a este entero.

#     precondiciones:
#         El número ingresado debe ser entero.
#     Postcondiciones:
#         Devuelve True si el producto de dos números consecutivos es igual al número ingresado. De lo contrario devuelve False
#     """
#     k = 0
#     n = 0
#     while k <= num:
#         k = n * (n+1)
#         if k == num:
#             return True
#         else:
#             n += 1
#     return False

# def main() -> None:
#     """
#         Contrato:
#             Ejecuta el programa principal del ejercicio.

#         Precondiciones:
#             El archivo debe ejecutarse como programa principal.

#         Postcondiciones:
#             Muestra por pantalla los resultados del ejercicio.
#     """
#     num = int(input("Ingrese el número que quiera probar: "))
#     if _es_oblongo(num):
#         print("El número ingresado es oblongo.")
#     else:
#         print("El número ingresado no es oblongo")

# if __name__ == "__main__":
#     assert _es_oblongo(6) == True, "6 = 2x3 debería ser oblongo"
#     assert _es_oblongo(0) == True, "0 = 0x1 debería ser oblongo"
#     assert _es_oblongo(-3) == False, "los negativos no son oblongos"
#     assert _es_oblongo(12) == True, "12 = 3x4 debería ser oblongo"

#     main()

# Ahora vamos con la lambda, la cuál me di cuenta que hay que pensar de manera muyb diferente y no se puede adaptar la función antetrior.
# Usé la IA para ayudarme a descubrir qué funcion matemática tenía que aplicar y en ambas funciones se utiliza Bhaskara
es_oblongo = lambda num: (
    (-1 + (1 + 4 * num) ** 0.5) / 2 == int((-1 + (1 + 4 * num) ** 0.5) / 2)
    if num >= 0
    else False
)

es_triangular = lambda num: (
    (-1 + (1 + 8 * num) ** 0.5) / 2 == int((-1 + (1 + 8 * num) ** 0.5) / 2)
    if num >= 0
    else False
)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio pidiendo el número a evaluar y llamando a las funciones.

    Precondiciones:
        El archivo debe ejecutarse como programa principal y num debe ser entero.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    num = int(input("Ingrese el número que quiera probar: "))
    if es_oblongo(num):
        print("El número ingresado es oblongo.")
    else:
        print("El número ingresado no es oblongo")

    if es_triangular(num):
        print("El número ingresado es triangular.")
    else:
        print("El número ingresado no es triangular")


if __name__ == "__main__":
    assert _es_oblongo(6) == True
    assert _es_oblongo(0) == True
    assert _es_oblongo(-3) == False
    assert _es_oblongo(12) == True
    assert _es_triangular(3) == True
    assert _es_triangular(6) == True
    assert _es_triangular(0) == True
    assert _es_triangular(5) == False
    assert _es_triangular(-2) == False

    main()
