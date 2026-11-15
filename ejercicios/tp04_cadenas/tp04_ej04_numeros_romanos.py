# TP04 - EJERCICIO 04
# Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
# lo convierta en un número romano, devolviéndolo en una cadena de caracteres.

# Me costó mucho pensarlo. Fui a revisar el ejercicio de vuelto de billetes y no me ayudó en nada,
# pues estaba muy poco algorítmico, así que empecé mejorando ese primero.


def num_romano(numero: int) -> str:
    """
    Contrato:
        Convierte un número entero a su representación en números romanos,
        recorriendo los valores de mayor a menor y calculando con división
        entera y módulo cuántas veces entra cada símbolo.

    Precondiciones:
        numero debe ser un entero entre 0 y 3999 inclusive.

    Postcondiciones:
        Devuelve una cadena con el número romano equivalente.
        Si numero es 0, devuelve una cadena vacía y muestra por pantalla un
        mensaje aclarando que el cero no existe en números romanos.
    """
    romanos = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    valores = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    cantidades = []
    num = ""
    for i in valores:
        cantidades.append(numero // i)
        numero = numero % i
    for c, r in zip(cantidades, romanos):
        num += c * r
    if num == "":
        print("No existe el cero en números romanos.")
    return num


numero = 4000
while numero < 0 or numero > 3999:
    numero = int(
        input("Ingrese un número entre 0 y 3999 que desee convertir a número romano: ")
    )
print(num_romano(numero))
