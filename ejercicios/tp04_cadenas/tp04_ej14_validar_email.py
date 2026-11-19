# TP04 - EJERCICIO 14
# Se solicita crear un programa para leer direcciones de correo electrónico y verificar
# si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que
# una dirección sea considerada válida el nombre de usuario debe poseer solamente
# caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
# tener al menos un carácter y tiene que finalizar con .com o .com.ar.
# Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar 
# mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
# recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas


def _validar_correo(correo: str) -> bool:
    """
    Contrato:
        Verifica si una dirección de correo electrónico es válida.
    Precondiciones:
        Recibe como parámetro 'correo', una cadena de caracteres que ya debe
        estar en minúscula.
    Postcondiciones:
        Retorna True si la dirección tiene un solo '@', un nombre de usuario
        formado solo por caracteres alfanuméricos, y un dominio sin espacios
        que termina en '.com' o '.com.ar' con al menos un carácter antes de
        esa terminación. Retorna False en cualquier otro caso.
    """
    if correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    if not usuario.isalnum():
        return False
    if " " in dominio:
        return False
    if dominio.endswith(".com.ar"):
        nombre_dominio = dominio[:-7]
    elif dominio.endswith(".com"):
        nombre_dominio = dominio[:-4]
    else:
        return False
    return len(nombre_dominio) > 0


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal. Lee direcciones de correo hasta que se
        ingresa una cadena vacía, indica si cada una es válida y, al finalizar,
        muestra los dominios de las direcciones válidas.
    Precondiciones:
        No recibe parámetros. El usuario debe ingresar cadenas de caracteres.
    Postcondiciones:
        Muestra en pantalla el resultado de cada validación y el listado de
        dominios sin repetir y ordenados alfabéticamente. No distingue
        mayúsculas de minúsculas.
    """
    print("\nEste programa verifica si las direcciones de correo ingresadas son válidas.\n")
    dominios = set()
    while True:
        correo = input("Ingrese una dirección de correo (Enter para terminar): ").strip().lower()
        if not correo:
            break
        if _validar_correo(correo):
            print("La dirección es válida.\n")
            dominios.add(correo.split("@")[1])
        else:
            print("La dirección NO es válida.\n")

    if dominios:
        print("\nDominios de las direcciones válidas, ordenados alfabéticamente:\n")
        for dominio in sorted(dominios):
            print(dominio)
    else:
        print("\nNo se ingresó ninguna dirección válida.")


if __name__ == "__main__":
    main()