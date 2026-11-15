# TP04 - EJERCICIO 10
# Desarrollar una función para reemplazar todas las apariciones de una palabra por
# otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
# cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
# palabras completas, y no fragmentos de palabras.


def reemplazar(cadena: str, palabra1: str, palabra2: str) -> tuple:
    """
    Contrato:
        Reemplaza todas las apariciones de una palabra completa por otra en
        una cadena, y cuenta cuántos reemplazos se hicieron.

    Precondiciones:
        cadena, palabra1 y palabra2 deben ser strings no vacíos.
        palabra1 y palabra2 no deben contener espacios.
        Las palabras de cadena están separadas por espacios y no llevan
        signos de puntuación pegados.

    Postcondiciones:
        Devuelve una tupla (cadena_reemplazada, contador).
        Solo se reemplazan palabras completas, no fragmentos de palabras.
        Las palabras de la cadena nueva quedan separadas por un solo espacio.
        Distingue mayúsculas de minúsculas.
        Si palabra1 no está en la cadena, devuelve la cadena con las palabras
        sin cambios y cantidad 0.
    """
    lista = cadena.split()
    contador = 0
    for i in range(len(lista)):
        if lista[i] == palabra1:
            lista[i] = palabra2
            contador += 1
    return (" ".join(lista), contador)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar una cadena y dos palabras.

    Postcondiciones:
        Pide cada dato hasta que no esté vacío. Muestra por pantalla la
        cadena resultante y la cantidad de reemplazos, o un aviso si la
        palabra a reemplazar no se encuentra en la cadena.
    """
    while True:
        cadena = input("Ingrese una cadena de caracteres: ")
        if cadena.strip():
            break
    while True:
        palabra1 = input("Qué palabra de la cadena desea reemplazar?: ").strip()
        if palabra1 and " " not in palabra1:
            break
    while True:
        palabra2 = input("Por cuál palabra quiere reemplazarla?: ").strip()
        if palabra2 and " " not in palabra2:
            break

    cadena_reemplazada, contador = reemplazar(cadena, palabra1, palabra2)
    if contador:
        print(
            f"La palabra {palabra2} reemplazó a la palabra {palabra1} {contador} veces."
            f"\nLa cadena quedó así: {cadena_reemplazada}"
        )
    else:
        print(f"La palabra {palabra1} no se encuentra en la cadena de caracteres.")


if __name__ == "__main__":
    assert reemplazar(
        "Profe estuve rompiéndome el cerebro con estos ejercicios",
        "rompiéndome",
        "usando",
    ) == ("Profe estuve usando el cerebro con estos ejercicios", 1)
    assert reemplazar("probando la función probando", "probando", "comprobando") == (
        "comprobando la función comprobando",
        2,
    )
    assert reemplazar("esta queda igual", "reemplazo", "ausente") == (
        "esta queda igual",
        0,
    )
    main()
