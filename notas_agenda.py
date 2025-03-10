'''def insertardiccionario():
    contactos = {}
    for i in range(0,3):
        nuevocontacto = input("Introduzca el nombre en la agenda:")
        telefono = int(input("Introduzca el número de telefono en la agenda: "))
        contactos[nuevocontacto] = telefono

    print(contactos)
insertardiccionario()

def buscardiccionario():
    contactos = {'juanma': 605028411, 'maria': 605028412, 'carlota': 605028413, 'lucia':605028414}
    if 'juanma' in contactos:
        print(contactos['juanma'])
        
buscardiccionario()'''

contexto = {'amigos':{},'compañeros trabajo':{},'familia':{}}
contactos = {}

def agrupar_contacto():
    while True:
            print("\nMenú :")
            print("1. Introducir un nuevo contacto")
            opcion = int(input("Elige una de las opciones: "))
        
            if opcion == 1:
                print("\nMenú :")
                print("1. Agrupar nuevo contacto como amigo")
                print("2. Agrupar nuevo contacto como compañeros trabajo")
                print("3. Agrupar nuevo contacto como familia")
                opcion = int(input("Elige una de las opciones: "))

                if opcion == 1:
                    nuevocontacto = input("Introduzca nombre del nuevo contacto:")
                    contacto = nuevocontacto.title()
                    telefono = int(input("Introduzca el número de telefono en la agenda: "))
                    contactos[contacto] = telefono
                    contexto['amigos'] = (contacto,telefono)
                    print(f"{contacto} ha sido añadido dentro del grupo de amigos.")

                elif opcion == 2:
                    nuevocontacto = input("Introduzca nombre del nuevo contacto:")
                    contacto = nuevocontacto.title()
                    telefono = int(input("Introduzca el número de telefono en la agenda: "))
                    contactos[contacto] = telefono
                    contexto['compañeros trabajo'] = (contacto,telefono)
                    print(f"{contacto} ha sido añadido dentro del grupo de compañeros trabajo.")

                elif opcion == 3:
                    nuevocontacto = input("Introduzca nombre del nuevo contacto:")
                    contacto = nuevocontacto.title()
                    telefono = int(input("Introduzca el número de telefono en la agenda: "))
                    contactos[contacto] = telefono
                    contexto['familia'] = (contacto,telefono)
                    print(f"{contacto} ha sido añadido dentro del grupo de familia.")

            print(contexto)
            print(contactos)
agrupar_contacto()