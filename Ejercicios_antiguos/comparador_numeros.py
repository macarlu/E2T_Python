number1 = int(input("Ingresa un numero: "))
number2 = int(input("Ingresa un numero: "))
number3 = int(input("Ingresa un numero: "))
largest_number = None
if number2 > number1 and number2 > number3:
    num_mas_grande = "number2",number2
elif number3 > number1 and number3 > number2:
    num_mas_grande = "number3",number3
else:
    num_mas_grande = "number1",number1
print("El número mas grande es el: ",num_mas_grande)
