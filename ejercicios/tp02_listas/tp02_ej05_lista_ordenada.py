# TP02 - Ejercicio 05
# Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función.

lista_ordenada = lambda lista: lista == sorted(lista)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. A partir de una serie de listas definidas, llama a la función 'lista_ordenada' para comprobar si están ordenadas o no.
    Precondiciones:
        El archivo debe ejecutarse como programa principal. No recibe parámetros.
    Postcondiciones:
        Muestra en pantalla las listas y si están o no ordenadas de forma ascendente.
    """
    lista1 = [x for x in range(10)]
    lista2 = [4, 6, 8, 1, 4, 3, 2]
    lista3 = ["a", "b", "c", "d", "e"]
    lista4 = ["d", "g", "a", "f"]

    print(
        f"Vamos a verificar si las siguientes listas están ordenadas de forma ascendente:\n"
    )
    print(f"{lista1}?: {lista_ordenada(lista1)}\n")
    print(f"{lista2}?: {lista_ordenada(lista2)}\n")
    print(f"{lista3}?: {lista_ordenada(lista3)}\n")
    print(f"{lista4}?: {lista_ordenada(lista4)}\n")


if __name__ == "__main__":
    main()
