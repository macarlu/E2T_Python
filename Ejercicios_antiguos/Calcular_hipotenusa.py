leg_a = float(input("Introduzca la longitud del primer cateto: "))
leg_b = float(input("Introduzca la longitud del segundo cateto: "))
hypo = round((leg_a ** 2 + leg_b ** 2) ** .5,2)#Así calculamos la raiz cuadrada ** .5
print("la longitud de la hipotenusa es:", hypo)