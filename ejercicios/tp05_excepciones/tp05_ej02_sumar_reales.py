# tp05 - ejercicio 02
# Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo 
# números reales, sume ambos valores y devuelva el resultado como un número real.
# Devolver -1 si alguna de las cadenas no contiene un número válido,
# utilizando manejo de excepciones para detectar el error

def caracteres_a_reales(num1: str, num2: str) -> float:
    """
    Contrato:
        Recibe dos cadenas de caracteres con números reales. Los castea y devuelve su suma como número real,
        o devuelve -1 si algúno de los datos no es válido.
    Precondiciones:
        num1 y num2 deben ser cadenas de caracteres.
    Postcondiciones:
        Retorna un número real con la suma de num1 y num2. De levantarse algún error retorna -1.
    """
    try:
        return float(num1) + float(num2)
    except ValueError:
        return -1

def main() -> None:
    """
    Contrato:
        Pide al usuario dos números reales, hasta obtener datos validos, y se los pasa como 
        parámetros a caracteres_a_reales.
    Precondiciones:
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar dos números reales.
        No recibe parámetros.
    Postcondiciones:
        Muestra en pantalla la suma de los números reales, o un mensaje de dato inválido de ser el caso.
    """
    while True:
        num1 = input("Ingrese un número real: ")
        num2 = input("Ingrese otro número real: ")
        if caracteres_a_reales(num1, num2) != -1:
            print(f"La suma de los números ingresados es: {caracteres_a_reales(num1, num2)}")
            break
        else:
            print("Dato inválido. Debe ingresar dos números reales.")

if __name__ == "__main__":
    main()
