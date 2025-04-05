base = float(input("Ingrese un valor para la base: "))
altura = float(input("Ingrese un valor para la altura: "))

def area_triangulo(base, altura):
    resultado = round(base * altura/2,2)
    return resultado
print("El área del triángulo es igual a: ", {area_triangulo(base, altura)})