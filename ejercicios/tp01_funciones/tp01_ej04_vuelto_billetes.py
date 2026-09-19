# TP01 - Ejercicio 04
# Programa para calcular que billetes deben ser entregados al dar un vuelto con la mínima cantidad de billetes.

# Profe considero que es un código poco optimizado, y poco algorítmico, pero por el momento es lo que se me ocurrió sin recurrir a la IA.


def calcular_vuelto(compra: int, pago: int) -> list:
    """
    Contrato:
      Calcula qué cantidad de cada billete se debe dar como vuelto en un comercio, calculando módulos y división entera para cada billete.
    Precondiciones:
        compra y pago deben ser enteros positivos.
    Postcondiciones:
        devuelve una lista de tuplas, donde cada tupla corresponde al tipo de billete y a la cantidad del mismo a devolver.

    """
    vuelto = pago - compra
    cant_5_000 = vuelto // 5_000
    resto = vuelto % 5_000
    cant_1_000 = resto // 1_000
    resto = resto % 1_000
    cant_500 = resto // 500
    resto = resto % 500
    cant_200 = resto // 200
    resto = resto % 200
    cant_100 = resto // 100
    resto = resto % 100
    cant_50 = resto // 50
    resto = resto % 50
    cant_10 = resto // 10
    resto = resto % 10
    if resto > 0:
        print(
            f"No es posible devolver los {resto}$ restantes. Te puedo dar un caramelo."
        )
    lista_vuelto = [
        (5_000, cant_5_000),
        (1_000, cant_1_000),
        (500, cant_500),
        (200, cant_200),
        (100, cant_100),
        (50, cant_50),
        (10, cant_10),
    ]
    return lista_vuelto


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """
    compra = int(input("Ingrese el total de la compra: "))
    pago = int(input("Ingrese el monto abonado por el cliente: "))

    if pago < compra:
        print("El monto abonado es insuficiente para realizar la compra")
    else:
        lista_billetes = calcular_vuelto(compra, pago)
        print("El vuelto es de: ")
        for billete, cantidad in lista_billetes:
            if cantidad != 0:
                print(f"{cantidad} billetes de {billete}$, ")


if __name__ == "__main__":
    main()
