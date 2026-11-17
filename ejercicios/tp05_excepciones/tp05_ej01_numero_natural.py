# TP05 - EJERCICIO 01
# Desarrollar una función para ingresar a través del teclado un número natural.
# La función rechazará cualquier ingreso inválido de datos utilizando excepciones y
# mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
# número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
# exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
# correcto. Escribir también un programa que permita probar el correcto 
# funcionamiento de la misma.

def numero_natural(numero: any) -> int:
    """
    Contrato:
        Valida si un dato es un número, entero y positivo. De no cumplir con alguna validación,
        levanta un error con un mensaje específico para cada caso.
    Precondiciones:
        Recibe un parámetro que puede ser de cualquier tipo.
    Postcondiciones.
        Si no se levantó ningún error, retorna el dato casteado a entero.
    """
    try:
        numero = float(numero)
    except ValueError:
        raise ValueError("Debe ingresar un número. No un caracter.")
    if int(numero) != numero:
        raise ValueError("El número debe ser un entero.")
    if numero <= 0:
        raise ValueError("El número debe ser mayor a 0.")
    return int(numero)


def main() -> None:
    """
    Contrato:
        Pide al usuario que ingrese un número(hasta que no levante ningún error), se lo pasa como parámetro a 
        numero_natural, e intenta mostrar su resultado por pantalla. Si hay errores, muestra el mensaje de error 
        por pantalla sin romper el programa.
    Precondiciones: 
        El archivo debe ejecutarse como programa principal.
        El usuario debe ingresar un número.
        No recibe parámetros.
    Postcondiciones:
        Muestra por pantalla el número obtenido de numero_natural. 
        O muestra en pantalla un mensaje correspondiente a cada error de ser necesario.
    """
    while True:
        try:
            print(f"El número ingresado es: {numero_natural(input("Ingrese un número: "))}")
        except ValueError as e:
            print(e)
        else:
            break
        
if __name__ == "__main__":
    assert numero_natural(5) == 5
    try:   
        numero_natural(0)

    except ValueError as e:
        assert str(e) == "El número debe ser mayor a 0." 

    try:   
        numero_natural("R")
        
    except ValueError as e1:
        assert str(e1) == "Debe ingresar un número. No un caracter."

    try:   
        numero_natural("3.14")
            
    except ValueError as e2:
        assert str(e2) == "El número debe ser un entero."
    main()

