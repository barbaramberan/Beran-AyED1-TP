# TP01 - Ejercicio 01
# Función que recibe tres números enteros positivos y devuelve el mayor de los tres sólo si éste es único.


def mayor_unico(a: int, b: int, c: int) -> int:
    """
    Recibe tres números enteros positivos y devuelve el mayor de los tres sólo si éste es único, de lo contrario devuelve -1.
    
    Precondiciones: 
        a, b, c deben ser números enteros.
    Postcondiciones: 
        Devuelve el mayor número único o -1 si no hay un mayor único.
    """
    if a > b:
        if a > c:
            return a
        elif  c > a:
            return c
        else:
            return -1 
    else:
        if b > a:
            if b > c:
                return b
            else:
                if c > b:
                    return c
                else:
                    return -1
        else: 
            if c > a:
                return c
            else:
                return -1

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))   
c = int(input("Ingrese el tercer número: "))
mayor = mayor_unico(a, b, c)
if mayor != -1:
    print(f"\nEl mayor número único es: {mayor}") 
else:
    print("\nNo hay un mayor número único.")
