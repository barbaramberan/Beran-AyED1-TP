# TP01 - Ejercicio 03
# Función que recibe como parámetro la cantidad de viajes realizados en un determinado mes y devuelve el total gastado en viajes


def calcular_viajes(viajes: int, precio_boleto: int) -> float:
    """Calcula el valor total a pagar según la cantidad de viajes, el valor de los bolestos y los descuentos correspondientes.

    Precondiciones:
        viajes y precio_bolestos deben ser enteros positivos.
    Postcondiciones:
        devuelve el valor total a pagar en flotante.
    """
    assert viajes > 0, "La cantidad de viajes debe ser mayor a 0"
    assert precio_boleto > 0, "El precio del boleto debe ser un número positivo"

    combinaciones = [
        (20, 0),
        (30, 20),
        (40, 30),
        (999, 40),
    ]  # Lista de tuplas combinando límites de pasajes con su descuento

    total_pagar = 0

    limite_anterior = 0

    for limite, descuento in combinaciones:
        if viajes == 0:
            break
        porcion = min(viajes, limite - limite_anterior)
        total_pagar += porcion * precio_boleto * (1 - descuento / 100)
        viajes -= porcion
        limite_anterior = limite
    return total_pagar


def main() -> None:
    """
    Contrato:
        Ejecuta el programa principal del ejercicio.

    Precondiciones:
        El archivo debe ejecutarse como programa principal.

    Postcondiciones:
        Muestra por pantalla los resultados del ejercicio.
    """

    viajes = int(input("Ingrese la cantidad de viajes realizados este mes: "))
    precio_boleto = 4_000
    gastos_transporte = calcular_viajes(viajes, precio_boleto)
    print(f"El total gastado este mes en transporte es de: {gastos_transporte}$")


if __name__ == "__main__":
    assert calcular_viajes(20, 1_000) == 20_000
    assert calcular_viajes(30, 1_000) == 28_000
    assert calcular_viajes(32, 4_000) == 117_600
    main()
