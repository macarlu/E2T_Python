import time

def lista_primos():
    primos=[]
    num=int(input("Introduce el número final: "))
    inicio= time.time()
    for i in range(2,num+1):
        for j in range(2,i-1):
            if i % j == 0:
                 break
        else:
            primos.append(i)
    fin=time.time()
    print(primos)
    print(f"Ha tardado {round(fin-inicio),4} segundos")
lista_primos()

