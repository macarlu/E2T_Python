def primos():
    num = (int(input("Ingrese el número que quiere comprobar: ")

    if num <= 2:
        print(f"Es primo, porque no tiene divisor, salvo la unidad y el mismo ")

    else:
        for i in range(2, num):
            if num % i == 0:
            print(f"No es primo, porque {i} es su divisor.")
        else:
            print("Es primo, porque no tiene divisor, salvo la unidad y el mismo ")

primos()