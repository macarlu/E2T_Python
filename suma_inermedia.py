import random 
numeros = []
def suma_intermedia():
    lista_num = []
    a = random.randint(1, 11)
    b = random.randint(1, 11)
    lista_num.append(a)
    lista_num.append(b)
    print(lista_num)
    if b > a:
            a, b = b, a
            
    for i in range(a,b+1):
        numeros.append(i)
        print(f"Números intermedios: {numeros}")
        suma = sum(numeros)
        print(f"Suma de los números intermedios: {suma}")
suma_intermedia()
