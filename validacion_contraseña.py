'''
Ejercicio 8: Validación de contraseña
Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.
'''

class Validador:

    def __init__(self, password = None):
        self.password = password 

    def verificar(self):
        
        while True:
            
            self.password =input("Introduzca la contraseña a validar: ")
            longitud = len(self.password)
            numeros = any(char.isdigit() for char in self.password)
            mayusculas = any(char.isupper() for char in self.password)
            
            if longitud > 7:
               
               
                
                if numeros:  

                    if  mayusculas:
                        print("La contraseña es válida")
                        break
                    else:
                        print("La contraseña debe tener mayúsculas y minúsculas, vuelva a intentarlo")

                else:
                    print("La contraseña debe tener al menos 1 numero, vuelva a intentarlo")
                    
            else:
                print("La contraseña es demasiado corta, debe tener al menos 8 caracteres contener numeros, intentelo de nuevo")
                
        
contraseña1 = Validador()

contraseña1.verificar()