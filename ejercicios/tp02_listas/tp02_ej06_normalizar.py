# TP02 - Ejercicio 06
# Escribir una función que reciba una lista de números enteros como parámetro y la normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar también un programa que permita verificar el comportamiento de la función.

# En matemática o probabilidad: que todo sume 1
# Si tenés una lista de enteros, normalizarla es dividir cada valor por la suma total:


def normalizar(lista: list[int]) -> list[float]:
    """
    Contrato:
        Divide cada elemento de la lista por la suma total de sus elementos. Devuelve una lista normaliada a 1.0.
    Precontrato:
        Recibe como parámetro una lista de enteros.
    Postcondiciones:
        Retorna una lista de enteros flotantes.
    """
    normalizada = list(map(lambda elemento: elemento / sum(lista), lista))
    return normalizada


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. A partir de una serie de listas definidas, llama a la función 'normalizar'.
     Precondiciones:
        El archivo debe ejecutarse como programa principal. No recibe parámetros, el usuario debe ingresar un entero entre 1 y 4.
    Postcondiciones:
        Muestra en pantalla las listas originales, y las listas normalizadas a 1.0.
    """
    lista1 = [1, 1, 2]
    lista2 = [2, 3, 4, 5]
    lista3 = [7, 8, 9]
    lista4 = [45, 65, 2, 7]

    print(
        f"Ingrese que lista quiere normalizar:\n1. {lista1}\n2. {lista2}\n3. {lista3}\n4. {lista4}\n"
    )
    op = int(input(":"))
    if op == 1:
        print(normalizar(lista1))

    elif op == 2:
        print(normalizar(lista2))

    elif op == 3:
        print(normalizar(lista3))

    elif op == 4:
        print(normalizar(lista4))

    else:
        print("Opción incorrecta. Ingrese un número del 1 al 4.")


if __name__ == "__main__":
    main()
