import sys
'''Escribe un programa que convierta una cantidad de metros a kilómetros, centímetros y milímetros. La función debe recibir la cantidad de metros como parámetro y devolver un diccionario con las conversiones.

Contempla validar que la entrada sea un número positivo.'''

class ConversorMedidas():
    
    def __init__(self):
        #Creo dos listas con los keys y los values del futuro diccionario
        self.keys = ["kms","cms","mms"]
        self.values = []
        try:
            self.metros = float(input("Introduzca la cantidad de metros a convertir: "))
        except ValueError:
            print("Debe introducir solo numeros")
            ConversorMedidas()
    
    def km(self):
        kms = round(self.metros * 1000,2)
        self.values.append(kms)
       
    def cm(self):
        cms = round(self.metros / 100,2)
        self.values.append(cms)
        
    def mm(self):
        mms = round(self.metros / 1000,2)
        self.values.append(mms)
    
    def resultado(self):
        #Utilizo la funcion zip() para meter dentro del dccionario los valores de las listas self.keys y self.values
        diccionario = dict(zip(self.keys,self.values))
        print(f"Este es el resultado metido en un diccionario: {diccionario}")

medida1 = ConversorMedidas()

def menu():
    while True:
        print("Elige la unidad de Medida")
        print("1. Pasar a Kilometros")
        print("2. Pasar a centimetros")
        print("3. Pasar a milimetros")
        print("4. Mostrar resultados")
        print("0. Salir del programa")
        opcion = input("Introduzca la opcion deseada: ")
        
        if opcion == "1":
            medida1.km()
        if opcion == "2":
            medida1.cm()
        if opcion == "3":
            medida1.mm()
        if opcion == "4":
            medida1.resultado()
        if opcion == "0":
            print("Saliendo del programa...")
            sys.exit()# importo el modulo sys y así termino el menú para no usar un break
            
            
menu()