import sys

'''Ejercicio 11: Gestión de cuentas bancarias
Crea una clase CuentaBancaria con atributos para titular y saldo.
Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar saldos negativos.'''

class CuentaBancaria:
    
    def __init__(self, titular = None):
        self.titular = titular
        self.saldo = 0
        
    def retirar(self, reintegro):
        try:
            self.saldo = self.saldo - reintegro
            print("Atencion, recoja su dinero")
            print(f"Su saldo actual es de: {self.saldo}€\n")
        except
   
    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
        print(f"Su saldo actual es de: {self.saldo}€\n")

    def consultar_saldo(self):
        print(f"Su saldo actual es de: {self.saldo}€\n")
        
    def menu_cliente(self):
        
        while True:
            
            print("*******************************************************\n* Bienvenido a su banco que operacion desea realizar? *\n*******************************************************")
            print("1. Retirar dinero")
            print("2. Depositar dinero")
            print("3. Consultar el saldo disponible")
            print("0. Salir")
            self.opcion = int(input("Introduzca la opcion elegida: "))

            if self.opcion == 1:
                reintegro = int(input("Introduzca la cantidad a retirar: "))
                titular1.retirar(reintegro)

            elif self.opcion == 2:
                deposito = int(input("Introduzca la cantidad a depositar: "))
                titular1.depositar(deposito)

            elif self.opcion == 3:
                titular1.consultar_saldo()

            elif self.opcion == 0:
                sys(exit)               
            
titular1 = CuentaBancaria()  
titular1.menu_cliente()
