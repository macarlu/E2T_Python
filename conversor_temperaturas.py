'''
Ejercicio 4: Conversor de temperaturas
Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
Usa un constructor para inicializar una temperatura base.'''

class ConversorTemperatura:
    
       
    def __init__(self):
        self.temperatura = input("Introduzca la temperatura a convertir: ")
            
    def Celsius_Farenheit(self):
        print((self.temperatura * 1.8) + 32)
        
          
    def Farenheit_Celsius(self):
        print((self.temperatura -32) / 1.8)
        
    
    def Celsius_Kelvin(self):
       print(self.temperatura + 273.15)
        
        
    def Kelvin_Celsius(self):
        print(self.temperatura - 273.15)
      
        
    def Farenheit_Kelvin(self):
        print((self.temperatura + 459.67) * 5/9)
        
        
    def Kelvin_Farenheit(self):
        print((self.temperatura * 9/5) - 459.67)
        
        
def conversion():
    while True:
        print("Menu")
        print("1. Cambiar de Celsius a Farenheit")
        print("2. Cambiar de Farenheit a Celsius")
        print("3. Cambiar de Celsius a Kelvin")
        print("4. Cambiar de Kelvin a Celsius")
        print("5. Cambiar de Farenheit a Kelvin")
        print("6. Cambiar de Kelvin a Farenheit")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            temperatura1.Celsius_Farenheit
            break
        elif opcion ==  "2":
            temperatura1.Farenheit_Celsius
            break
        elif opcion ==  "3":
            temperatura1.Celsius_Kelvin
            break
        elif opcion ==  "4":
            temperatura1.Kelvin_Celsius
            break
        elif opcion ==  "5":
            temperatura1.Farenheit_Kelvin
            break
        elif opcion == "6":
            temperatura1.Kelvin_Farenheit
            break
            
temperatura1 = ConversorTemperatura()

conversion()