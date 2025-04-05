def loteria():
    total = []
    valores_totales = 49
    for i in range((valores_totales - 1), 0, -1):
        valores_totales = valores_totales * i
        total.append(valores_totales)
        total_final = sorted(total)
        a = total_final[-1]

    extracto = []
    extracciones = 6
    for i in range((extracciones - 1), 0, -1):
        extracciones = extracciones * i
        extracto.append(extracciones)
        extracto_final = sorted(extracto)
        b = extracto_final[-1]

    diferente = []
    diferencia = 49 - 6
    for i in range((diferencia - 1), 0, -1):
        diferencia = diferencia * i
        diferente.append(diferencia)
        diferente_final = sorted(diferente)
        c = diferente_final[-1]

    resultado = a / (b * c)
    print(resultado)

loteria()