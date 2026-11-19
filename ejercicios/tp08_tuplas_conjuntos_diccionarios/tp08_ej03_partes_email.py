# TP03 - EJERCICIO 03
# Desarrollar un programa que utilice una función que reciba como parámetro una
# cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
# una tupla con las distintas partes que componen dicha dirección. Ejemplo:
# alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
# formatos de fecha inválidos y devolver una tupla vacía.


def _partes_email(direccion: str) -> tuple[str]:
    """
    Contrato:
        Función que recibe una dirección de correo electrónico, separa sus partes y las devuelve en una tupla.
        De no ser una dirección válida devuelve una tupla vacía.
    Precondiciones:
        Recibe como parámetro 'direccion', que debe ser una cadena de caracteres correspondiente a
        una dirección de correo electrónico.(Se considera válido el correo con un '@', al menos 1 '.' y máximo 2 '.')
    Postcondiciones:
        Retorna una tupla con las partes del correo, o una tupla vacía de no ser una dirección válida.
    """
    if direccion.count("@") != 1:
        return ()

    usuario, dominio = direccion.split("@")
    if usuario == "" or dominio == "":
        return ()
    if " " in usuario or " " in dominio:
        return ()
    dominio = dominio.split(".")
    for i in dominio:
        if not i:
            return ()
    if len(dominio) == 1 or len(dominio) > 3:
        return ()

    return (usuario,) + tuple(dominio)


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Pide al usuario que ingrese un correo electrónico y llama a la función.
    Precondiciones:
        No recibe parámetros.
    Postcondiciones:
        Muestra en pantalla los resultados.
    """
    while True:
        direccion = input("Ingrese una dirección de correo electrónico: ")
        tupla = _partes_email(direccion)
        if tupla != ():
            print(tupla)
            break
        else:
            print("\nLa dirección de correo electrónico no es válida.\n")


if __name__ == "__main__":
    main()
