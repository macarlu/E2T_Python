
'''Ejercicio 11: Gestión de cuentas bancarias
Crea una clase CuentaBancaria con atributos para titular y saldo.
Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar saldos negativos.'''

class CuentaBancaria:
    
    def __init__(self, titular = None):
        self.titular = titular
        self.saldo = 0
        
    def retirar(self, reintegro):

        try:
            if reintegro > self.saldo:
                raise ValueError("¡Saldo Insuficiente!")
            self.saldo = self.saldo - reintegro
            print("¡Atencion!, recoja su dinero")
            print(f"Su saldo actual es de: {self.saldo}€\n")

        except ValueError as e:
            print(e)
           
    def depositar(self, deposito):
        if deposito < 0:
            print("Debe introducir un número positivo")
            return # No deposita valores negativos
        self.saldo += deposito
        print(f"Su saldo actual es de: {self.saldo}€\n")

    def consultar_saldo(self):
        print(f"Su saldo actual es de: {self.saldo}€\n")
        
    def menu_cliente(self):
        
        while True:
            
            print("\n*******************************************************\n* Bienvenido a su banco que operacion desea realizar? *\n*******************************************************")
            print("1. Retirar dinero")
            print("2. Depositar dinero")
            print("3. Consultar el saldo disponible")
            print("0. Salir")
            try:
                opcion = int(input("Introduzca la opcion elegida: "))
                if opcion < 0 or opcion > 3:
                    raise ValueError("¡Debe introducir un nùmero del menú!")
                    continue
                
                if opcion == 1:
                    try:
                        reintegro = int(input("Introduzca la cantidad a retirar: "))
                        self.retirar(reintegro)
                    except ValueError:
                        print("Debe introducir un número")
                elif opcion == 2:
                    try:
                        deposito = int(input("Introduzca la cantidad a depositar: "))
                        self.depositar(deposito)
                        if deposito < 0:
                            raise ValueError
                    except ValueError:
                        print("Debe introducir un número positivo")
                elif opcion == 3:
                    self.consultar_saldo()
                elif opcion == 0:
                    break # Salimos del bucle
            except ValueError as e:
                print(e) 

titular1 = CuentaBancaria()  
titular1.menu_cliente()
