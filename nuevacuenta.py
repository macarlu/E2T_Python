import random

def almacenar_datos():
    cuenta = []
    banco = []
  
    for i in range(0,5):
        
        clientes = input("Introduzca su nombre y apellidos: ")
        numeros = str(random.randint(1,9999999999))
        cuenta.append(clientes)
        cuenta.append(numeros)
        banco.extend(cuenta)
        #print(cuenta)
    print(banco)


almacenar_datos()