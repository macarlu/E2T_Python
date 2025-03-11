import json
import os

class Agenda:

    def __init__(self, archivo ="contactos2.json"):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def cargar_contactos(self):# para cargar todos nuestros contactos en la ram
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                return json.load(f)
        else:
            return {}
        
    def mostraragenda(self):
        if self.contactos:# Se podria poner == True, es lo mismo
            for nombre, info in self.contactos.items():
                print(f"Nombre: {nombre}")
                print(f"Teléfono: {info["telefono"]}")
                print(f"Email: {info["email"]}\n")
        else:
            print("La agenda está vacia")

agenda_test = Agenda()
agenda_test.mostraragenda()

