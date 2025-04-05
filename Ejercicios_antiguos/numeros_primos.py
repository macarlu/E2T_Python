
def primos():

    num = (int(input("Ingrese el número que quiere comprobar: ")
    for i in range(2, num + 1):
        if num % i == 0:
        print(f"No es primo, porque {i} es su divisor.")
            if num == i:
                pass
    else:
        print("Es primo, porque no tiene divisor, salvo la unidad y el mismo ")

primos()
