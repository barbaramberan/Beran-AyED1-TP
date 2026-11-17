# TP05 - EJERCICIO 05
# La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
# módulo math. Escribir un programa que utilice esta función para calcular la raíz
# cuadrada de un número cualquiera ingresado a través del teclado. El programa
# debe utilizar manejo de excepciones para evitar errores si se ingresa un número negativo

from math import sqrt

def cuadradas(num: int):
    """
    Contrato:
        Función para calcular la raíz cuadrada de un número.
    Precondiciones:
        num debe ser un entero.
    Postcondiciones:
        Retorna un número float.
    """
    return sqrt(num)

def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.
    
    Precondiciones:
        El archivo debe ejecutarse como programa principal.
    
    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    while True:
        try:
            resultado = cuadradas(int(input("Ingrese un número para calcular su raíz cuadrada: ")))
            print(f"\nLa raiz cuadrada del número ingresado es: {resultado}.\n")
            break
        except ValueError:
            print("\nDato inválido. Debe ingresar un número entero positivo.\n")


if __name__ == "__main__":
    main()