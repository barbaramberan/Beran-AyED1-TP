# TP08 - EJERCICO 08
# Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
# 20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.

def diccionario_cuadrados() -> None:
    """
    Contrato:
        Genera e imprimir un diccionario donde las claves son números enteros entre 1 y
        20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
    Precondiciones:
        No recibe parámetros.
    Postcondiciones:
        Muestra el diccionario por pantalla.
    """
    print({num: num * num for num in range(1, 21)})


diccionario_cuadrados()