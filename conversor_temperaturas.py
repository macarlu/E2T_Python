import sys
'''
Ejercicio 4: Conversor de temperaturas
Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
Usa un constructor para inicializar una temperatura base.'''

class ConversorTemperatura:
    
       
    def __init__(self):
        self.temperatura = float(input("Introduzca la temperatura a convertir: "))
            
    def Celsius_Farenheit(self):
        resultado = round(((self.temperatura * 1.8) + 32),2)
        print(resultado)
        
          
    def Farenheit_Celsius(self):
        resultado = round(((self.temperatura -32) / 1.8),2)
        print(resultado)
    
    def Celsius_Kelvin(self):
        resultado = round((self.temperatura + 273.15),2)
        print(resultado)
        
    def Kelvin_Celsius(self):
        resultado = round((self.temperatura - 273.15),2)
        print(resultado)
        
    def Farenheit_Kelvin(self):
        resultado = round(((self.temperatura + 459.67) * 5/9),2)
        print(resultado)
        
    def Kelvin_Farenheit(self):
        resultado = round(((self.temperatura * 9/5) - 459.67),2)
        print(resultado)
        
def conversion():
    while True:
        print("Menu")
        print("1. Cambiar de Celsius a Farenheit")
        print("2. Cambiar de Farenheit a Celsius")
        print("3. Cambiar de Celsius a Kelvin")
        print("4. Cambiar de Kelvin a Celsius")
        print("5. Cambiar de Farenheit a Kelvin")
        print("6. Cambiar de Kelvin a Farenheit")
        print("7. Elegir una nueva temperatura")
        print("0. Salir del programa")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            temperatura1.Celsius_Farenheit()
           
        elif opcion ==  "2":
            temperatura1.Farenheit_Celsius()
           
        elif opcion ==  "3":
            temperatura1.Celsius_Kelvin()
           
        elif opcion ==  "4":
            temperatura1.Kelvin_Celsius()
           
        elif opcion ==  "5":
            temperatura1.Farenheit_Kelvin()
            
        elif opcion == "6":
            temperatura1.Kelvin_Farenheit()
            
        elif opcion == "7":
            ConversorTemperatura()
            
        elif opcion == "0":
            print("Sliendo del programa...")
            sys.exit()
            
temperatura1 = ConversorTemperatura()

conversion()