# TP08 - EJERCICIO 13
# Escribir una función buscarclave() que reciba como parámetros un diccionario y un
# valor, y devuelva una lista de claves que apunten ("mapeen") a ese valor en el diccionario. 
# Comprobar el comportamiento de la función mediante un programa apropiado.

def _buscar_clave(diccionario: dict, valor) -> list:
    """
    Contrato:
        Busca en un diccionario todas las claves que apuntan a un valor dado.
    Precondiciones:
        Recibe un diccionario y un valor a buscar. Los valores del diccionario
        deben poder compararse con 'valor' mediante ==.
    Postcondiciones:
        Retorna una lista con las claves cuyo valor es igual a 'valor', en el
        orden en que aparecen en el diccionario. Si ninguna clave apunta a ese
        valor, retorna una lista vacía. No modifica el diccionario.
    """
    claves = []
    for clave, valor_actual in diccionario.items():
        if valor_actual == valor:
            claves.append(clave)
    return claves

# Le pedí a claude que me ayude con los asserts para que no me queden tan largos como en el ejercicio 10,
#  y me recomendó esto:
def _probar_buscar_clave() -> None:
    """
    Contrato:
        Verifica con assert el comportamiento de 'buscar_clave'.
    Precondiciones:
        No recibe parámetros.
    Postcondiciones:
        No retorna nada. Lanza AssertionError si algún caso falla.
    """
    casos = [
        ({"a": 1, "b": 2, "c": 1}, 1, ["a", "c"]),
        ({"a": 1, "b": 2, "c": 1}, 2, ["b"]),
        ({"a": 1, "b": 2, "c": 1}, 5, []),
        ({}, 1, []),
        ({"x": "hola", "y": "chau", "z": "hola"}, "hola", ["x", "z"]),
    ]
    for diccionario, valor, esperado in casos:
        assert _buscar_clave(diccionario, valor) == esperado


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Arma un diccionario de prueba, pide un
        valor al usuario y muestra las claves que apuntan a ese valor.
    Precondiciones:
        No recibe parámetros. El usuario debe ingresar un número entero.
    Postcondiciones:
        Muestra en pantalla las claves encontradas o un mensaje si no hay ninguna.
    """
    edades = {
        "Ana": 20,
        "Luis": 25,
        "Marta": 20,
        "Pedro": 30,
        "Sofía": 25,
        "Juan": 20,
    }

    print("\nEste programa busca qué claves apuntan a un valor del diccionario.\n")
    print("El diccionario (nombre: edad) es:\n")
    for nombre, edad in edades.items():
        print(f"{nombre:<10} {edad:>3}")

    while True:
        try:
            valor = int(input("\nIngrese la edad que desea buscar: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    claves = _buscar_clave(edades, valor)
    if claves:
        print(f"\nLas personas con {valor} años son: {', '.join(claves)}.\n")
    else:
        print(f"\nNo hay ninguna persona con {valor} años.\n")


if __name__ == "__main__":
    _probar_buscar_clave()
    main()