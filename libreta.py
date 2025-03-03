import random
libreta = []

nombre_cliente = " "
numero = 0


def insertar_libreta():
   
    nombre_cliente = input("Introduzca su nombre y apellidos: ")
    numero = random.randint(1,9999999999)

    libreta.insert(0,nombre_cliente)
    libreta.insert(1,numero)
    
    print(libreta)
   

insertar_libreta()
