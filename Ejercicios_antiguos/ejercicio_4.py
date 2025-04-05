edad = int(input("Ingrese la edad del juagador a fichar: "))
def categoria(edad):
    if 5 <= edad <= 7:
        print("Tu categoría es: Prebenjamines")
    elif 7 < edad <=9:
        print("Tu categoría es: Benjamines")
    elif 10 <= edad <= 11:
        print("Tu categoría es: Alevines")
    elif 12 <= edad <= 13:
        print("Tu categoría es: Infantiles")
    elif 14 <= edad <= 15:
        print("Tu categoría es: Cadetes")
    elif 16 <= edad <= 18:
        print("Tu categoría es: Juveniles")
    elif edad > 18:
        print("Tu categoría es: Senior")
    else:
        print("No es posible hacer ficha a esta edad")
categoria()