password =input("Introduzca la contraseña a validar: ")
longitud = len(password)
numeros = any(char.isdigit() for char in password)
mayusculas = any(char.isupper() for char in password)
print(mayusculas)

if longitud >= 8:
    pass

    if numeros:
        pass
    
        if mayusculas == True:
            pass
        
        else:
            print("La contraseña debe tener al menos una mayuscula")
    else:
        print("La contraseña debe tener numeros")
        
 
   
else:
    print("La contraseña es demasiado corta, debe tener al menos 8 caracteres contener numeros, intentelo de nuevo")
                