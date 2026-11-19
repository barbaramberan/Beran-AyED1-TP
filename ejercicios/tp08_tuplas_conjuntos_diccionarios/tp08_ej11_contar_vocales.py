# TP08 - EJERCICIO 11
# Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
# contiene, identificando la cantidad de cada una. Devolver un diccionario con los
# resultados. Luego desarrollar un programa para leer una frase e invocar a la
# función por cada palabra que contenga la misma. Imprimir las palabras y la
# cantidad de vocales hallada.

def _contarvocales(palabra: str) -> dict[str, int]:
    """
    Contrato:
        Función que recibe una palabra y cuenta cuántas vocales
        contiene, identificando la cantidad de cada una.
        Las vocales con tílde se cuentan como vocal normal.
    Precondiciones:
        Recibe un string como parámetro.
    Postcondiciones:
        Retorna un diccionario con cada vocal y la cantidad que hay en la palabra.
    """
    vocales = ('A', 'E', 'I', 'O', 'U')
    equivalencias = {"Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U", "Ü": "U"}
    diccionario = {}
    palabra = palabra.upper()
    for tilde, basica in equivalencias.items():
        palabra = palabra.replace(tilde, basica)
    for vocal in vocales:
        diccionario[vocal] = palabra.count(vocal)
    return diccionario

def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Pide al usuario que ingrese una cadena de strings.
        Llama a '_contarvocales' por cada palabra en la frase ingresada por el usuario.
    Precondiciones:
        No recibe parámetros. El usuario debe ingresar una cadena de strings.
    Postcondiciones:
        Muestra en pantalla los resultados de las funciones.
    """
    print("\nEste programa calcula cuántas vocales hay en cada palabra que ingreses.\n")
    frase = input("Ingresá una oración: ")
    palabras = frase.strip().split()
    for palabra in palabras:
        resultados = _contarvocales(palabra)
        total = sum(resultados.values())
        if total == 0:
            print(f"\nLa palabra: '{palabra}' no tiene vocales.\n")
        else:
            print(f"\nLa palabra '{palabra}' tiene en total {total} vocales: \n")
            for vocal, cantidad in resultados.items():
                if cantidad > 0:
                    print(f"{cantidad} letras '{vocal}'")


if __name__ == "__main__":
    main()
            
