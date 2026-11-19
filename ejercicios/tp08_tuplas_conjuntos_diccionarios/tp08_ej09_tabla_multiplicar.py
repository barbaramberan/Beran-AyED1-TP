# TP08 - EJERCICIO 09
# Escribir un programa que permita ingresar un número entero N y genere un diccionario
# por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la tabla de
# multiplicar con el formato apropiado.


def _tabla_multiplicar(n: int) -> dict:
    """
    Contrato:
        Genera un diccionario por comprensión con la tabla de multiplicar de un número N del 1 al 12.
    Precondiciones:
        Recibe n como parámetro. Que debe ser un entero.
    Postcondiciones:
        Retorna un diccionario con clave: valor. siendo clave, del 1 al 12 y valor el resultado de clave por n.
    """
    return {i: n * i for i in range(1, 13)}


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Llama a la función 'tabla_multiplicar'.
    Precondiciones:
        No recibe parámetros. Pide al usuario que ingrese un entero.
    Postcondiciones:
        Muestra en pantalla una tabla de multiplicar del 1 al 12 de un valor n.
    """
    while True:
        try:
            n = int(
                input(
                    "\nIngrese un número para visualizar su tabla de multiplicar del 1 al 12. (-1 para finalizar): "
                )
            )
            if n == -1:
                break
        except ValueError:
            print("\nError. Debe ingresar un número entero.\n")
        tabla = _tabla_multiplicar(n)
        print(f"\nLa tabla de multiplicar de {n}, es la siguiente: \n")
        for clave, valor in tabla.items():
            print(f"{n}  x {clave:3}  = {valor:4}")


if __name__ == "__main__":
    main()
