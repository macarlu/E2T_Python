ancho = float(input("Introduzca el valor de la base: "))
alto = float(input("Introduzca el valor de la altura: "))

def calcular_area():
    area = ancho * alto
    print("El area calculada es:", area)

def calcular_perimetro():
    perimetro = 2 * (ancho + alto)
    print("El perímetro calculado es:", perimetro)

calcular_area()
calcular_perimetro()