'''
Ejercicio 8: Validación de contraseña
Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.
'''

class Validador:

    def __init__(self):
        self.password = input("Introduzca la contraseña a validar: ")

    def verificar(self):
            
        while True:
        
            if len(self.password) <= 7:
                print("La contraseña es demasiado corta, vuelva a intentarlo")
                contraseña1.verificar()
            elif self.password.isdigit(): 
                print("La contraseña debe contener letras  numeros, vuelva a intentarlo ")
                Validador()
            
            for l in self.password:

                if not any l.islower():
                    print("La contraseña debe contener mayusculas y minusculas, vuelva a intentarlo")
                    contraseña1.verificar()

                elif not any l.isupper():
                    print("La contraseña debe contener mayusculas y minusculas, vuelva a intentarlo")
                    contraseña1.verificar()

            else:
                print("La contraseña introducida es válida")
                break

contraseña1 = Validador()

contraseña1.verificar()