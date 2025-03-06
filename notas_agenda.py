'''def insertardiccionario():
    contactos = {}
    for i in range(0,3):
        nuevocontacto = input("Introduzca el nombre en la agenda:")
        telefono = int(input("Introduzca el número de telefono en la agenda: "))
        contactos[nuevocontacto] = telefono

    print(contactos)
insertardiccionario()'''

def buscardiccionario():
    contactos = {'juanma': 605028411, 'maria': 605028412, 'carlota': 605028413, 'lucia':605028414}
    if 'juanma' in contactos:
        print(contactos['juanma'])
        
buscardiccionario()