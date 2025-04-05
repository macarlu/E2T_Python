def calcular_filas(bloques):
    fila_actual = 1
    bloques_utilizados = 0

    while bloques_utilizados + fila_actual <= bloques:
        bloques_utilizados += fila_actual
        fila_actual += 1

    return fila_actual - 1
try:
    bloques = int(input("Ingrese la cantidad de bloques: "))

    if bloques < 0:
        print("Por favor, ingrese un número no negativo.")

    else:
        filas = calcular_filas(bloques)
        print(f"Se pueden construir {filas} filas con {bloques} bloques.")

except ValuError:
    print("Por favor, ingrese un número válido.")