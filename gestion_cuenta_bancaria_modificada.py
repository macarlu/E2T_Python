import random
import json
import os
import sys
'''Ejercicio 11: Gestión de cuentas bancarias
Crea una clase CuentaBancaria con atributos para titular y saldo.
Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar saldos negativos.'''

class CuentaBancaria:

    def __init__(self, registro = "banco.json"):
        self.registro = registro
        self.cuentas = []
        self.titular = {}
        

    def cargar_registro(self):
        try:
            if os.path.exists(self.registro):
                with open(self.registro, "r") as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            print(f"Se ha producido el error: {e} al cargar los datos del programa.")
            return []

    def registrarse(self):
        self.num_cuenta = random.randint(0,11)
        self.nombre = input("Introduzca su nombre y apellidos: ")
        self.password = input("Introduce una contraseña")
        self.titular = {'nombre': self.nombre, 'password': self.password}
        print(self.cuentas)
        
    def identificarse(self):
        self.validar_nombre = input("Introduzca su nombre y apellidos: ")
        if self.validar_nombre in self.registro:
            self.validar_password = input("Introduzca su contraseña: ")
            if self.validar_password == self.password:
                cuenta1.menu_cliente()
            
    
    

   
    def retirar(self):
   
    def depositar(self):


    


    def consultar_saldo(self:)
    
    
    
    
    def guardar_archivo(self):#Guarda en un archivo JSON.
        with open(self.registro, "w") as f:
            json.dump(self.alumnos, f, indent=4)
            print(f"Archivo guardado correctamente\n")

    def menu_cliente(self):
        while True:
            print("Bienvenido a su banco que operacion desea realizar?")
            print("1. Retirar dinero")
            print("2. Depositar dinero")
            print("3. Consultar el saldo disponible")
            print("0. Salir")
            self.opcion = int(input("Introduzca la opcion elegida: "))



    
def cajero():
    while True:
        print("Menú")
        print("1. Registrarse como cliente")
        print("2. Identificarse")
        print("0. Salir")
        opcion = int(input("Introduzca la opcion elegida: "))

        if opcion == 1:
            cuenta1.registrarse()
        
        elif opcion == 2:
            cuenta1.identificarse()
            
        elif opcion == 0:
            sys.exit()
            





cuenta1 = CuentaBancaria()



