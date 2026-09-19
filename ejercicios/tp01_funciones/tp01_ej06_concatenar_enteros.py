# TP01 - Ejercicio 06
# Función para concatenar dos números enteros


def concatenar(a: int, b: int) -> int:
    """
    Contrato:
        Concatena dos números enteros positivos, descomponiendo b para saber por cuántos digitos hay que multiplicar a antes de sumarle b.
    precondiciones:
        a y b tienen que ser enteros positivos.
    postcondiciones:
        Devuelve un entero compuesto por a y b
    """
    contador = 0
    aux = b

    while aux != 0:
        aux = aux // 10
        contador += 1

    concatenado = a * (10**contador) + b
    return concatenado


a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))
print(f"El resultado de unir esos dos números es: {concatenar(a,b)}")
