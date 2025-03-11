
contactos ={}

def introducir_contacto():
    nuevocontacto = input("Introduzca nombre del nuevo contacto:")
    contacto = nuevocontacto.title()
    tfno = int(input("Introduzca el número de telefono en la agenda: "))
    email = input("Introduzca su direccion de correo electronico: ")
    mail = email.lower()
    contactos[contacto] = {'telefono': tfno, 'email': mail}
    print(f"{contacto} ha sido añadido dentro del grupo de amigos.")
    print(contactos)

introducir_contacto()