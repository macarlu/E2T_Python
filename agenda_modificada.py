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
        self.contactos[contacto] = {'telefono': tfno, 'email': mail}
        print(f"{contacto} ha sido añadido correctamente a la agenda.")
        print(self.contactos)

    def buscar_contacto(self):
        busqueda = str.title(input("Introduzca el nombre a buscar en la agenda: "))
        #buscado = busqueda.title()
        if busqueda in self.contactos:
            buscado = self.contactos[busqueda]
            print(f"El número de telefono buscado es: {buscado['telefono']}")
            print(f"La dirección de correo buscada es: {buscado['email']}")
        else:
            print(f"{buscado} no ha sido encontrado en la agenda")

    def borrar_contacto(self):
        borrado = str.title(input("Introduzca el contacto a borrar: "))
        if borrado in self.contactos:
            self.contactos.pop(borrado)
            print(f"El contacto {borrado} ha sido eliminado satisfactoriamente")
        else:
            print(f"{borrado} no ha sido encontrado en la agenda")

    def guardar_agenda(self):#para guardarlo en el archivo json
        with open(self.archivo, "w") as f:
            json.dump(self.contactos, f, indent=4)
            return f"Agenda guardada correctamente"
        





        
    def mostraragenda(self):
        if self.contactos:# Se podria poner == True, es lo mismo
            for nombre, info in self.contactos.items():
                print(f"Nombre y Apellidos: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info["email"]}\n")
        else:
            print("La agenda está vacia")

    
            


agenda_test = Agenda()
agenda_test.introducir_contacto()
agenda_test.buscar_contacto()
agenda_test.borrar_contacto()
agenda_test.mostraragenda()

