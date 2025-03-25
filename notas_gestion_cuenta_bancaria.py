import random
import json
import os

#def registrarse():
titular = {}
cuentas = {}
registro = banco.json

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
    
    
    '''num_cuenta = random.randint(0,11)
    nombre = input("Introduzca su nombre y apellidos: ")
    password = input("Introduce una contraseña: ")
    titular = {'nombre': nombre, 'password': password}
    print(titular)
    
registrarse()'''

def identificarse():
    validar_nombre = input("Introduzca su nombre y apellidos: ")
    validar_nombre in registro:
        validar_password = input("Introduzca su contraseña: ")
        if validar_password == password:
            pritn