'''
Realiza una función que compare dos listas y nos diga si son iguales (misma longitud y mismos elementos en cada indice)'''

'''
def compara():
    lista1=[1,2,3,4,8,6]
    lista2=[1,2,3,4,5,6]
    lista3= []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            for k in range(len(lista3)):
                if i != j or j != k or k != i:
                    break
                    print("Las listas son distintas")
                else:
                    if sorted(lista1) != sorted(lista2) or sorted(lista2) != sorted(lista3) or sorted(lista3) != sorted(lista1):
                        print("Las listas son distintas")
                    else:
                        print("Las listas son iguales")
   
   
compara()
'''

def comparador(l1,l2,l3):
    if len(l1) != len(l2) != len(l3):
        return "Son diferentes"
    else:
        for i in range(len(l1)):
            if l1[i] != l2[i] != l3[i] :
                return "Son diferentes"
        return "Son iguales"
    while True:
        x = int(input("Introduzca dato (para salir escriba -15489): "))
        if x!= -15489:
            lista3.append(x)
        else:
            break
            
lista1=[1,2,3,4,5,6]
lista2=[1,2,3,4,5,6]
lista3=[1,2,3,4,5]

print(comparador(lista1,lista2,lista3))