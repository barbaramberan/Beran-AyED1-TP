# TP08 - EJERCICIO 07
# Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
# usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido
# del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
# Utilizar manejo de excepciones para evitar errores al intentar quitar elementos inexistentes.


def eliminar_valores() -> None:
    numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    print(f"En este programa hay un conjunto de números del 0 al 9:\n{numeros}\n")
    while True:
        candidato = int(
            input("Ingrese qué valor desea eliminar del conjunto (-1 PARA FINALIZAR): ")
        )
        try:
            numeros.remove(candidato)
            print("\nEl número fue eliminado correctamente.\n")
            if numeros:
                print(f"{numeros}\n")
            if not numeros:
                print("El conjunto fue completamente eliminado. ¡Hasta luego!")
                candidato == -1
            if candidato == -1:
                break
        except KeyError:
            print(
                "\nEl número ingresado no puede ser eliminado, ya que no se encuentra en el conjunto.\n"
            )


eliminar_valores()
