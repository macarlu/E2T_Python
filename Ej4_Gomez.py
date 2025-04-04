import random
'''Realiza una aplicación a tu elección que tenga una función útil.

La aplicación debe utilizar como minimo:

función o funciones
al menos un bucle for y un bucle while
al menos un if, un else y un elif
el código debe estar comentado correctamente en donde sea necesario.'''

class ContraseñaSegura:
    
    def __init__(self):
        self.minusculas = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.chars = ["º", "ª", "!", "|", "@", "·", "#", "$", "%", "&", "¬", "/", "(", ")", "=", "?", "'", "¡", "¿", "*", "+", "]", "^", "`", "[", "Ç", "}", "¨", "{", "_", "-", ".", ":", ",", ";" ]
        self.resultado = []
    
    def longitud(self):
        while True:
            try:
                self.long = int(input("Introduce la longitud de la contraseña: "))
                if self.long < 8:
                    print("La contraseña es demasiado corta, debe tener al menos 8 caracteres\n")
                else:
                    break

            except ValueError:
                print("Debe introducir solo números")
              
    def minusc(self):
        try:
            self.min = int(input("Introduce la cantidad de minúsculas de la contraseña: "))
            for l in range(1, self.min + 1):
                self.minuscula= random.choice(self.minusculas)
                self.resultado.append(self.minuscula)
            print(self.resultado)
        except ValueError:
            print("Debe introducir solo números")
                
    def mayusc(self):
        try: 
            self.may = int(input("Introduce la cantidad de mayúsculas de la contraseña: "))
            for l in range(1, self.may + 1):
                self.mayuscula= random.choice(self.mayusculas)
                self.resultado.append(self.mayuscula)
            print(self.resultado)
        except ValueError:
            print("Debe introducir solo números")
                 
    def nums(self):
        try:
            self.num = int(input("Introduce la cantidad de números de la contraseña: "))
            for n in range(1, self.num + 1):
                self.numero = random.randint(0,10)
                self.resultado.append(str(self.numero))
            print(self.resultado)
        except ValueError:
            print("Debe introducir solo números")
              
    def caracteres(self):
        try:
            self.char_es = int(input("Introduce la cantidad de caracteres especiales de la contraseña: "))
            for c in range(1, self.char_es + 1):
                self.caracter = random.choice(self.chars)
                self.resultado.append(self.caracter)
            print(self.resultado)
        except ValueError:
            print("Debe introducir solo números")
             
    def generar_contraseña(self):
        self.password = []
        try: 
            self.contraseña = random.choice(self.resultado)
            for c in range(1, self.long + 1):
                self.password.append(random.choice(self.resultado))
        except IndexError:
            print("Primero debe introducir los datos para conformar la contraseña")
            menu()
        
        '''
        uso "".join(lista)para evitar que la impresion sea una lista con corchetes y comillas
        delante de .join va el separador en este caso he puesto "", es decir nada que separe
        para que parezca una string'''  
        print("La contraseña generada es:", "".join(self.password))

password1 = ContraseñaSegura()

def menu():
    while True:
        print("*******************************************************")
        print("¡Bienvenido a tu generador de contraseñas ACME-3000!\n vamos a generar una contraseña segura, recuerda que al\n menos debe contener 8 caracteres y debe contener\n mayúsculas, minúsculas, números y carateres especiales")
        print("*******************************************************\n")
        print("1. Selecciona la longitud de la contraseña a generar")
        print("2. Selecciona la cantidad de minúsculas que debe contener")
        print("3. Selecciona la cantidad de mayúsculas que debe contener")
        print("4. Selecciona la cantidad de numeros que debe contener")
        print("5. Selecciona la cantidad de caracteres especiales que debe contener")
        print("6. Generar contraseña")
        print("0. Salir del programa")
        opcion = input("Seleccione una opcion para configurar su contraseña: ")
        
        if opcion == "1":
            password1.longitud()
        elif opcion == "2":
            password1.minusc()
        elif opcion == "3":
            password1.mayusc()
        elif opcion == "4":
            password1.nums()
        elif opcion == "5":
            password1.caracteres()
        elif opcion == "6":
            password1.generar_contraseña()
        elif opcion == "0":
            print("Gracias por usar ACME-3000...")
            exit()
menu()