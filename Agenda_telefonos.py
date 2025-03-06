import sys
'''
Hacer una aplicacion àra tener una agenda de telefonos.
Crear la clase Agenda.
Los telefonos se gur¡ardaran en un diccionario con clave: Nombre del contacto y valor: Telefono.
Necesitamos los siguientes metodos:
    - __init__(por supuesto que siempre hace falta)
    - Método para introducir nuevo contacto
    - Método para borrar un contacto (por nombre)
    - Método para buscar un contacto (por nombre)
    - Método para mostrar toda la agenda.
'''

class Agenda:

    def __init__(self):
        contactos ={}
        contactos[self.set_introducir_contacto] = self.set_introducir_telefono

    def set_introducir_contacto(self, nuevocontacto):
        self.set_introducir_contacto = nuevocontacto
   
    def get_introducir_contacto(self):
        return self.get_introducir_contacto
    
    def set_introducir_telefono(self,telefono):
        self.set_introducir_telefono = telefono
    
    def get_introducir_telefono(self):
        return self.get_introducir_telefono
    
    def get_contactocreado(self):
        return contactos
    
    def set_borrar_contacto(self, borrado):
        self.set_borrar_contacto = borrado

    def set_buscar_contacto(self, busqueda):
        self.set_buscar_contacto = busqueda
    
    def get_buscar_contacto(self):
        return self.get_buscar_contacto
    
    def mostrar_informacion():
        pass
           
    def mostrar_agenda():
        while True:
            print("\nMenú :")
            print("1. Introducir un nuevo contacto")
            print("2. Buscar un contacto")
            print("3. Borrar un contacto")
            print("0. Para salir del menú")
            opcion = int(input("Elige una de las opciones: "))

            if opcion == 1:
                nuevocontacto = input("Introduzca el nombre en la agenda:")
                print(f"El nuevo contacto {nuevocontacto} ha sido añadido satisfactoriamente")
                telefono = int(input("Introduzca el número de telefono en la agenda: "))
                print("El nuevo numero de telefono ha sido añadido satisfactoriamente")
        
            elif opcion == 2:
                busqueda = input("Introduzca el nombre a buscar en la agenda: ")
                if busqueda in :
                

            elif opcion == 3:
                Agenda.set_borrar_contacto()

            elif opcion == 0:
                print("Saliendo del programa...")
                sys.exit()

            else:
                print("El número elegido no es correcto, pruebe con otro")
                opcion = int(input("Elige una de las opciones: "))
            
            print(contactos)
        
    mostrar_agenda()
                        
        
        
