import json
import os
import sys

"""
Clase para gestionar una agenda de contactos. Permite añadir, buscar, modificar, borrar y guardar
contactos en un archivo JSON."""

class Agenda:

    def __init__(self, archivo ="contactos.json"):#Inicializa la agenda cargando los contactos desde un archivo JSON.
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def cargar_contactos(self):
    #Carga los contactos desde el archivo JSON si existe, de lo contrario, devuelve un diccionario vacío.
        
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r") as f:
                    return json.load(f)
            else:
                return {}
        except Exception as e:
            print(f"Se ha producido el error: {e} al cargar los datos del programa.")
            return {}
        
    def introducir_contacto(self):#Permite al usuario introducir un nuevo contacto en la agenda.
        contacto = str.title(input("Introduzca nombre y apellidos del nuevo contacto:"))
        
        try:#Permite asegurar que el número sea de 9 números y solo números.
            tfno = int(input("Introduzca el número de telefono en la agenda: "))
            contador =len(str(tfno))
            
            if contador != 9:
                print("El número introducido no es correcto, debe tener 9 dígitos.")
                tfno = int(input("Introduzca el número de telefono en la agenda: "))
                
        except ValueError:
            print("El número introducido no es correcto, debe introducir solamente números.")
            
            try:
                tfno = int(input("Introduzca el número de telefono en la agenda: "))
                contador =len(str(tfno))
                if contador != 9:
                    print("El número introducido no es correcto, debe tener 9 dígitos.")
                    tfno = int(input("Introduzca el número de telefono en la agenda: "))
            except Exception:
                print("Se ha producido un error, comience de nuevo")
                agenda_test.introducir_contacto()

        try:
            email = input("Introduzca la direccion de correo electronico: ")
            mail = email.lower()
            arroba = mail.index("@")
            puntocom = mail.index(".com")
    
        except ValueError:
            print("La dirección de correo no es válida")
            
        try:
            email = input("Introduzca la direccion de correo electronico: ")
            mail = email.lower()
            arroba = mail.index("@")
            puntocom = mail.index(".com")
            
        except ValueError:
            print("Se ha producido un error, comience de nuevo")
            agenda_test.introducir_contacto()
        
        self.contactos[contacto] = {'telefono': tfno, 'email': mail}
        print(f"{contacto} ha sido añadido correctamente a la agenda.")
        
    def buscar_contacto(self):#Busca un contacto por nombre y muestra su información si existe.
        busqueda = str.title(input("Introduzca el nombre a buscar en la agenda: "))
        
        if busqueda in self.contactos:
            buscado = self.contactos[busqueda]
            print(f"El número de telefono buscado es: {buscado['telefono']}")
            print(f"La dirección de correo buscada es: {buscado['email']}")
        else:
            print(f"{busqueda} no ha sido encontrado en la agenda")

    def modificar_contacto(self):#Modifica un contacto existente permitiendo cambiar nombre, teléfono o email.
        cambio = str.title(input("Introduzca el contacto a modificar: "))
        
        if cambio in self.contactos:
            contacto_actual = self.contactos[cambio]  

            while True:
                print("\n=====Submenú de modificacion===== ")
                print("1. Modificar nombre o apellidos del contacto.")
                print("2. Moficar número de telefono.")
                print("3. Modificar dirección de correo electrónico.")
                print("0. Para salir del submenú")
                opcion = int(input("Elige una de las opciones: "))

                if opcion == 1:
                    cambio_nombre = str.title(input("Introduzca la modificación en nombre o apellidos: "))
                    self.contactos[cambio_nombre] = self.contactos.pop(cambio) 
                    print("Modificado correctamente.")
                
                elif opcion == 2:
                    cambio_tfno = int(input("Introduzca el nuevo número de teléfono: "))
                    print("El teléfono ha sido modificado")
                    self.contactos[cambio]['telefono'] = cambio_tfno 
                    print(f"El nuevo número de teléfono es: {self.contactos[cambio]['telefono']}")

                elif opcion == 3:
                    cambio_mail = input("Introduzca el nuevo correo electrónico:")
                    print("El correo ha sido modificado")
                    self.contactos[cambio]['email'] = cambio_mail
                    print(f"La dirección de correo buscada es: {self.contactos[cambio]['email']}")

                elif opcion == 0:
                    agenda_test.guardar_agenda()
                    print("Saliendo del submenu...")
                    return
        else:
            print(f"{cambio} no ha sido encontrado en la agenda")

    def borrar_contacto(self):#Elimina un contacto de la agenda si existe.
        borrado = str.title(input("Introduzca el contacto a borrar: "))
        if borrado in self.contactos:
            self.contactos.pop(borrado)
            print(f"El contacto {borrado} ha sido eliminado satisfactoriamente")
        else:
            print(f"{borrado} no ha sido encontrado en la agenda")

    def guardar_agenda(self):#Guarda agenda en un archivo JSON.
        with open(self.archivo, "w") as f:
            json.dump(self.contactos, f, indent=4)
            return f"Agenda guardada correctamente"

    def mostraragenda(self):#Muestra todos los contactos guardados en la agenda.
        if self.contactos:# Se podria poner == True, es lo mismo
            for nombre, info in self.contactos.items():
                print(f"Nombre y Apellidos: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info['email']}\n")
        else:
            print("La agenda está vacia")

def mostrar_menu(): #Muestra el menú principal y permite al usuario interactuar con la agenda.
    
    while True:

        print("\n=========  Menú  ==========\n___________________________\n")
        print("1. Introducir contacto")
        print("2. Buscar telefono contacto")
        print("3. Modificar contacto")
        print("4. Borrar contacto")
        print("5. Mostrar agenda completa")
        print("0. Para salir del menú")
        opcion = int(input("Elige una de las opciones: "))

        if opcion == 1:
            agenda_test.introducir_contacto()

        elif opcion == 2:
            agenda_test.buscar_contacto()

        elif opcion == 3:
            agenda_test.modificar_contacto()

        elif opcion == 4:
            agenda_test.borrar_contacto()

        elif opcion == 5:
            agenda_test.mostraragenda()

        elif opcion == 0:
            agenda_test.guardar_agenda()
            print("Saliendo del programa...")
            sys.exit()
            
agenda_test = Agenda()
mostrar_menu()

if __name__ == "__main__":
    mostrar_menu()
