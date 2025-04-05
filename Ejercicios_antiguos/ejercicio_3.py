valor = int(input("Ingrese la Tª que hace fuera: "))

def temperatura_agua(valor):
    if valor <= 0:
        print("Congelada")
    elif 1 <= valor <= 99:
        print("Liquida")
    else:
        print("Evaporándose")
temperatura_agua(valor)