'''
Realiza una función que compare dos listas y nos diga si son iguales (misma longitud y mismos elementos en cada indice)'''
import time

def compara():
    lista1=[1,2,3,4,5,6]
    lista2=[1,2,3,4,5,6]
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if i != j :
                break
                print("Las listas son distintas")
            else:
                if sorted(lista1) != sorted(lista2):
                    print("Las listas son distintas")
                else:
                    print("Las listas son iguales")
   
compara()


def comparador(l1,l2):
    if len(l1) != len(l2):
        return "Son diferentes"
    else:
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return "Son diferentes"
        return "Son iguales"
            
lista1=[1,2,3,4,5,6]
lista2=[1,2,3,4,5,7]

print(comparador(lista1,lista2))