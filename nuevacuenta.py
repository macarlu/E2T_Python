import random

def almacenar_datos():
    cuenta = []
    cliente = input("Introduzca su nombre y apellidos: ")
    numero = random.randint(1,9999999999)
    cuenta.append(cliente)
    cuenta.append(numero)
    print(cuenta)


almacenar_datos()