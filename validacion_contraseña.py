'''
Ejercicio 8: Validación de contraseña
Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.
'''

class Validador:

    def __init__(self,password = ""):
        self.password = password 

    def verificar(self):
        
        while True:
            
            self.password =input("Introduzca la contraseña a validar: ")
            longitud = len(self.password)
            numeros = any(char.isdigit() for char in self.password)
            mayusculas = any(char.isupper() for char in self.password)
            minusculas = any(char.islower() for char in self.password)

            if longitud > 7:
                pass
            
                if numeros:
                    pass
                
                    if mayusculas:
                        pass

                        if minusculas:
                            pass
                    
                        else:
                            print("La contraseña debe tener al menos una minúscula")

                    else:
                        print("La contraseña debe tener al menos una mayúscula")
                else:
                    print("La contraseña debe tener al menos un número")

            else:
                print("La contraseña es demasiado corta, intentelo de nuevo")
                
            if longitud and numeros and mayusculas and minusculas:
                print("¡Enhorabuena!, la contraseña es válida")
                break

contraseña1 = Validador()

contraseña1.verificar()