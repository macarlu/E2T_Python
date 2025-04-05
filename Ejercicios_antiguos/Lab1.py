x = float(input("Ingresa un valor para x: "))
a = float(x + 1/x)
b = float(x + 1/a)
c = float(x + 1/b)
y = c / b / a

print("y = ", y)

''' no me ha dado el resultado porque debe haber algo mal planteado en
las divisiones, pero sale aproximado, ;)'''