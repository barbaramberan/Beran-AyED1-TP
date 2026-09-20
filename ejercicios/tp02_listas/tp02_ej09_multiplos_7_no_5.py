# TP02 - Ejercicio 09
# Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 que no sean múltiplos de 5. A y B se ingresar desde el teclado.
# Yo voy a utilizar unicamente valores positivos.

print("Vamos a crear una lista con todos los números que sean múltiplos de 7, pero no  de 5, en un rango determinado por vos.\n")

a = int(input("Ingresá un número entero positivo para definir donde querés que empiece ese rango: "))
b = int(input("Ingresá un número entero positivo para definir donde querés que termine ese rango: "))

multiplos = [num for num in range(a, b + 1) if num % 7 == 0 and num % 5 != 0]

print(f"La lista de múltiplos entre {a} y {b}, quedó asi:\n{multiplos}")