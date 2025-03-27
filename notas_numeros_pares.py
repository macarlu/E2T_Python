lista = [12,15,21,26,29,34,37,41,43,46,58,62,74,79,86]

def pares(x):
    return x % 2 == 0
      
    par = filter(pares, lista)

    print(list(par))


pares()