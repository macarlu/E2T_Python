print(2)
print(2.4)
print(2 + 3)
print(2 - 8)
print(4 * 3)
print(10 / 2)# devuelve siempre un float

print(2 ** 4)# devuelve 2 elevado a 4
print((2 + 3) * 5)# primero hace las operaciones entre parentesis

numero = 20
print(numero)
numero += 1
print(numero)

#numeros y funciones

def suma():
    print(2+3)
suma()

def suma_inteligente(a = 0,b= 0):# ponemos 0 como parametro default
    print(a + b)

suma_inteligente(7, 2.5)
suma_inteligente(3, -5)
suma_inteligente(3, 5)
suma_inteligente(3)# aquí cogería el valor default para 3 + 0

def resta(a = 0, b = 0):
    print(a - b)

resta(8, 4)
resta(-8, 4)
resta(8, 5.7)
resta(4)

def multiplicacion(a = 1, b = 1):
    print(a * b)

multiplicacion(2.5, 7)
multiplicacion(-2, 7)
multiplicacion(2)

def division(a = 1, b = 1):
    print(round(a / b, 2))# con la funcion round redondea el resultado

division(42.5, 7)
division(-2, 9)
division(2)