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
contexto = {'amigos':{},'compañeros trabajo':{},'familia':{}}
contactos ={}
class Agenda:
    
    def __init__(self):
        pass
        
    def set_introducir_contacto_amigos(self):
        nuevocontacto = input("Introduzca nombre del nuevo contacto:")
        contacto = nuevocontacto.title()
        telefono = int(input("Introduzca el número de telefono en la agenda: "))
        contactos[contacto] = telefono
        contexto['amigos'] = (contacto,telefono)
        print(f"{contacto} ha sido añadido dentro del grupo de amigos.")

    def set_introducir_contacto_compañeros(self):
        nuevocontacto = input("Introduzca nombre del nuevo contacto:")
        contacto = nuevocontacto.title()
        telefono = int(input("Introduzca el número de telefono en la agenda: "))
        contactos[contacto] = telefono
        contexto['compañeros trabajo'] = (contacto,telefono)
        print(f"{contacto} ha sido añadido dentro del grupo de compañeros trabajo.")

    def set_introducir_contacto_familia(self):
        nuevocontacto = input("Introduzca nombre del nuevo contacto:")
        contacto = nuevocontacto.title()
        telefono = int(input("Introduzca el número de telefono en la agenda: "))
        contactos[contacto] = telefono
        contexto['familia'] = (contacto,telefono)
        print(f"{contacto} ha sido añadido dentro del grupo de familia.")

    def get_introducir_contacto_amigos(self):
        return self.contexto
    
    def get_introducir_contacto_compañeros(self):
        return self.contexto
    
    def get_introducir_contacto_familia(self):
        return self.contexto
   
    def set_borrar_contacto(self):
        borrado = input("Introduzca el contacto a eliminar de la agenda: ")
        eliminado = borrado.title()
        if eliminado in contactos:
            del(contactos[borrado])
            print(f"El contacto {eliminado} ha sido eliminado satisfactoriamente")
        else:
            print(f"{eliminado} no ha sido encontrado en la agenda")

    def set_buscar_contacto(self):
        busqueda = input("Introduzca el nombre a buscar en la agenda: ")
        buscado = busqueda.title()
        if buscado in contactos:
            print(f"El número de telefono buscado es: {contactos[buscado]}")
        else:
            print(f"{buscado} no ha sido encontrado en la agenda")
    
    def get_buscar_contacto(self):
        return self.buscado
    
    def set_mostrar_informacion(self):
        valores = contactos.items()
        print(f"Estos son tus contacto hasta el momento: {valores}")
           
def mostrar_agenda():
    
    while True:

        print("\nMenú :")
        print("1. Introducir un nuevo contacto")
        print("2. Buscar un contacto")
        print("3. Borrar un contacto")
        print("4. Mostrar la agenda al completo")
        print("0. Para salir del menú")
        opcion = int(input("Elige una de las opciones: "))
        
        if opcion == 1:
            print("\nMenú :")
            print("1. Agrupar nuevo contacto como amigo")
            print("2. Agrupar nuevo contacto como compañeros trabajo")
            print("3. Agrupar nuevo contacto como familia")
            opcion = int(input("Elige una de las opciones: "))
            
            if opcion == 1:
                agenda1.set_introducir_contacto_amigos()
            
            elif opcion == 2:
                agenda1.set_introducir_contacto_compañeros()

            elif opcion == 3:
                agenda1.set_introducir_contacto_familia()
                
        elif opcion == 2:
            agenda1.set_buscar_contacto()

        elif opcion == 3:
            agenda1.set_borrar_contacto()

        elif opcion == 4:
            print("\nMenú :")
            print("1. Mostrar contactos existentes como amigos")
            print("2. Mostrar contactos existentes como compañeros trabajo")
            print("3. Mostrar contactos existentes como familia")
            print("4. Mostrar total de contactos existentes")
            opcion = int(input("Elige una de las opciones: "))
            
            agenda1.set_mostrar_informacion()

        elif opcion == 0:
            print("Saliendo del programa...")
            sys.exit()
        
        else:
            print("El número elegido no es correcto, pruebe con otro")
            opcion = int(input("Elige una de las opciones: "))
        
        #print(contactos)
        print(contexto)

agenda1 = Agenda()        
           
mostrar_agenda()
                      
        
        
