'''Ejercicio 13: Rectángulo
Crea una clase Rectangulo con atributos para ancho y alto.
Incluye métodos para calcular el área y el perímetro, usando un constructor para inicializar los valores.'
'''

class Rectangulo:

    def __init__(self):
        try: 
            self.ancho = float(input("Introduzca el valor de la base: "))
            self.alto = float(input("Introduzca el valor de la altura: "))
        except ValueError:
            print("Debe introducir numeros, no letras")
            Rectangulo()

    def calcular_area(self):
        self.area = round(self.ancho * self.alto, 2)
        print(f"El area calculada es: {self.area}\n")

    def calcular_perimetro(self):
        self.perimetro = round(2 * (self.ancho + self.alto), 2)
        print(f"El perímetro calculado es: {self.perimetro}\n")

    def menu(self):

        while True:
            print("¡Vamos a calcular el area y perimetro de un rectangulo!")
            print("1. Calcula el area")
            print("2. Calcula el perímetro")
            print("0. Para salir del programa")
            opcion = input("Elija la opcion a realizar: ")
            if opcion == "1":
                calculo1.calcular_area()
            elif opcion == "2":
                calculo1.calcular_perimetro()
            elif opcion == "0":
                print("Saliendo del programa\n")
                break

calculo1 = Rectangulo()
calculo1.menu()