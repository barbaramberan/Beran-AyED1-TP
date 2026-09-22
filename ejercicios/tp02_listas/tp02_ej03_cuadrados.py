# TP02 - Ejercicio 03
# Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista


def crear_lista_cuadrados() -> list[int]:
    """
    Contrato:
        Crea una lista con los cuadrados de los números entre 1 y n inclusive.
    Precondiciones:
        n es ingresado por el usuario y debe ser un entero positivo mayor a 0.
    Postcondiciones:
        Devuelve una lista de enteros positivos.
    """
    n = int(
        input(
            "Vamos a crear una lista con los cuadrados de números.\n¿Cuántos elementos quiere que tenga?\nIngrese un número entero positivo: "
        )
    )
    return [x**2 for x in range(1, n + 1)]


lista = crear_lista_cuadrados()
print(f"Ésta es nuestra lista:\n{lista}\n")
if len(lista) >= 10:
    print(lista[-10:])
