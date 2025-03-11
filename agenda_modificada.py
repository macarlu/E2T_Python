import json
import os

class Agenda:

    def __init__(self, archivo ="contactos.json"):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def cargar_contactos(self):# para cargar todos nuestros contactos en la ram cada vez que empieza el programa
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        else:
            return {}
        
    def introducir_contacto(self):
        nuevocontacto = input("Introduzca nombre del nuevo contacto:")
        contacto = nuevocontacto.title()
        tfno = int(input("Introduzca el número de telefono en la agenda: "))
        email = input("Introduzca su direccion de correo electronico: ")
        mail = email.lower()
        self.contactoscontactos[contacto] = {'telefono': tfno, 'email': mail}
        print(f"{contacto} ha sido añadido correctamente a la agenda.")
        print(self.contactos)
        
    def mostraragenda(self):
        if self.contactos:# Se podria poner == True, es lo mismo
            for nombre, info in self.contactos.items():
                print(f"Nombre y Apellidos: {nombre}")
                print(f"Teléfono: {info['tfno']}")
                print(f"Email: {info["mail"]}\n")
        else:
            print("La agenda está vacia")

    
            


agenda_test = Agenda()
agenda_test.introducir_contacto()
#agenda_test.mostraragenda()

