# TP02 - Ejercicio 11
# Programa para clínica. Se ingresa número de afiliado y si viene por urgencia o con turno. Se muestra un listado de pacientes de urgencias y con turno. Se permite buscar por número de afiliado cuántas veces fue atendido de urgencias y cuántas con turno.


def leer_afiliado(lista_u: list, lista_t: list) -> None:
    """
    Lee el número de afiliado, y en qué carácter se presenta a la clínica. Según en carácter, agrega el núnmero de afiliado a la lista correspondiente.
    Precondiciones:
        Recibe como parámetros dos listas de enteros. El número de afiliado debe ser un entero de 4 dígitos.
    Postcondiciones:
        No retorna nada, ni muestra nada en pantalla. Agrega los valores de num_afiliado a la lista correspondiente según validación de carácter.
    """
    while True:
        num_afiliado = int(
            input(
                "Ingrese su número de afiliado. (Ingrese -1 para dejar de ingresar afiliados): "
            )
        )
        if num_afiliado == -1:
            break
        while num_afiliado < 1000 or num_afiliado > 9999:
            num_afiliado = int(
                input(
                    "Número de afiliado incorrecto. Debe ingresar un número de 4 dígitos: "
                )
            )
        caracter = int(
            input("Ingerse '0' si viene por una urgenica o '1' si viene con turno: ")
        )
        while caracter < 0 or caracter > 1:
            caracter = int(
                input(
                    "Valor incorrecto. Ingerse '0' si viene por una urgenica o '1' si viene con turno: "
                )
            )
        if caracter == 0:
            lista_u.append(num_afiliado)
        elif caracter == 1:
            lista_t.append(num_afiliado)


def buscar_afiliado(lista_u: list[int], lista_t: list[int]) -> None:
    """
    Contraro:
        Pide al usuario ingresar un número de afiliado, luego busca cuántas veces fue atendido de urgencias y cuántas con turno.
    Precondiciones:
        Recibe como parámetros dos listas de enteros.
    Postcondiciones:
        No retorna nada, pero muestra en pantalla la cantidad de veces que un paciente fue atendido de urgencias y cuántas con turno.
    """
    while True:
        num_afiliado = int(
            input(
                "Ingrese el número de afiliado que desea buscar. (Ingrese -1 para salir): "
            )
        )
        if num_afiliado == -1:
            break
        cantidad_u = lista_u.count(num_afiliado)
        cantidad_t = lista_t.count(num_afiliado)
        print(
            f"Ese afiliado fue atendido {cantidad_u} veces de urgencia, y {cantidad_t} veces con turno."
        )


def main() -> None:
    """
     Ejecuta el programa principal. Crea dos listas vacías y llama a las funciones del programa.
     Precondiciones:
        No recibe parámetros.
    Postcondiciones:
        No retorna nada, pero muestra en pantalla listas de pacientes a treves de las funciones.
    """
    lista_u = []
    lista_t = []
    leer_afiliado(lista_u, lista_t)
    print(f"Este es un listado con los pacientes atendidos por urgencias:\n{lista_u}")
    print(f"Este es un listado con los pacientes atendidos con turno:\n{lista_t}")
    buscar_afiliado(lista_u, lista_t)


if __name__ == "__main__":
    main()
