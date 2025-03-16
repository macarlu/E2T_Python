
try:
    tfno = int(input("Introduzca el número de telefono en la agenda: "))
    contador =len(str(tfno))
    while True:
        if contador != 9:
            print("El número introducido no es correcto, debe tener 9 dígitos.")
            contador =len(str(tfno))
        while True:
            if contador != 9:
                print("El número introducido no es correcto, debe tener 9 dígitos.")
                tfno = int(input("Introduzca el número de telefono en la agenda: "))
            else:
                break
        else:
            break
except ValueError:
    print("El número introducido no es correcto, debe introducir solamente números.")
    
try:
    tfno = int(input("Introduzca el número de telefono en la agenda: "))
    contador =len(str(tfno))
    while True:
        if contador != 9:
            print("El número introducido no es correcto, debe tener 9 dígitos.")
            tfno = int(input("Introduzca el número de telefono en la agenda: "))
        else:
            break
except Exception:
    print("Error fatal")
"""
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
        print("La dirección de correo no es válida")"""

