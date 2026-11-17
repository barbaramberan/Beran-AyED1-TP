# TP05 - EJERCICIO 04
# Todo programa Python es susceptible de ser interrumpido mediante la pulsación de
# las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt. Realizar
# un programa para imprimir los números enteros entre 1 y 100000, y que solicite
# confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

import time


def interrupcion() -> None:
    """
    Contrato:
        Programa para imprimir los números enteros entre 1 y 100000, y que solicita
        confirmación al usuario antes de detenerse cuando se presione Ctrl-C. Si se vuelve a
        presionar ctrl-C antes de confirmar, se pide que confirme.
    Precondiciones:
        No recibe parámetros.
    Postcondiciones:
        Muestra en pantalla los números del 1 al 100_000.
    """
    numero = 1
    limite = 10000
    while numero < limite:
        try:
            print(numero)
            numero += 1

        except KeyboardInterrupt:
            while True:
                try:
                    confirmar = input(
                        "Está seguro que desea interrumpir el programa? SI/NO: "
                    )
                    if (
                        confirmar == "SI"
                        or confirmar == "si"
                        or confirmar == "Si"
                        or confirmar == "sí"
                        or confirmar == "Sí"
                    ):
                        print("Interrumpiendo el programa..")
                        exit()
                    elif confirmar == "NO" or confirmar == "no" or confirmar == "No":
                        print("El programa seguirá ejecutándose..")
                        break
                    else:
                        print("Por favor, responda SI / NO :")
                except KeyboardInterrupt:
                    print("Primero debe confirmar la interrupción.")


interrupcion()
