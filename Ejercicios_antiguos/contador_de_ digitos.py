def contar_digitos(n):
    contador = 0
    num = n
    while num > 0:
        contador = contador + 1
        num = num // 10
    return print(contador)
contar_digitos(123)