# TP02 -Ejercicio 08
# Utilizar la técnica de listas por comprensión para construir una lista con todos los números impares comprendidos entre 100 y 200.

impares = [x for x in range(100, 201) if x % 2 == 1]
print(impares)
