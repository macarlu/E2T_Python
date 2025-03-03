import random
import sys

'''
Crea la clase "Cuenta".
Cada cuenta tendrá un número (diferente a las demás) y un saldo (float).
El número de cuenta se puede consultar y modificar (getter y setter)
Pero el saldo tenemos que hacer un ingreso o una retirada.

Para modificar el saldo tenemos que hacer un ingreso o una retirada'''

class Cuenta:
 
    def __init__(self):
        self.num_cuenta = []
        self.cliente = []
        self.saldo = float()
        
    def set_num_cuenta(self,numero):
        self.num_cuenta = numero

    def get_num_cuenta(self):
        return self.numero
        return self.saldo
    
    def set_ingresar(self,ingreso):
        self.ingreso = ingreso
        self.saldo = ingreso + self.saldo
        
    def get_ingresar(self):
        return self.ingreso
           
    def set_retirar(self,retirada):
        self.retirada = retirada
        self.saldo = self.saldo - retirada
        
    def get_retirar(self):
        return self.retirada
        
    
def operaciones():
    cuenta = Cuenta()
    
    
    while True:
        print("\nMenu:\n-----")
        print("1. Registrese como Cliente")
        print("2. Ingresar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Consultar nº de cuenta")
        print("6. Salir")
        operacion = int(input("Seleccione la operación a realizar: "))

        if operacion == 1:
            nombre_cliente = input("Introduzca su nombre y apellidos: ")
            numero = random.randint(1,9999999999)
            cuenta.cliente.append(nombre_cliente)
            cuenta.num_cuenta.append(numero)

        if operacion == 2:
            ingreso = float(input("Introduzca la cantidad a ingresar: "))
            cuenta.set_ingresar(ingreso)
                    
        elif operacion == 3:
            retirada = float(input("Introduzca la cantidad a retirar: "))
            cuenta.set_retirar(retirada)
            
        elif operacion == 4:
            print(f"El saldo de su cuenta es de {cuenta.saldo} euros.")
        
        elif operacion == 5:
            print(f"El numero de cuenta de {nombre_cliente} es {numero}")
        
        elif operacion == 6:
            print(f"Saliendo del programa...")
            sys.exit()
        

operaciones()


    